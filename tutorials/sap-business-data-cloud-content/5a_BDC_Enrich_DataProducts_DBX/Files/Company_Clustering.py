# Databricks notebook source
# MAGIC %md
# MAGIC ## Company data clustering
# MAGIC Based on the company data product we consume it in order to cluster the data. To provide the data to the cluster algorithm, we prepare the data by handling Null values and afterwards perform a One Hot Encoding in order to get a dataframe only containing numerical values. Prior to applying the model, we optimize selected hyperparameters of the Affinity Propagation clustering algorithm. After performing the hyperparameter tuning, we select the model with the highest silhouette score. This model is used in order to then apply the model for the clustering approach. In order to be able to visualize the data in a dashboard, we perform a PCA to reduce the dimensionality of the prepared dataset.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Install packages
# MAGIC All necessary packages for this notebook are going to be outlined in the following notebook cell. In order to make sure that the results are reproducible, the following package versions are going to be installed

# COMMAND ----------

# MAGIC %pip install mlflow
# MAGIC %pip install bayesian-optimization
# MAGIC %pip install databricks-feature-engineering
# MAGIC %restart_python

# COMMAND ----------

# MAGIC %md
# MAGIC ### Import packages

# COMMAND ----------

# Upgrade typing_extensions to a compatible version
%pip install --upgrade typing_extensions

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max
from pyspark.sql.types import DecimalType
import pandas as pd
from delta import *
import pandas as pd
import mlflow
from mlflow.models import infer_signature
from pathlib import Path
from sklearn.cluster import AffinityPropagation
from sklearn.manifold import TSNE
import numpy as np
from sklearn.metrics.cluster import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from bayes_opt import BayesianOptimization
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events
import pyspark

# COMMAND ----------

# MAGIC %md
# MAGIC ### Setup Spark Session and consume data product

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS company_code_data_product;
# MAGIC SET CATALOG company_code_data_product;
# MAGIC CREATE SCHEMA IF NOT EXISTS company_code;
# MAGIC USE SCHEMA company_code;

# COMMAND ----------

spark = SparkSession.builder.appName("company_clustering").getOrCreate()
data = spark.read.table("companycode_share.companycode.companycode")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data preparation
# MAGIC When consuming the dataset, we select a subset of the company data product which does not consider columns that contain unique identifiers. In order to prepare the company dataset, we need to transform the boolean and character columns into a numeric representation. For the boolean columns we replace the `True` value to 1 and the `False` value to 0. For the character columns we encode the values by applying a One Hot Encoder. In case a column only contains null values, we remove the columns.

# COMMAND ----------

def drop_fully_null_columns(df, but_keep_these=[]):
    """Drops DataFrame columns that are fully null
    (i.e. the maximum value is null)

    Arguments:
        df {spark DataFrame} -- spark dataframe
        but_keep_these {list} -- list of columns to keep without checking for nulls

    Returns:
        spark DataFrame -- dataframe with fully null columns removed
    """

    # skip checking some columns
    cols_to_check = [col for col in df.columns if col not in but_keep_these]
    if len(cols_to_check) > 0:
        # drop columns for which the max is None
        rows_with_data = df.select(*cols_to_check).groupby().agg(*[max(c).alias(c) for c in cols_to_check]).take(1)[0]
        cols_to_drop = [c for c, const in rows_with_data.asDict().items() if const == None]
        cleaned_df = df.drop(*cols_to_drop)

        return cleaned_df
    else:
        return df

# COMMAND ----------

from pyspark.sql.functions import col

clustering_data = data.select(
    "CompanyCode", "Country", "Currency", "Language", "ControllingArea", 
    "CreditControlArea", "FiscalYearVariant", "FieldStatusVariant", 
    "TaxRptgDateIsActive", "DocDateIsUsedForTaxDetn", "FinancialManagementArea", 
    "ExtendedWhldgTaxIsActive", "CashDiscountBaseAmtIsNetAmt", "NonTaxableTransactionTaxCode"
)
clustering_data = clustering_data.replace('', None)

# Convert boolean columns to integer
for column, column_dtype in clustering_data.dtypes:
    if column_dtype == 'boolean':
        clustering_data = clustering_data.withColumn(column, col(column).cast('integer'))

clustering_data = drop_fully_null_columns(clustering_data)

