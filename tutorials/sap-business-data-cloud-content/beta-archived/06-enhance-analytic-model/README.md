# Enhance an Analytic Model

## Persona 

Actors: <br/>
<img src="../resources/images/bdc_admin.png" alt="BDC Admin" width="100"/>
<img src="../resources/images/data_modeler.png" alt="Data Modeler" width="100"/>

Stakeholder: <br/>
<img src="../resources/images/business_analyst.png" alt="Business Analyst" width="105"/>

## Use Case
:warning: This exercise can be completed without Databricks as it uses sample mock data. Please note that it does not offer real ML insights into your data. This exercise will be updated once the ML functionality based on Data Product sharing is available, you can get a sneak preview [on the Databricks integration here](../beta-pipeline/05-enrich-data-products-with-databricks-ml/README.md).

When analyzing the Cash Flow, our business users want to better understand the company segmentation. The clustering algorithm is executed in Databricks and returns a cluster label for each company as well as the coordinates to visually interpret the company clusters.

We want to add the coordinates as visual representation to our report, therefore we need to add these as measures to our model.

To customize the delivered content through SAP Business Data Cloud as part of the Intelligent Application (in beta: lean intelligent application), the space content onboarded via SAP Business Data Cloud needs to be transformed from SAP managed content into editable content using the space copy option. The Data Builder entities are originally protected by the "sap." namespace, where the namespace of the copied entities will be removed and they'll become editable.

Afterwards, the user will enhance the views and Analytic Model with the output of the ML clustering algorithm.

