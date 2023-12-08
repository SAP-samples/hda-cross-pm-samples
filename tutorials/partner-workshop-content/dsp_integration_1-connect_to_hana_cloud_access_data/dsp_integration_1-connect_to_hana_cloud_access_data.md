# Access, Load and Transform Data from HANA Cloud
 
 HANA Cloud is a multi-model database management system that stores high volume business data. For the business need to consume this data in SAP Datasphere, SAP Datasphere allows to add HANA Cloud connection in order to consume the data meaningfully.

## Prerequisites
You need to have:

- a space and service account user added to that space in SAP Datasphere
- user and password to access an SAP HANA Cloud / SAP HANA Cloud Trial instance

## You will learn
  - How to connect to HANA Cloud instance from SAP Datasphere
  - How to access the HANA Cloud data
  - How to build replication flows and transformation flows on HANA cloud data
  
### Use Case and Exercise Break-up

Please note that the survey data is a <b>fictional example</b>.
The company <b>Best Run Bikes</b> has office loctions in different countries. Employee statisfaction and Work-life balance are very important topics for this organization. To ensure this, the company employs a monthly employee survey to stay informed about the changing employee attitudes. The survey data is then visualized to make relevant changes in the company.
In this exercie, we want to identify these trends as quickly as possible and derive actions based on the analysis of these surveys. 

The survey is run using an own developed application. The results are stored in a table in a standalone HANA Cloud system. To gurantee the anonymity of each employee, only the office code is part of a survey record. Our goal is to map the survey results to the locations of our company to analyze the results in SAP Analytics Cloud.

This exercise is divided into three main parts. They are:
1. Connect to HANA Cloud
3. Create a replication flow to access data from a table and enable it for delta load
4. Create a transformation flow to categorize repititive data

In the next sections, we will look at the step-by-step process for each of these parts.

If you are interested in learning how to set up a HANA cloud instance and upload data to a table, please refer to this [tutorial](./others-dsp_integration_1-connect_to_hana_cloud_access_data/dsp_integration_1.1-connect_to_hana_cloud.md). If you already have the details and the credentials of the HANA Cloud instance, we can begin with adding it as a connection.

### Connect to HANA Cloud
The HANA Cloud instance has already been created on the BTP account. It needs to be added to the Datasphere space. Please note that this can be done in each space only once

1. Select **Connections** from the main menu.

    ![Select Connections Tab](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Connection_tab.png)

2. Select Create option from Menu.

    ![Create Connection](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Create_Connection.png)

3. Search for the 'SAP HANA' option and select it as the connection type.

    ![Select SAP HANA Connection](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Connection_HANA.png)

4. Add the connection details and credentials and continue to the next step.

    ![Add HC Credentials](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Create_connection1.png)

5. Add the technical and business names for the connection. If you create connections to different  HANA Cloud tenants, add your user ID. Click on **Create Connection**.

    ![Add HC Credentials](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Create_connection2.png)

6. Validate the new created connection. Check that **Replication Flows** are enabled. To configure **Remote Tables**, a certifacte would need to be updated to DSP. As we focus on Replication Flows in this exercise, it's not required. 

      ![Validate Connection](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Validate_Connection.png)

### Create a replication flow
Now that the HANA Cloud connection has been established, we can start replicating the data. For this use case, we need a replication flow. A replication flow is used to copy multiple data assets from the same source to the same target in a fast and easy way. Hence, it does not require complex projections.
We will create a replication flow to fetch the latest data from a HANA Cloud instance. When the replication flow runs for the first time, all the data is fetched and on subsequent runs, the delta data will be fetched. 

Here are the steps to create a replication flow:

1. In the Data Builder Section, use the **New Replication Flow** option to start creating it.

    ![Create Replication Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Create_Replication_Flow.png)

2. Add the Source object information. The HANA Cloud instance connection is the Source Connection. i.e. <b>HANA_CLOUD(HANA)</b> is the connection that we created previously.
The schema of the database will be added as the Source Container. i.e. <b>APP_SURVEY</b> is the schema in the HANA Cloud instance which will be added.

    ![Add Source Information](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Add_Source_RF1_1.png)

3. Add the source object from the source system. The table **SURVEY_RESULTS_<USER_ID>** contains the survey data. Please add the table which ends with your user id as the source table.

    ![Add Source Object](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Add_target_container_1.png)