# Replace string values
replace_string_values = {column: f"No{column}" for column, col_dtypes in clustering_data.dtypes if col_dtypes == "string" and column != "CompanyCode"}
clustering_data = clustering_data.fillna(replace_string_values)
# display(clustering_data)

# COMMAND ----------

# MAGIC %md
# MAGIC In order to apply the dataset, we transform the prepared Spark dataframe to a Pandas dataframe. The column Company Code, which is the primary key is going to be removed and assigned to a separate variable. we perform the One Hot Encoding over the pandas library functionality

# COMMAND ----------

# MAGIC %md
# MAGIC ### Hyperparameter tuning
# MAGIC In order to select an optimal set of hyperparameters, we apply a Bayesian Search optimization in order to determine an optimal set of parameter combination. We want to therefore maximize the silhouette score. As a clustering algorithm we use the Affinity Propagation from scikit-learn. For the Bayesian Search optimization we define the following parameters:
# MAGIC - random_iteration (number of iteration for random selection of hyperparameters to define search space)
# MAGIC - optimization_iteration (number of optimization iteration of hyperparamter tuning process)

# COMMAND ----------

clustering_data = clustering_data.toPandas()
company_code_data = clustering_data.pop("CompanyCode")
clustering_data = pd.get_dummies(data=clustering_data, dtype=int)

# COMMAND ----------

def cluster_scoring(cluster_labels:np.array, data: pd.DataFrame) -> tuple:
    """
    Computes cluster evaluation metrics for a given set of cluster labels and data points.

    This method calculates three clustering quality metrics:
    - Silhouette Score: Measures how similar an object is to its own cluster compared to other clusters.
    - Calinski-Harabasz Index: Evaluates the ratio of between-cluster dispersion to within-cluster dispersion.
    - Davies-Bouldin Index: Measures the average similarity ratio of each cluster with the one most similar to it.

    Args:
        cluster_labels (np.array): An array of cluster labels for each data point, as assigned by a clustering algorithm.
        data (pd.DataFrame): The dataset used for clustering, where each row represents a data point and each column represents a feature.

    Returns:
        tuple: A tuple containing:
            - silhouette_scoring (float): The Silhouette Score (higher is better, -1 if there is only one cluster).
            - calinski_score (float): The Calinski-Harabasz Index (higher is better, 0 if there is only one cluster).
            - davies_score (float): The Davies-Bouldin Index (lower is better, infinity if there is only one cluster).
    """
    number_labels = len(set(cluster_labels))
    if number_labels > 1:
        silhouette_scoring = silhouette_score(data, labels=cluster_labels)
        calinski_score = calinski_harabasz_score(data, cluster_labels)
        davies_score = davies_bouldin_score(data, cluster_labels)
    else:
        silhouette_scoring, calinski_score, davies_score = -1, 0, np.inf
    return silhouette_scoring, calinski_score, davies_score

# COMMAND ----------

def affinity_clustering_hpt(damping: float, max_iter: float, convergence_iter: float, data: pd.DataFrame=clustering_data):
    """
    Perform hyperparameter tuning and model training using the Affinity Propagation clustering algorithm.

    This method initializes an Affinity Propagation model with the specified parameters, fits it to the provided dataset,
    and evaluates clustering performance using silhouette, Calinski-Harabasz, and Davies-Bouldin scores. Model and metrics
    are logged to MLflow for tracking purposes.

    Args:
        damping (float): The damping factor between 0.5 and 1.0 that adjusts the extent to which the responsibility and availability
                         messages are updated with each iteration in the Affinity Propagation algorithm.
        max_iter (float): The maximum number of iterations for the model to converge. This value is rounded to the nearest integer.
        convergence_iter (float): The number of iterations with no change in the estimated clusters before convergence is
                                  declared. This value is rounded to the nearest integer.
        data (pd.DataFrame, optional): The dataset to fit the model on. Defaults to `clustering_data`.

    Returns:
        float: The silhouette score evaluating clustering quality, where a higher score indicates better-defined clusters.
    """
    max_iter = int(round(max_iter, 0))
    convergence_iter = int(round(convergence_iter, 0))
    with mlflow.start_run():
        affinity_model = AffinityPropagation(damping=damping, max_iter=max_iter, convergence_iter=convergence_iter)
        cluster_labels = affinity_model.fit_predict(data)
        silhouette_scoring, calinski_score, davies_score = cluster_scoring(cluster_labels, data)
        input_example = data[:5]
        signature = infer_signature(input_example, model_output=cluster_labels)
        mlflow.sklearn.log_model(affinity_model, artifact_path="model", signature=signature)
        mlflow.log_params(affinity_model.get_params())
        mlflow.log_param("clustering_model", "Affinity Propagation")
        mlflow.log_metrics({"silhouette_score": silhouette_scoring, "calinski_harabasz_score": calinski_score, "davies_bouldin_score": davies_score})
    return silhouette_scoring

