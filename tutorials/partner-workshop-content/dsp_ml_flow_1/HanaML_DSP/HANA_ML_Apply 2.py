from hana_ml import dataframe
from hana_ml.model_storage import ModelStorage
from hana_ml.algorithms.pal.auto_ml import Preprocessing
import mlflow
from constants import db_url, db_user, db_password
#db_url= "102b8ba6-b0cf-4508-b151-676381cfc4f9.hna0.prod-eu10.hanacloud.ondemand.com"
#db_user="SUVA#MLUSER"
#db_password="H!.R#Kdg)!!o8b!fD2=ulfui>!m$!f;b"
conn = dataframe.ConnectionContext(address=db_url,
                                   port=443,
                                   user=db_user,
                                   password=db_password)

# full_set, diabetes_train, diabetes_test, _ = DataSets.load_diabetes_data(conn)
dataset_data = conn.table('RETAILER_UNION_V', schema='SUVA')
# data preprocessing
dataset_data = Preprocessing(name="OneHotEncoder").fit_transform(data=dataset_data,features=["calendar_year","calendar_month","productsku", "retailer"])
dataset_data = dataset_data.auto_cast({"BIGINT": "INT", "DECIMAL": "DOUBLE"})
#dataset_data = dataset_data.drop("emp_var_rate")
# set up MLFlow
mlflow.set_tracking_uri("https://mlflow.cfapps.eu30.hana.ondemand.com")
model_storage = ModelStorage(connection_context=conn, schema='SUVA#MLUSER')
logged_model = 'runs:/4e9d0dd0c7ee4841b65e59842824d237/model'
mymodel = model_storage.load_mlflow_model(connection_context=conn, model_uri=logged_model)
dataset_data_predict = mymodel.predict(data=dataset_data, key="")
#dataset_data_predict.save(where="HanaML_DSP_Table_suva")
print(dataset_data_predict.collect())