4. Select SAP Datasphere as Target Connection since we are extracting the data to Datasphere. The section **Target Objects** is automatically being filled with the same name as the data source data set name. The replication flow can either us an already pre-created data set in the target (e.g. a pre-created target table) or you can let the Replication Flow create the target data set in case it is not yet existing. In this case, the Replication Flow will create the target table, rename it to **T_SURVEY_RESULTS_<USER_ID>**. 

    ![Add Target Container](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Add_Target.png)

5. For each selected source data set, there are two ways to configure each replication.
The first possibility is using "Projections" and "Settings" in the middle of your replication flow.  Change the Load Type to **Intial and Delta**. Also, turn on the **Truncate** option.
With this load type, the first time you run the transformation flow, the system will load the full set of data to the target table. For subsequent runs, the system will only load changes (inserts, updates, deletes) to the target table.

    ![Add Target Container](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_RF_Settings.png)

6. You can set additional configurations when selecting your replication object. On the right side, check that **Delta Capture** is set to **ON**. 

    ![Check Delta Enabled](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_RF_Target_Delta.png)

7. Then, name the Replication Flow **RF_Populate_Survey_Results_<USER_ID>**. Then Save and Deploy. You will be notified when the deployment is successful.

    ![Save Replication Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_RF_Name.png)

8. You can run the Replication Flow using the Run button. The progress of the run can be viewed in the **Data Integration Monitor**.

    ![Run Replication Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_RF_Run.png)

9. Wait until the replication run successfully, which means the initial load is done. Afterwards, the replication flow is in delta load stage to receive updates from the source system. Once the initial load is done the status of the replication object switchs to `Retrying` which means it will check every 1h for new change data to arrive. You can check the number of `Initial Load Operations` to see the number of transferred records.

    ![Run Replication Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_RF_DIM.png)


10. If the initial load was successful, the data written into the local table can be viewed in the Data Builder. The target table is called **T_SURVEY_RESULTS_<USER_ID>**. The Data Viewer button can be used to view the data.

    ![Data Viewer Replication Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_View_Data_RF.png)

### Create a transformation flow
 
Now, we need a transformation flow. Tranformation flows load data from one or more source tables, apply transformations on it (such as a join), and output the result in a target table. You can load a full set of data from one or more source tables to a target table. You can also load delta changes from one source table to a target table.
A transformation flow run is a one-time event that completes when the relevant data is loaded to the target table successfully. You can run a transformation flow multiple times, for example if you are loading delta changes to the target table.

For this use case, we will use the transformation flow to create categories for the repititive survey questions. We will create a calculated column which will generate an umbrella category for the questions. The questions can be categorized as follows:

<table>
  <tr>
    <th>Statement</th>
    <th>Category</th>
  </tr>
  <tr>
    <td>I have a really interesting  job.</td>
    <td>Job Satisfaction (Positive)</td>
  </tr>
  <tr>
    <td>Most of the time I enjoy going to work.</td>
    <td>Job Satisfaction (Positive)</td>
  </tr>
  <tr>
    <td>I'm often bored at work.</td>
    <td>Job Satisfaction (Negative)</td>
  </tr>
  <tr>
    <td>If I could, I would like to change careers.</td>
    <td>Job Satisfaction (Negative)</td>
  </tr>
  <tr>
    <td>I'm satisified with the relations between colleagues in my team.</td>
    <td>Positive Working Atmosphere</td>
  </tr>
  <tr>
    <td>I can always trust the colleagues in my team.</td>
    <td>Positive Working Atmosphere</td>
  </tr>
  <tr>
    <td>It would not bother me if some colleagues of my team would be replaced.</td>
    <td>Negative Working Atmosphere</td>
  </tr>
  <tr>
    <td>It's sometimes difficult to remain a good relation to all colleagues.</td>
    <td>Negative Working Atmosphere</td>
  </tr>
   <tr>
    <td>After work, I'm exhausted in the evening.</td>
    <td>Workload (Negative)</td>
  </tr>
  <tr>
    <td>I'm often working under time pressure.</td>
    <td>Workload (Negative)</td>
  </tr>
</table>

Here are the steps:
1. In the Data Builder Tab, select the option **New Tranformation Flow** to start creating a transformation flow.

    ![New Tranformation Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Start_TF.png)