## Overview
This exercise consists of the following sections:
- [Copy SAP-Managed Space](#copy-sap-managed-space)
- [Run Replication Flows](#run-replication-flows)
- [Prepare Mock Data](#prepare-mock-data)
- [Enhance Fact View](#enhance-fact-view) 
- [Enhance Analytic Model](#enhance-analytic-model) 

## Prerequisites
* SAP Datasphere User Permissions: 
    - DW Admin Role to copy space - Persona ***BDC Admin*** 
    - DW Modeler to modify entities in the Data Builder - Persona ***Data Modeler***

## Steps

> :books: If you are participating in a SAP BDC training, the space copy was already done for you (space name BDC_IA_CASHFLOW_AC_BDC_***USER-ID***). Read the following chapter and continue with [Run Replication Flows](#run-replication-flows). <br>

### Copy SAP-Managed Space

> <img src="../resources/images/bdc_admin.png" alt="BDC Admin" width="100"/>

1. Open the space created as part of the Intelligent Application (named ***BDC_IA_CASHFLOW***). If you are not sure of the space name, you can find it in the SAP Business Data Cloud Cockpit and jump directly to the space via the link.
<img src="./images/bdc_cockpit_space_name.png"  width="1000"/>

2. Select the ***...*** button in the menu of the space in order to duplicate a space.
<img src="./images/IA_SPACE_OVERVIEW.png"  width="1000"/>

3. Select ***Copy***.
<img src="./images/Space_copy_1.png"  width="1000"/>

4. By default, the space name of the copied space is the same of the copied name. "_COPY" is appended. Objects in a copied space are not deployed automatically by default.
<img src="./images/Space_copy_2.png"  width="1000"/>

5. Replace "_COPY" with "_EXT". Select the option ***Deploy objects***.
<img src="./images/Space_copy_3.png"  width="1000"/>

6. You are navigated to the copied space. After the space is successfully deployed, you receive a notification and the status changes to ***Deployed***.
<img src="./images/Space_copy_deployed.png"  width="1000"/>

7. No user assignment to the copied space is run during the copy process. Scroll down to the section ***Users***.
<img src="./images/Space_copy_user_assignment.png"  width="1000"/>

8. Select user who you want to add to the space.

9. All scoped roles to which the source space (the space which was copied) was assigned to also contain the newly copied space. Select the scoped role ***BDC_Scope_Space_Admin***. In the next step, select the according users (like your own to proceed with the exercise).
<img src="./images/Space_copy_scoped_role_editor.png"  width="1000"/>

10. Log out and log in again to refresh the scoped role applied to the user.

11. Open the data builder of the copied space. You can see that all entities are deployed as you selected the according option.
<img src="./images/Space_copy_data_builder.png"  width="1000"/>

12. In the app ***Connections***, you see that the connection to S/4HANA PCE (required to access the data products) is already available because of the copy.
<img src="./images/Space_copy_connection.png"  width="1000"/>

### Run Replication Flows 

> <img src="../resources/images/data_modeler.png" alt="Data Modeler" width="100"/>

> [!NOTE]
> In Beta, the Replication Flows need to be scheduled again after a space copy. For GA/after GA, it is planned to have an "ingestion space" to persist the once per source. The space copy feature will then only apply to Intelligent Application spaces serving the View-Entities which are referencing to the "ingestion space" tables & data. Therefore, there won't be the demand to re-run data replication or the need to schedule Replication Flows within the copied space. 

1. Two Replication Flows were created previously for the Intelligent Application to load the data of the data products.
<img src="./images/RF_overview.png"  width="1000"/>

2. Open the Replication Flow ***CompanyCode RepFlow***. It contains nine data products. The delta load interval is set to one hour. As the Replication Flow is already deployed (as selected in the space copy), the delta load interval can not be changed.
<img src="./images/RF_CompanyCode.png"  width="1000"/>

3. Open the Replication Flow ***CashFlow RepFlow***. It contains two data products.
<img src="./images/RF_CashFlow.png"  width="1000"/>

4. You can schedule the Replication Flows individually in the editor of each Replication Flow or in the Data Integration Monitor. The screenshot below displays how to start the run in the Data Integration Monitor. Start both Replication Flows individually.
<img src="./images/RF_DIM_StartRun.png"  width="1000"/>

5. You will receive a message that the run has started. 

6. Access the run details of a Replication Flow by selecting the arrow symbol (in this example for ***CashFlow ReplFlow***).

7. Here you can monitor the execution details of your Replication Flow. The left panel displays the runs of the flow, their corresponding messages are available in the right panel. Select the flow in the left panel to view its details. The metrics provide the record count for source and target tables used in the flow. You can select the according object (Data Product) above. In the screenshot, the initial run finished for both objects and it is now retrieving the delta.
<img src="./images/RF_cashflow_run.png"  width="1000"/>

8. If the status switches to ***Retrying***, the initial load finished. The delta load interval is configured by you in the Replication Flow before. If the status is ***retrying***, the delta load completed and it will retry. 
<img src="./images/RF_DIM_Result.png"  width="1000"/>

### Prepare Mock Data
This section is only necessary until the Databricks integration is available. Mock data will simulate the output of the Databricks clustering, it generates fake coordinates to allow a visualization later in SAC. There are two options how you can generate mock data explained below:

- [Reuse the existing CSV-File with Mock Data](#reuse-the-existing-csv-file-with-mock-data-manual-adjustments-to-make-sure) - manual adjustments might be required to make sure that the company codes fit to the company codes available in the customer data (otherwise the later modeled join will not work and there is no visualization) 
- [Generate Mock Data with SQL View](#enhance-fact-view) - makes sure that the join will work by generating mock data specific to the customer's transactional data in a SQL View

#### Reuse the existing CSV-File with Mock Data (manual adjustments to make sure)
1. Download the sample data set available in the [data folder](./data/company_clusters.csv).

2. In the data builder of the space copy, import the CSV-file downloaded before. Select that the first row is used as column header and that the CSV delimiter is auto-detected.
<img src="./images/import_local_table.png"  width="1000"/>

3. Define the column ***CompanyCode*** as key.
<img src="./images/table_setkey.png"  width="1000"/>

4. Click ***Deploy***.
<img src="./images/import_local_table_2.png"  width="1000"/>

5. Name the table ***Mock Data for Company Clusters*** (technical name ***MockDataCompanyClusters***) and confirm with clicking ***Deploy***.

6. Open the data editor for ***Mock Data for Company Clusters***.
<img src="./images/lt_data_preview.png"  width="1000"/>

7. You can add new records for the company codes available at the customer and sample coordinates by pressing the button ***Add***. 

8. Another option is to duplicate an existing record and to enter a new company code. 
<img src="./images/record_duplicate.png"  width="1000"/>

9. After adding and modifying the data records, save them by clicking the according button in the upper left corner.
<img src="./images/save_data_records.png"  width="1000"/>

#### Generate Mock Data with SQL View
In contrast to the later approach, a SQL View is used to generate the mock data. Later, the Databricks result will be consumed as a local table populated by the Replication Flow generated as part of the Data Product Installation.

1. In the Data Builder, create a new SQL View. 

2. Paste the following SQL Code:

```sql
SELECT CompanyCode,
	ROUND(Rand() * 100, 2) AS TSNE_X,
	ROUND(Rand() * 100, 2) AS TSNE_Y,
	FLOOR(Rand() * 20) + 1 AS label
FROM (
		SELECT DISTINCT CompanyCode
		FROM "Remote.S4H.CashFlow:v1.CashFlow"
	)
```
4. Validate the script and check that no issue is identified.
<img src="./images/validate_sql_view.png"  width="1000"/>

5. Run a data preview.
<img src="./images/sql_view_data_preview.png"  width="1000"/>

6. Set the following model properties for the view:
- ***Business Name*** View - Mock Data for Company Cluster
- ***Technical Name***: V_MockData_CompanyCluster

7. Save and deploy the view.

8. After the view is deployed, persist it once so that the records don't change:
<img src="./images/start_data_persistence.png"  width="1000"/>

9. Confirm that the persistency run completes by refreshing the data persistency status.
<img src="./images/data_persistency_status.png"  width="500"/>


### Enhance Fact View

> <img src="../resources/images/data_modeler.png" alt="Data Modeler" width="100"/>

1. :warning: To complete the exercise without Databricks, use the table or view with mock data created in the [section before](#prepare-mock-data). <br>
The local table ***Mock Data for Company Clusters*** was onboarded as part of the data product shared by Databricks. We want to add the details of the clusters like cluster label and coordinates to our Analytic Model for reporting. The coordinates ***TSNE_X*** and ***TSNE_Y*** will be visualized as a cluster in the SAP Analytics Cloud dashboard.

<img src="./images/local_table_dbx_company_clusters.png"  width="1000"/>

2. Open the view ***Cash Flow Actuals View***. 
<img src="./images/view_cash-flow-actuals-view.png"  width="1000"/>

3. Drag and drop the table ***Mock Data for Company Clusters*** from the left side into the modelling canvas. It is available because you onboarded it in the [previous step](./05-enrich-data-products-with-databricks-ml/README.md). Select the option *Join*. 
<img src="./images/join_company_clusters.png"  width="1000"/>

4. Select the ***Join*** node and configure the join:
- Join Type: ***Inner***
- Mappings: ***Company Code*** and ***Company Code***
<img src="./images/join_mapping.png"  width="1000"/>

5. Select the output view ***Cash Flow Actuals View*** (***Cash Flow Actuals View***). ***TSNE_X*** and ***TSNE_Y*** are listed as attributes. To define them as measures, select and drag & drop these two measures to the measures section.
<img src="./images/attribute_to_measure.png"  width="1000"/>

6. Save and deploy the view.

### Enhance Analytic Model

> <img src="../resources/images/data_modeler.png" alt="Data Modeler" width="100"/>

1. Open the Analytic Model ***Cash Flow Actuals Model***.
<img src="./images/am_overview.png"  width="1000"/>

2. Select the fact source. On the right side, you see that you can select the newly added measures ***TSNE_X*** and ***TSNE_Y***, select both.
<img src="./images/am_select_measures.png"  width="1000"/>

3. Now the Analytic Model contains five measures.
<img src="./images/am_overview_2.png"  width="1000"/>

4. Display details of the fact source measure ***TSNE_X***. Adjust the aggregation type to ***NONE*** since aggregating the cluster coordinates is not meaningful. Do the same for measure  ***TSNE_Y*** afterwards.
<img src="./images/aggregation_type.png"  width="1000"/>

5. Open the data preview for the Analytic Model. :warning: check for correct aggregation type
<img src="./images/am_preview.png"  width="1000"/>

6. This is an analytical preview which allows you to navigate through dimensions (if associations are available), and view the aggregated data. 

7. Select the measures ***TSNE_X*** and ***TSNE_Y*** as well as the dimension ***Company Code***. Confirm in the preview panel on the left side that the aggregation is applied correct (so the measures as not summed up but display the result of the Databricks clustering).
<img src="./images/data_preview.png"  width="1000"/>

8. Go back to the modelling environment.
<img src="./images/back_modelling.png"  width="1000"/>

9. Save and deploy the Analytic Model ***Cash_Flow_Actuals_Model***. 
<img src="./images/am_save_deploy.png"  width="1000"/>


## Next Steps
You created a new Analytic Model in the copied space based on the content delivered as part of the Intelligent Application. Now, the model is now available for the Business Analyst to be used in the report ([next exercise](/07-enhance-intelligent-applications/README.md)). 

This exercise focused on Company Clusters using mock data, you could redo the exercise in the future with the Data Product shared by Databricks. The additional exercise in which you are going to create an Analytic Model based on the forecasted cashflow ([via this link](./additional_use_case-cashflow_prediction.md)) can be skipped for now as this is also based on a Data Product shared by Databricks.

Continue with ([next exercise](/07-enhance-intelligent-applications/README.md)) to customize and enhance the dashboard.
