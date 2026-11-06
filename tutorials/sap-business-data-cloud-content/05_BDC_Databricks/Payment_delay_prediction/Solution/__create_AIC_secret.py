# Databricks notebook source
# MAGIC %md
# MAGIC ## define AI Core service parameters
# MAGIC
# MAGIC We use parameters from 
# MAGIC - service key: `aicore-in-dxb`
# MAGIC - serice instance `ai-core` (id: f95bb29b-96c7-4030-a759-e4ff301e3913)
# MAGIC - subaccount `ai-core-bdc-poc` (id: bcc94c54-9f91-467f-ab18-bc45087e7024)
# MAGIC - global account `AI Core Potsdam`
# MAGIC

# COMMAND ----------

from databricks.sdk import WorkspaceClient
from typing import Dict
import getpass

def put_credentials(scope_name: str, key_value_pairs: Dict = None):
    w = WorkspaceClient()
    
    try:
        w.secrets.create_scope(scope_name)
        print(f"Scope {scope_name} is now created")
    except Exception as e:
        print(f"Scope {scope_name} already exists")

    if key_value_pairs != None:
        for key in key_value_pairs.keys():
            value = key_value_pairs[key]
            if isinstance(value, str):
                print(f"value for '{key}': {value}")
                w.secrets.put_secret(scope_name, key, string_value = value)
            elif value == None:
                value = getpass.getpass(f"Please provide the value for '{key}': ")
                w.secrets.put_secret(scope_name, key, string_value = value)
            else:
                print("Unhandled value type")
    else:
        continue_adding = True
        print(f"You will iteratively add credentials under scope {scope_name}. Type 'break' to stop")
        while continue_adding:
            key = input("Please provide the key for the credential: ")
            value = input("Please provide the value for the credential: ")
            if key == "break":
                continue_adding = False
            elif value == "break":
                continue_adding = False
            else:
                w.secrets.put_secret(scope_name, key, string_value = value)

    print("Credentials successfully stored")

# COMMAND ----------

scope_name = "aicore_service_params"

key_value_pairs = {"AICORE_CLIENT_ID": "sb-f95bb29b-96c7-4030-a759-e4ff301e3913!b945203|xsuaa_std!b318061",
             "AICORE_CLIENT_SECRET": None,
             "AICORE_AUTH_URL": "https://aicore-bdc-poc-jpy6ytc0.authentication.eu12.hana.ondemand.com",
             "AICORE_BASE_URL": "https://api.ai.intprod-eu12.eu-central-1.aws.ml.hana.ondemand.com/v2",
             "AICORE_RESOURCE_GROUP": "default"
             }

put_credentials(scope_name, key_value_pairs)

# COMMAND ----------

# use secrets
# doc: https://docs.databricks.com/aws/en/security/secrets/example-secret-workflow 
# read value - we cannot print (https://docs.databricks.com/aws/en/security/secrets/#redaction)

AICORE_CLIENT_ID = dbutils.secrets.get(scope = scope_name, key = "AICORE_CLIENT_ID")
print(AICORE_CLIENT_ID)


# COMMAND ----------

# MAGIC %md
# MAGIC # validate that integration is working

# COMMAND ----------

# MAGIC %pip install "sap-ai-sdk-gen[all]"
# MAGIC %restart_python

# COMMAND ----------

from databricks.sdk import WorkspaceClient
import os
w = WorkspaceClient()
for key in ["AICORE_CLIENT_ID", "AICORE_CLIENT_SECRET", "AICORE_AUTH_URL", "AICORE_BASE_URL", "AICORE_RESOURCE_GROUP"]:
    os.environ[key] = w.dbutils.secrets.get(scope = "aicore_service_params", key=key)

# COMMAND ----------


from gen_ai_hub.orchestration.models.llm import LLM
from gen_ai_hub.orchestration.models.message import SystemMessage, UserMessage
from gen_ai_hub.orchestration.models.template import Template, TemplateValue
from gen_ai_hub.orchestration.models.config import OrchestrationConfig 
from gen_ai_hub.orchestration.service import OrchestrationService 

llm=LLM(name="gpt-4o-mini")
template = Template(messages=[UserMessage("{{?prompt}}")])


orchestration_config = OrchestrationConfig(
    llm=llm,
    template=template,
)

orchestration_service = OrchestrationService(config = orchestration_config)

result = orchestration_service.run(template_values=[
    TemplateValue(name="prompt", value="Who are you?")
])
print(result.orchestration_result.choices[0].message.content)