2. Use the Edit Button on the object **View Transform** to start editing.

    ![New Tranformation Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Edit_TF.png)

3. From the Repository, search for the local table **T_SURVEY_RESULTS_<USER_ID>**. Drag and drop the table on the View Tranform Editor. Then, use the calculated column option on the object, to start creating a calculated column.

    ![View Tranformation Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_View_TF.png)

4. Name the operation **Calculate_category** and proceed to add a calculated column.

    ![Add Calculated Column](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Calculated_Column.png)

5. Name the calculated column **CATEGORY** and add the semantic type for the column. 

    ![Add Calculated Column2](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Add_Calculated_Column.png)

6. Then proceed to add the logic for the calculation as follows and validate the expression.

```
CASE
WHEN STATEMENT = 'I have a really interesting  job.' THEN 'Job Satisfaction (Positive)' 
WHEN STATEMENT = 'Most of the time I enjoy going to work.' THEN 'Job Satisfaction (Positive)' 
WHEN STATEMENT = 'I''m often bored at work.' THEN 'Job Satisfaction (Negative)' 
WHEN STATEMENT = 'If I could, I would like to change careers.' THEN 'Job Satisfaction (Negative)' 
WHEN STATEMENT = 'I''m satisified with the relations between colleagues in my team.' THEN 'Positive Working Atmosphere' 
WHEN STATEMENT = 'I can always trust the colleagues in my team.' THEN 'Positive Working Atmosphere' 
WHEN STATEMENT = 'It would not bother me if some colleagues of my team would be replaced.' THEN 'Negative Working Atmosphere' 
WHEN STATEMENT = 'It''s sometimes difficult to remain a good relation to all colleagues.' THEN 'Negative Working Atmosphere' 
WHEN STATEMENT = 'After work, I''m exhausted in the evening.' THEN 'Workload (Negative)' 
WHEN STATEMENT = 'I''m often working under time pressure.' THEN 'Workload (Negative)' 
ELSE 'Not Available'
END
```

7. Go back to the main view of the Tranformation flow and add a new local table as the target table to persist the results. The new table is called **T_SURVEY_RESULTS_ETL_<USER_ID>**.

    ![Add Target Table](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Add_TF_Target.png)

8. In the main view, change the load type for the transformation flow as **Intial and Delta**. Save the transformation flow as **TF_Populate_Category_<USER_ID>**. Then Deploy the changes

    ![Save Deploy TF](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Save_TF.png)

9. The **Delta Capture** Option has to be turned on in the table **T_SURVEY_RESULTS_ETL_<USER_ID>** as shown below. 

    ![Delta Capture](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_DeltaCaptureON.png)

If this is not turned on already. Then you have to turn it. Search for the table **T_SURVEY_RESULTS_ETL_<USER_ID>** in the Data Builder section. Then turn on the toggle **Delta Capture**:

  ![Delta Capture On](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_TurnOnDC.png)

10. Now that the transformation flow is ready, you can run it to populate the 'CATEGORY' column in the local table **T_SURVEY_RESULTS_ETL_<USER_ID>**. You can see the status of the run and you will be notified once the run has finished.

![Run Tranformation Flow](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Run_TF.png)

11. You can view the data from using the Data Viewer button in the table **T_SURVEY_RESULTS_ETL_<USER_ID>**

![View Tranformation Flow Data](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_View_Data_TF.png)

12. Now that our data has been transformed using the Transformation Flow. Later, we will build a data model based on this data source. 
As this data set contains numerical values which we want to analyze, we want to adjust the semantic type accordingly. Create a new graphical view.

  ![Add a Measure](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Create_View.png)

13. Drag the table **T_SURVEY_RESULTS_ETL_<USER_ID>** into the modelling canvas. Change the Semantic Usage of the new view to 'Fact'. 


Then name the view **V_SURVEY_RESULTS_<USER_ID>**, save and deploy.

In addition to this, we have to add a measure in the Fact. Measures appear in tables and views with a Semantic Usage of Fact and are columns containing numerical values that you want to analyze. Each Fact must contain at least one measure. Let us add a measure to our new created view.
We will move the column **RATING** as a Measure since this is the KPI that we want to analyze. You can either drag and drop the column in the Measures section or simply use the downward arrow to do so.

![Add a Measure](./images-dsp_integration_1-connect_to_hana_cloud_access_data/DS_Rating_Measure.png)
