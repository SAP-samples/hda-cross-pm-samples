# Create an Entity Relationship Model in SAP Datasphere
<!-- description --> An entity-relationship model (or E/R model) describes interrelated things of interest in a specific domain of knowledge. You can use an E/R model to better understand a subset of the entities in your space, and to communicate this information to other stakeholders. By using an E/R Model in Datasphere, you can maintain relations between your entities which will be leveraged in the reporting later.

## Prerequisites
 - You have [imported your dataset into your Space.](../dsp_modeling_1-import-dataset/dsp_modeling_1-import-dataset.md)

## You will learn
  - Overview of E/R Models
  - How to create an E/R Model
  - How to associate data columns
  - Finalise an E/R Model and deploy

---

### Understand the basics of E/R models


An E/R model provides a diagram for organising your data entities (tables and views) in relation to one another. You can:

•	Add entities from the repository or import them from a connection or a CSN file, as well as creating new entities directly

•	Modify the properties of your entities including adding human-readable business names and creating associations directly in the diagram

•	Save and deploy all the contents of your model with a single action

The work that you do in an E/R model benefits all the users in your space as they can use the entities that you import or enhance as sources in their views.

A data model is a way to organise the data and define the relationship between the data elements you have, to give it a structure. This structure must be aligned with your team's needs to generate reports and queries.


### Create an E/R model


1.	Go to the Data Builder and click on the **New Entity-Relationship Model** button

    ![ER Model Icon](./images-dsp_modeling_2-create-relationships/DS_Create_ER_Model.png)

2.	This takes you into the graphical modelling interface. Since you have imported the sample data manually via CSV, your data can be found under the **Repository** tab
3.	Click and drag the tables `T_SalesOrders`, `T_BusinessPartners` and `T_Addresses` onto the canvas

    ![SalesOrder and SalesOrderItems](./images-dsp_modeling_2-create-relationships/DS_Import_Tables.png)

5.	With the data tables in your modelling interface, you are now ready to create the relevant associations and deploy your E/R model.

### Adjust Semantic Types

1. Each entity (tables and views) have a property called `Semantic Usage`. This property is used to indicate the type of data contained in the entity. Select the table `T_SalesOrders` and set the Semantic Usage to `Fact`. This indicates that your entity contains numerical measures that can be analyzed.
2. Drag the measures `GROSSAMOUNT`, `NETAMOUNT` and `TAXAMOUNT` from the **Attributes** section into the **Measures** section

  ![SalesOrders_MeasuresAndAttributes](./images-dsp_modeling_2-create-relationships/DS_SO_Items.png)

3. After maintaining the semantic type of the table in the first step, specify the semantic types for the measures and attributes now. Semantic types include values, quantities, dates, and geo and textual information. Click on the **Edit columns** pencil icon for attributes and select the according `Semantic Type` for `CURRENCY`.

  ![SalesOrders_SemanticTypes_Attributes](./images-dsp_modeling_2-create-relationships/DS_SO_Items_Attributes.png)

4. Next, click on the **Edit columns** pencil icon for measures. Assign `Semantic Type` and `Unit Column` as displayed in the screenshot

  ![SalesOrders_SemanticTypes_Attributes](./images-dsp_modeling_2-create-relationships/DS_SO_Items_Measures.png)

5. Adjust the semantic type of `BusinessPartners` to `Dimension`. This indicates that your entity contains attributes that can be used to analyze and categorize measures defined in other entities

6. After adjusting the semantic type, a yellow validation warning is displayed as Dimension entities need at least one key attribute. Define `PARTNERID` as key attribute by clicking on **More** when hovering the attribute

    ![BusinessPartners](./images-dsp_modeling_2-create-relationships/DS_BP_Key.png)

7. Adjust the semantic type of `T_Addresses` to `Dimension`

8. Set `ADDRESSID` as key attribute 

9. Save and deploy the entities of E/R Model by clicking the according buttons in the upper left corner. Set the technical name to `ER_Sales`. When saving entities in Datasphere, they are stored as design-time definition. Deploying an entity creates a run-time version

  ![Deploy E/R Model](./images-dsp_modeling_2-create-relationships/DS_ER_Deploy.png)

### Associate Data Columns

Associations are created and maintained in the E/R model editor, in the table editor or in the graphical view/SQL editor. As we are modifying associations between multiple tables, we will use the E/R model editor.
They are used to e.g. associate master data, text or time objects to fact data.

1. Click on the `T_SalesOrders` table and then click on the **Create Association** arrow icon

2.	Drag it over to the `T_BusinessPartners` table to create an association between the two tables

3.	Ensure that the created association is between the columns `PARTNERID` in the **Association Properties** panel

4.	Drag and drop to connect the `PARTNERID` column from one table to the other if it's not done already

    ![BusinessPartners Table](./images-dsp_modeling_2-create-relationships/DS_SO_BP_Association.png)


