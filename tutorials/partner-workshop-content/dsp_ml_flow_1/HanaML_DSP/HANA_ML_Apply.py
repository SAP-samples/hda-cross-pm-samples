from hana_ml import dataframe
from hana_ml.model_storage import ModelStorage
from hana_ml.algorithms.pal.auto_ml import Preprocessing
import mlflow
from constants import db_url, db_user, db_password, db_space, mlflow_url

conn = dataframe.ConnectionContext(address=db_url,
                                   port=443,
                                   user=db_user,
                                   password=db_password)

data = conn.table('Customer_Profile_View', schema=db_space)
# Create data transformation casting data types
data = data.auto_cast({"BIGINT": "INT", "DECIMAL": "DOUBLE"})
# set up MLFlow
mlflow.set_tracking_uri(mlflow_url)
# define model storage and retrieve model from MLflow run
model_storage = ModelStorage(connection_context=conn)
logged_model = 'runs:/d0685a34831c4efcaa70c71da6bdddd5/model'
mymodel = model_storage.load_mlflow_model(connection_context=conn, model_uri=logged_model)
dataset_data_predict = mymodel.predict(data=data, key="Customer_Id")
dataset_data_predict.save(where=("ML_SPACE#DBUSER", "HANA_ML_Prediction"), force=True)
print(dataset_data_predict.collect())
