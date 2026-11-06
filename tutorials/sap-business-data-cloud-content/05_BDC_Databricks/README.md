
# Operationalizing AI with SAP Databricks in SAP Business Data Cloud

## Description

## Requirements
Following pre-requisites should have been already prepared by the system administrator:
- Unity Catalog with 2 predefined catalogs with read and write access for all users:
    - `uc_cash_liquidity_forecast`
    - `uc_delayed_payments`
- The following SAP Data Products are shared and accessible by all users:
    - `Cashflow` 
    - `Entry View Journal Entry` 
- Appropriate permissions for all users to create schema within the above mentioned catalogs
- Access to a configured SAP AI Core Service intance with corresponding service key
    - https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/initial-setup
- Access to required Python packages
    - `sap-bdc-connect-sdk` 
    - `sap-ai-sdk-gen` 
- Configured SECRET SCOPE
    - This step has already been done by the administrator to facilitate the sharing process. However, if you need to do it on you own you can follow the steps described here to create a secret scope: To create a secret scope you can either use the following URL `https://<databricks-instance>#secrets/createScope`. Replace `<databricks-instance>` with the workspace URL of your Databricks deployment.
    - Alternatively, you can run the following command in the terminal by clicking on the terminal icon on the lower right corner: `databricks secrets create-scope sap-bdc-connect-sdk`. 
    - The secret scope only has to be created once and can be made accessible to all workspace users by either toggling `manage principal` to `all workspace users` or via the terminal using the following command `databricks secrets put-acl sap-bdc-connect-sdk users READ`. To check whether the assignment worked, you can then use the command `databricks secrets list-acls sap-bdc-connect-sdk`.
    - A full explanation can be found here https://docs.databricks.com/aws/en/security/secrets/example-secret-workflow     




## Exercises
- ### Use Case 1: Cashflow Forecast
    - **Scenario**:
        The data scientist wants to forecast the cashflow for the upcoming 6 months and make the result available for reporting. For that he needs to access the cashflow data product from S/4HANA, apply ML/AI model training and forecasting, and share / install the enriched data product in BDC Cockpit and Datasphere. 

    - **Key Learnings**:
        - Sharing Data Product to SAP Databricks
        - Enrich Data Product with ML/AI Insights, e.g. 
            -  Data understanding and preparation
            -  Train time series forecast model 
            -  Apply cashflow forecast
        - MLFlow for monitoring query performance 
        - Re-sharing custom Data Product to BDC Data Catalog with `sap-bdc-connect-sdk`
    - **Exercises**:
        - [01_Data Understanding.ipynb](./Cashflow_prediction/Exercise/01_Data_Understanding.ipynb)
        - [02_Cash_Liquidity_Data_Preparation.ipynb](./Cashflow_prediction/Exercise/02_Cash_Liquidity_Data_Preparation.ipynb)
        - [03_Cash_Liquidity_Training.ipynb](./Cashflow_prediction/Exercise/03_Cash_Liquidity_Training.ipynb)
        - [04_Cash_Liqudity_Forecast.ipynb](./Cashflow_prediction/Exercise/04_Cash_Liqudity_Forecast.ipynb)
        - [05_Publish_Data_Product.ipynb](./Cashflow_prediction/Exercise/05_Publish_Data_Product.ipynb)
    - **Solution**
        - [00_Share_Cashflow_Data_Product.md](./Cashflow_prediction/Solution/00_Share_Cashflow_Data_Product.md)
        - [01_Data Understanding.ipynb](./Cashflow_prediction/Solution/01_Data_Understanding.ipynb)
        - [02_Cash_Liquidity_Data_Preparation.ipynb](./Cashflow_prediction/Solution/02_Cash_Liquidity_Data_Preparation.ipynb)
        - [03_Cash_Liquidity_Training.ipynb](./Cashflow_prediction/Solution/03_Cash_Liquidity_Training.ipynb)
        - [04_Cash_Liqudity_Forecast.ipynb](./Cashflow_prediction/Solution/04_Cash_Liqudity_Forecast.ipynb)
        - [05_Publish_Data_Product.ipynb](./Cashflow_prediction/Solution/05_Publish_Data_Product.ipynb)

- ### Use Case 2: Payment Delay Prediction
    - **Scenario**:
        The data scientist needs to predict payment delays and run a root cause analysis. He has to provide the key drivers for the delays and an explanation in a human readable manner. For that he combines SAP Databricks and AI Foundation LLM capabilities to derive the insights. These insights will help the Financial Controller to better understand the payment delays problem and to derive the corresponding actions to mitigate.

    - **Key Learnings**:
        - Advanced ML/AI capabilities
            - Determine key drivers for payment delay via SHAP Values
            - Visualizing SHAP Values
            - Hyperparameter optimization with xgboost
        - Integrating SAP AI Core Service for LLM modelling
            - Configure SAP AI Core `orchestration services`
        - Implementing MLFlow custom model with PyFunc for monitoring and logging
    - **Exercises**:
        - [01_Payment_Delay_Data_Preparation.ipynb](./Payment_delay_prediction/Exercise/01_Payment_Delay_Data_Preparation.ipynb)
        - [02_Payment_Delay_Training.ipynb](./Payment_delay_prediction/Exercise/02_Payment_Delay_Training.ipynb)
        - [03_Payment_Delay_Inference.ipynb](./Payment_delay_prediction/Exercise/03_Payment_Delay_Inference.ipynb)
        - [04_Payment_Delay_Explain.ipynb](./Payment_delay_prediction/Exercise/04_Payment_Delay_Explain.ipynb)
        - [05_Publish_Data_Product.ipynb](./Payment_delay_prediction/Exercise/05_Publish_Data_Product.ipynb)
    - **Solution**
        - [00_Share_Entry_Journal_Entry_View_Data_Product.md](./Payment_delay_prediction/Solution/00_Share_Entry_Journal_Entry_View_Data_Product.md)
        - [01_Payment_Delay_Data_Preparation.ipynb](./Payment_delay_prediction/Solution/01_Payment_Delay_Data_Preparation.ipynb)
        - [02_Payment_Delay_Training.ipynb](./Payment_delay_prediction/Solution/02_Payment_Delay_Training.ipynb)
        - [03_Payment_Delay_Inference.ipynb](./Payment_delay_prediction/Solution/03_Payment_Delay_Inference.ipynb)
        - [04_Payment_Delay_Explain.ipynb](./Payment_delay_prediction/Solution/04_Payment_Delay_Explain.ipynb)
        - [05_Publish_Data_Product.ipynb](./Payment_delay_prediction/Solution/05_Publish_Data_Product.ipynb)