5.	Now create an association between the `T_BusinessPartners` and `T_Addresses` tables using the `ADDRESSID` column (drag the association from `T_BusinessPartners` to `T_Addresses`)

    ![AddressID Association](./images-dsp_modeling_2-create-relationships/DS_BP_AD_Association.png)
    

### Create Hierarchy for Addresses
1. Select the hierarchy table `T_Addresses`and click on the **Hierarchy** Icon on the right side.
   
   ![Hierarchies](./images-dsp_modeling_2-create-relationships/DS_Hierarchy.png)
   
2. Adding a hierarchy enable drill-down and drill-up in BI clients. A Level-Based hierarchy is non-recursive, has a fixed number of levels, and is defined by specifying two or more level columns within the dimension. Define a hierarchy for the location
   
  ![Hierarchies](./images-dsp_modeling_2-create-relationships/DS_Hierarchy2.png)

### Create Time Association
After creating associations between the imported data entities, add an association to the already existing time dimension. This allows you to work with this date data at a granularity of day, week, month, quarter, and year, and to drill down and up in hierarchies.

1. Drag the view `Time Dimension - Day`(`SAP.TIME.VIEW_DIMENSION_DAY`) onto the modelling canvas and view the properties. This generated dimension includes different predefined hierarchies

  ![Time Dimension](./images-dsp_modeling_2-create-relationships/DS_TimeDimensionDay.png)
    
2. Create an association from the column `CREATEDAT` of `T_SalesOrders` to `Date` of `Time Dimension - Day`(`SAP.TIME.VIEW_DIMENSION_DAY`). Validate using the data preview that the date format of the two columns is the same as this is required for the mapping
   
  ![Time Dimension Association](./images-dsp_modeling_2-create-relationships/DS_TimeDimensionDay_Association.png)

3. Have a look at the properties of the table `Time Dimension - Day`(`SAP.TIME.VIEW_DIMENSION_DAY`) dragged into the editor. In the **Association** section, different associations to text entities are displayed. Have a look at the associated table `Translation Table - Day `and open it in a new tab. An entity with the semantic usage `Text` must to have one identifier , one language identifier and one text attribute. Open the data preview to see the data records. Keep the table as it is generated.

  ![Time Dimension Text](./images-dsp_modeling_2-create-relationships/DS_TimeDimensionDay_Text.png)

> **_HINT:_**  The last point may be useful for an optional exercise later on!

> **_CHECK:_** This is how the T_SalesOrders attribute table would look after creating all the necessary relationships.

  ![SO_Attributes_ER](./images-dsp_modeling_2-create-relationships/DS_SO_Attributes_ER.png)


### Save and deploy

Save and deploy your Entity-Relationship Model again to activate the recent changes (e.g. associations).

> **_NOTE:_**  If there are 2 warnings at this point on the `Time Dimension - Day`(`SAP.TIME.VIEW_DIMENSION_DAY`) View, they can be ignored and the ER model can be saved and deployed using the `Save Anyway` and `Deploy Anyway` buttons. These are known warnings and will be fixed in an upcoming release.

### Maintaining Semantic Usage and Semantic Types in Table Editor

In the previous steps you have maintained associations and semantic properties using the E/R Model. These changes to objects like tables and views can also be done in the table/view editor. 
Rules for creating associations depend on the Semantic Usage. A Fact can only point to a Dimension or a Text Entity, but not to another Fact view or table. 
Hence, we haven't modified `T_SalesOrderItems` yet as it is not part of the E/R Model which arranges the data entities in relation to one another. 

1. Go to Data Builder UI and select the table `T_SalesOrderItems`. 
  
  ![SalesOrderItem_1](./images-dsp_modeling_2-create-relationships/DS_SalesOrderItem_1.png)
     
2. Set the Semantic Usage to Fact. This indicates that your entity contains numerical measures that can be analyzed.
  
  ![SalesOrder_2](./images-dsp_modeling_2-create-relationships/DS_SalesOrder_2.png)
     
3. Select the measures `GROSSAMOUNT`,`NETAMOUNT`,`TAXAMOUNT` and `QUANTITY` from the Attributes section and convert them into the Measures.
  
  ![SalesOrderItem_3](./images-dsp_modeling_2-create-relationships/DS_SalesOrderItem_3.png)
     
4. Go to the Attributes section and select the appropriate Semantic Type for `CURRENCY` and `QUANTITYUNIY`.
  
  ![SalesOrderItem_4](./images-dsp_modeling_2-create-relationships/DS_SalesOrderItem_4.png)
     
5. Next, go to the Measures section and assign Semantic Type and Unit Column as displayed in the screenshot
  
  ![SalesOrderItem_5](./images-dsp_modeling_2-create-relationships/DS_SalesOrderItem_5.png)
     
6. Save and Deploy the changes.   
---
