# Databricks notebook source
# MAGIC %pip install "sap-ai-sdk-gen[all]"
# MAGIC %restart_python

# COMMAND ----------

from ai_core_sdk.ai_core_v2_client import AICoreV2Client
from databricks.sdk import WorkspaceClient
import os
w = WorkspaceClient()
for key in ["AICORE_CLIENT_ID", "AICORE_CLIENT_SECRET", "AICORE_AUTH_URL", "AICORE_BASE_URL", "AICORE_RESOURCE_GROUP"]:
    os.environ[key] = w.dbutils.secrets.get(scope = "aicore_service_params", key=key)

# COMMAND ----------

# Databricks notebook source
# MAGIC %pip install "sap-ai-sdk-gen[all]"
# MAGIC %restart_python

# COMMAND ----------

from ai_core_sdk.ai_core_v2_client import AICoreV2Client
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
from ai_core_sdk.ai_core_v2_client import AICoreV2Client

llm=LLM(name="gpt-4o-mini")
template = Template(messages=[UserMessage("{{?prompt}}")])


orchestration_config = OrchestrationConfig(
    llm=llm,
    template=template,
)

orchestration_service = OrchestrationService(config = orchestration_config)

result = orchestration_service.run(template_values=[
    TemplateValue(name="prompt", value=
                  '''
                  can you create a jira from: 
                  We feel that our polling of 5 minutes is fast enough that customers should not be impacted between publishing in one system and then logging into a second system to start consumption.  Normally a delay of over 5 minutes that can extend to hours or days is due to communication issues between dbx and ucl that cause the data product to no be published to ucl and not visible to catalog to extract.  Or none errors with ucl that ignore aggregation or fail in that process of extracting the ord from source system and fail the update process.  We have asked for events to be enabled on ucl for us to not have to do active polling on our side, but that is only a partial fix that would save a few minutes and reduce load.

 
                  '''
                  )
])
print(result.orchestration_result.choices[0].message.content)

# COMMAND ----------


