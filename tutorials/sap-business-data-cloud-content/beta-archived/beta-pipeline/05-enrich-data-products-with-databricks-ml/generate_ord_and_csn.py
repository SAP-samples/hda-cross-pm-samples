from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, length, max
from databricks.feature_engineering import FeatureEngineeringClient
from pyspark.sql.types import StringType
import mlflow
import json
import re
def ord_csn_generation(share_name: str, ord_title: str, ord_short_description: str, ord_description: str):
    """
    Generates the ORD and CSN schema files for the given table name.
    Generates the ORD and CSN schema files for the given table name.

    Parameters:
    table_name (str): The name of the table for which the schemas are generated.
    short_description (str): A short description of the data product.
    description (str): A detailed description of the data product.
    share_name (str): The name of the share associated with the data product.
    primary_key (list): A list of columns that form the primary key of the table.

    The function performs the following steps:
    1. Retrieves the dataset and schema descriptions from the specified table.
    2. Constructs the ORD schema using the provided descriptions.
    3. Saves the ORD schema to a JSON file.
    4. Maps Spark data types to CSN data types.
    5. Constructs the CSN schema using the mapped data types and primary key information.
    6. Saves the CSN schema to a JSON file.
    """
    mlflow.set_registry_uri("databricks")
    fe = FeatureEngineeringClient()

    ord_schema = {
        "title": ord_title,
        "shortDescription": ord_short_description,
        "description": ord_description
    }
    with open(f"ord_{share_name}.json", "w") as file:
        file.write(json.dumps(ord_schema))
    
    spark = SparkSession.builder.appName("ORD_CSN_Generation").getOrCreate()
    delta_share_sql = f"SHOW ALL IN SHARE {share_name}"
    delta_share_information = spark.sql(delta_share_sql)
    delta_share_information = delta_share_information.toPandas().to_dict("records")

    user_id = spark.sql("select current_user() AS user")
    creator_name = user_id.toPandas()["user"][0]

    spark_csn_mapping = {
        "boolean": "cds.Boolean",
        "string": "cds.String",
        "int": "cds.Integer",
        "double": "cds.Double",
        "float": "hana.REAL",
        "bigint": "cds.Integer64",
        "decimal": "cds.Decimal",
        "date": "cds.Date",
        "timestamp": "cds.DateTime",
        "timestamp_ms": "cds.Timestamp"
    }
    context_name = delta_share_information[0]["name"].split(".")[0]
    csn_schema = {
        "csnInteropEffective": "1.0",
        "$schema": "2.0",
        "definitions": {
            context_name: {
                "kind": "context"
            }
        },
        "i18n": {},
        "meta": {
            "creator": creator_name,
            "flavor": "inferred",
            "share_name": share_name
        }
    }

    for table_asset in delta_share_information:
        share_table_name = table_asset["name"]
        csn_schema["definitions"][share_table_name] = {"kind": "entity"}
        
        table_name = table_asset["shared_object"]
        primary_keys = fe.get_table(name=table_name).primary_keys
        
        schema_sql = f"DESCRIBE TABLE {table_name}"
        schema_description = spark.sql(schema_sql)
        
        schema_description = schema_description.toPandas()
        schema_list = schema_description.values.tolist()
        column_mapping = {}
        for column_name, data_type, comment in schema_list:
            if "decimal"in data_type:
                schema_key = data_type.split("(")[0]
                precision, scale = re.findall(r"\d+", data_type)
                base_dtype = spark_csn_mapping[schema_key]
                column_mapping[column_name] = {"type": base_dtype, "precision": int(precision), "scale": int(scale)}

            elif "string" in data_type:
                schema_key = "string"
                base_dtype = spark_csn_mapping[schema_key]
                column_mapping[column_name] = {"type": base_dtype, "length": 5000}
            else:
                csn_dtype = spark_csn_mapping[data_type]
                column_mapping[column_name] = {"type": csn_dtype}
            if column_name in primary_keys:
                column_mapping[column_name]["key"] = True
        
        csn_schema["definitions"][share_table_name]["elements"] = column_mapping
        
    
    with open(f"csn_{share_name}.json", "w") as file:
        file.write(json.dumps(csn_schema))
    
    print("Generated ORD and CSN file for delta share")