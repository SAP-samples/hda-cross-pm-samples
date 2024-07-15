from hana_ml import dataframe
from hana_ml.algorithms.pal.unified_regression import UnifiedRegression
import mlflow
from hana_ml.algorithms.pal.auto_ml import Preprocessing
from constants import db_url, db_user, db_password
#db_url= "102b8ba6-b0cf-4508-b151-676381cfc4f9.hna0.prod-eu10.hanacloud.ondemand.com"
#db_user="SUVA#MLUSER"
#db_password="H!.R#Kdg)!!o8b!fD2=ulfui>!m$!f;b"
# dataset retrieval
conn = dataframe.ConnectionContext(address=db_url,
                                   port=443,
                                   user=db_user,
                                   password=db_password)

dataset_data = conn.table('RETAILER_UNION_V', schema='SUVA')
# data preprocessing
dataset_data = Preprocessing(name="OneHotEncoder").fit_transform(data=dataset_data,features=["calendar_year","calendar_month","productsku", "retailer"])
dataset_data = dataset_data.auto_cast({"BIGINT": "INT", "DECIMAL": "DOUBLE"})
#dataset_data = dataset_data.drop("emp_var_rate")
# set up MLFlow
mlflow.set_tracking_uri("https://mlflow.cfapps.eu30.hana.ondemand.com")
mlflow.set_experiment("HanaML_DSP Experiment_suva1")
# set up classification
hgt_params = {
    "n_estimators": 100,
    "random_state": 43,
    "evaluation_metric": "rmse"
}
uc = UnifiedRegression(func="HybridGradientBoostingTree", **hgt_params)
uc.enable_mlflow_autologging(schema="SUVA#MLUSER")
# train data
uc.fit(dataset_data, label="sales")