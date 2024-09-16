from hana_ml import dataframe
from hana_ml.algorithms.pal.unified_classification import UnifiedClassification
import mlflow
from bayes_opt import BayesianOptimization
from constants import db_url, db_user, db_password, db_space, mlflow_url
# suppress warnings coming from pandas
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def hgt_training_routine(n_estimators:float, max_depth:float, subsample: float, col_subsample_tree: float, col_subsample: float, learning_rate: float) -> float:
    """Trains a Hybrid Gradient Boosting Tree classifier and returns the MCC (Matthews Correlation Coefficient) score.

    Args:
        n_estimators (float): The number of boosting stages to be run.
        max_depth (float): The maximum depth of the individual estimators.
        subsample (float): The fraction of samples to be used for fitting the individual base learners.
        col_subsample_tree (float): The fraction of features to be used for each tree.
        col_subsample (float): The fraction of features to be used for each split.
        learning_rate (float): The learning rate shrinks the contribution of each tree by `learning_rate`.

    Returns:
        float: The MCC score of the trained model.
    """
    with mlflow.start_run():
        # Set parameters for the Hybrid Gradient Boosting Tree model
        hgt_params = {
            "n_estimators": int(n_estimators),
            "max_depth": int(max_depth),
            "subsample": subsample,
            "col_subsample_tree": col_subsample_tree,
            "col_subsample_split": col_subsample,
            "learning_rate": learning_rate,
            "random_state": 42,
            "evaluation_metric": "auc"
        }
        # Initialize the classification model with specified parameters
        hgt_classification = UnifiedClassification(func="HybridGradientBoostingTree", **hgt_params)
        hgt_classification.enable_mlflow_autologging()
        # Fit the model with the data, specifying all parameters
        hgt_classification.fit(data,key="Customer_Id", label="Has_Responded", partition_method="stratified", stratified_column="Has_Responded", build_report=True, partition_random_state=42, training_percent=0.8)
        # Collect model statistics and extract the MCC metric
        statistic_dataset = hgt_classification.statistics_.collect()
        mcc_metric = statistic_dataset[statistic_dataset["STAT_NAME"] == "MCC"]["STAT_VALUE"].values.tolist()[0]
        mcc_score = float(mcc_metric)
    return mcc_score

def mlp_training_routine(max_iter: float, learning_rate: float, momentum: float, batch_size: float, hidden_layer_size: float) -> float:
    """Trains a Multi-Layer Perceptron (MLP) classifier and retrieves the MCC (Matthews Correlation Coefficient) score from the model statistics.

    Args:
        max_iter (float): The maximum number of iterations.
        learning_rate (float): The learning rate for weight updates.
        momentum (float): The momentum for gradient descent updates.
        batch_size (float): The number of samples per batch.
        hidden_layer_size (float): The size of the hidden layer.

    Returns:
        float: The MCC score of the trained model.
    """
    with mlflow.start_run():
        # Set parameters for the MLP model
        mlp_params = {
            "max_iter": int(max_iter),
            "learning_rate": learning_rate,
            "momentum": momentum,
            "batch_size": int(batch_size),
            "hidden_layer_size": (int(hidden_layer_size),),
            "random_state": 42,
            "evaluation_metric": "auc_onevsrest",
            "activation": "sigmoid_asymmetric",
            "output_activation": "sigmoid_asymmetric",
            "normalization": "z-transform",
            "weight_init":'uniform'
        }
        # Initialize the classification model with specified parameters
        mlp_classification = UnifiedClassification(func="MLP", **mlp_params)
        mlp_classification.enable_mlflow_autologging()
        # Fit the model with the data, specifying all parameters
        mlp_classification.fit(data,key="Customer_Id", label="Has_Responded", partition_method="stratified", stratified_column="Has_Responded", build_report=True, partition_random_state=42, training_percent=0.8)
        # Collect model statistics and extract the MCC metric
        statistic_dataset = mlp_classification.statistics_.collect()
        mcc_metric = statistic_dataset[statistic_dataset["STAT_NAME"] == "MCC"]["STAT_VALUE"].values.tolist()[0]
        mcc_score = float(mcc_metric)
    return mcc_score

# build up connection to HANA database
conn = dataframe.ConnectionContext(address=db_url,
                                   port=443,
                                   user=db_user,
                                   password=db_password)

data = conn.table('Customer_Profile_View', schema=db_space)
# Create data transformation casting data types
data = data.auto_cast({"BIGINT": "INT"})
# define search space for hyperparameter tuning of the HGT model itself
hgt_optimizer = BayesianOptimization(f=hgt_training_routine,
                                     pbounds={
                                         "n_estimators": (50, 1000),
                                         "max_depth": (0, 50),
                                         "subsample": (0.01, 1.0),
                                         "col_subsample_tree": (0.01, 1.0),
                                         "col_subsample": (0.01, 1.0),
                                         "learning_rate": (0.01, 1.0)
                                         },
                                         verbose=2)

# set up MLflow tracking with experiment
mlflow.set_tracking_uri(mlflow_url)
mlflow.set_experiment("HANA ML DSP Experiment")
# define run of the model using 10 random selections and 30 iterations using a bayesian search optimization through the hyperparamter search space
hgt_optimizer.maximize(
    init_points=10,
    n_iter=30
)
# # print out optimal hyper parameter combination with respective score
print(f"""
The best score for the model is {hgt_optimizer.max['target']} with the parameter combinations of {hgt_optimizer.max['params']}
""")

mlp_optimizer = BayesianOptimization(f=mlp_training_routine,
                                     pbounds={
                                         "max_iter": (1, 10000),
                                         "learning_rate": (0.00001, 1.0),
                                         "momentum": (0.00001, 1.0),
                                         "batch_size": (1, 50),
                                         "hidden_layer_size": (1, 300)
                                         },
                                         verbose=2)
# define run of the model using 10 random selections and 30 iterations using a bayesian search optimization through the hyperparamter search space
mlp_optimizer.maximize(
    init_points=10,
    n_iter=30
)
# print out optimal hyper parameter combination with respective score
print(f"""
The best score for the model is {mlp_optimizer.max['target']} with the parameter combinations of {mlp_optimizer.max['params']}
""")