# COMMAND ----------

random_iteration = 5
optimization_iteration = 20

# COMMAND ----------

# MAGIC %md
# MAGIC #### Define MLflow setup

# COMMAND ----------

notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
root_path = str(Path(notebook_path).parent)

# COMMAND ----------

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment(f"{root_path}/Company clustering")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Run Hyperparameter optimization
# MAGIC For the Affinity Propagation we define the following Hyperparameters and the respective search range:
# MAGIC - damping: [0.5, 0.99999]
# MAGIC - max_iter: [10, 4000]
# MAGIC - convergence_iter: [10, 4000]

# COMMAND ----------

affinity_propagation_parameter_bound = {"damping": (0.5, 0.99999), "max_iter": (10, 4000), "convergence_iter": (10, 4000)}
ap_bo_optimizer = BayesianOptimization(
    f=affinity_clustering_hpt,
    pbounds=affinity_propagation_parameter_bound,
    random_state=42
)
ap_bo_optimizer.maximize(init_points=random_iteration, n_iter=optimization_iteration)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Retrieval of runs after hyperparameter tuning
# MAGIC In order to retrieve the runs from the hyperparameter tuning, we search runs under the used experiment. We will retrieve the run with the highest silhouette score to perform our predictions. 

# COMMAND ----------

cluster_runs = mlflow.search_runs()
if "metrics.silhouette_score" in cluster_runs.columns:
    run_id = cluster_runs.sort_values("metrics.silhouette_score", ascending=False).head(1).loc[:, "run_id"].tolist()[0]
    logged_model = f"runs:/{run_id}/model"
else:
    raise KeyError("The column 'metrics.silhouette_score' does not exist in the search results.")
run_id = cluster_runs.sort_values("metrics.silhouette_score", ascending=False).head(1).loc[:,"run_id"].tolist()[0]
logged_model = f"runs:/{run_id}/model"

# COMMAND ----------

clustering_prediction_data = np.ascontiguousarray(clustering_data)

# COMMAND ----------

# Load model as a Spark UDF. Override result_type if the model does not return double values.
loaded_model = mlflow.sklearn.load_model(model_uri=logged_model)
cluster_labels = loaded_model.predict(clustering_prediction_data)

# COMMAND ----------

tsne_model = TSNE(n_components=2)
tsne_data = tsne_model.fit_transform(clustering_data)
tsne_data = pd.DataFrame(tsne_data, columns=["TSNE_X", "TSNE_Y"])
tsne_data["labels"] = cluster_labels

# COMMAND ----------

company_clusters = pd.concat([tsne_data, company_code_data], axis=1)
display(company_clusters)


# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS company_code_clusters (
# MAGIC   TSNE_X DECIMAL(38,18),
# MAGIC   TSNE_Y DECIMAL(38,18),
# MAGIC   labels LONG,
# MAGIC   CompanyCode STRING,
# MAGIC   PRIMARY KEY (CompanyCode)
# MAGIC )
# MAGIC

# COMMAND ----------

# Convert Pandas DataFrame to Spark DataFrame
company_clusters_spark = spark.createDataFrame(company_clusters)

# Use Spark DataFrame functions
company_clusters_spark = company_clusters_spark.withColumn("TSNE_X", col("TSNE_X").cast(DecimalType(38,18))).withColumn("TSNE_Y", col("TSNE_Y").cast(DecimalType(38,18)))

company_clusters_spark.write.format("delta") \
    .mode("overwrite") \
    .option("delta.enableChangeDataFeed", "true") \
    .option("delta.enableDeletionVectors", "false") \
    .saveAsTable("company_code_clusters")