from dotenv import load_dotenv
import os

load_dotenv('.secret')

db_url = os.getenv("DB_URL")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_space = os.getenv("DB_SPACE")
db_table = "Sales_Order_SQL_View"
mlflow_url = "https://mlflow.cfapps.eu30.hana.ondemand.com"