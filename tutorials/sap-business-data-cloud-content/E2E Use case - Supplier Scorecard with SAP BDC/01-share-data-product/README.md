# Activating Data Packages in Business Data Cloud Cockpit & Sharing Data Product to SAP Databricks (READ ONLY)

> :books: This is a read-only exercise. Please read through for your information but these steps have been already performed by an SAP BDC Admin<br/>

> [!NOTE]
> For this use case, we will need to share activate and share three SAP-managed data product with SAP Databricks. The data products are Supplier, Supplier Invoice and Purchase Order. In the exercise, you will see how an SAP BDC Admin can activate and share data products in SAP Business Data Cloud. For the purpose of the use case, the SAP BDC admin would need to activate the two packages comprising the above-mentioned data products:
-   SAP Database and Data Management Data Products (SAP S/4HANA Cloud Private Edition) for `Supplier` data product
-   SAP Sourcing and Procurement Data Products (SAP S/4HANA Cloud Private Edition) for `SupplierInvoice` and `PurchaseOrder`


## Persona 
Actors: <br/>
<img src="../../resources/images/data_modeler.png" alt="Data Modeler" width="100"/><br/>
<img src="../../resources/images/bdc_admin.png" alt="BDC Admin" width="100"/><br/>

## Use Case

SAP Business Data Cloud Data Products can be used to:
- Build Analytic Models in SAP Datasphere
- Create custom stories in SAP Analytics Cloud based on a new data model
- Share them with Databricks for ML/AI processing

In all the cases listed above, the activation of a Data Package in SAP BDC Cockpit is a prerequisite to make it available for business users in the Catalog (covered in this exercise). The Data Products of this package are visible in the Catalog after this activation. They can be either shared with Databricks for AI/ML use cases or installed in SAP Datasphere which is required for modeling in SAP Datasphere.

## Overview
This exercise is separated into three sections:
- [Explore Data Products in the Catalog](#explore-data-products-in-the-catalog) (Explanation of the difference between active and inactive Data Products.)
- [Activate Data Packages in BDC Cockpit](#activate-data-packages-in-bdc-cockpit) (Prerequisites to share Data Products with SAP Databricks or to install them in SAP Datasphere.)
- [Share Data Products to SAP Databricks](#share-data-product-to-databricks)  (Share SAP Managed Data products with SAP Databricks)

## Explanation
In the next section, we will learn how to activate a Data Package in SAP Business Data Cloud cockpit and then install the included Data Products in the corresponding SAP Datasphere tenant. 

We will be utilising the following data packages:
- **SAP S/4HANA Database and Data Management Data Products** (SAP S/4HANA Cloud Private Edition) providing Supplier Data Product
- **SAP Sourcing and Procurement Data Products** (SAP S/4HANA Cloud Private Edition) providing both the Supplier Invoice and Purchase Order Data Products

But before we do that, let's take a closer look at what a Data Package is and its key elements.

### Data Package 
A Data package contains sets of related data products for use in modelling projects and pro-code applications. All Data packages are available in the SAP Business Data Cloud Cockpit in the [Catalog & Marketplace](#explore-data-products-in-the-catalog).


### Main components of the Data Package

#### Overview
The Overview section provides the following information about the package:
<img src="./images/BDCDatapackage.png"  width="1000"/>


- Activate: Activation of a Data Package in SAP BDC Cockpit is a prerequisite to make it available for business users in the Catalog (covered in this exercise). 
<!-- Deactivation can also be performed here which is currently represented in this example.  -->

- Category : categories help in organizing and filtering data efficiently, ensuring that users can easily find relevant information related to specific areas like finance or sales.

- Version: Displays the version of the data package.

- Source System: Displays the SAP S/4HANA Cloud Private Edition system that provides the business data which populate the data products.

- Last Modified : Displays the date on which the data package was activated or last modified (appears for active data packages).

- Minimum System Version: This column appears for available data packages only and displays the minimum version of the SAP S/4HANA Cloud Private Edition system required for the data package to be installed. If the current SAP S/4HANA Cloud Private Edition version included in your 'SAP Business Data Cloud' formation is lower than the minimum version required by the data product, the data product cannot be installed.

- System Version: Appears for activated data packages and displays the current version of the SAP S/4HANA Cloud Private Edition system.

- Update: if there are updates available, they will also be shown at the data package level, and you could trigger an update.

####  Activation of a data package
After activating the Data package, the included Data products will become available in both the Business Data Cloud Catalog and SAP Datasphere. These Data Products can be installed exclusively from the Catalog within SAP Datasphere.
- As illustrated, in this precefing example, the Data package contains two Data products tailored to the Financial Operations business use case.

####  Installation of a data product
Installing a Data product for the first time in the corresponding SAP Datasphere tenant will automatically create and deploy an SAP-managed space in the underlying SAP Datasphere.

- SAP-managed Space (or Ingestion space): This space contains all local tables and their corresponding replication flows. Data from the Data products resides in these local tables and are replicated once into this space.
- Custom Space (or Consumption space): This is a user-defined space where the user chooses to install the Data product. The tables in this space are shared copies from the SAP-managed space.

## Observations

### Explore Data Products in the Catalog
> :books: If you are participating in a SAP BDC training, the creation of your SAP BDC Cockpit user has already been done. This next section is just for observations, feel free to click through and learn. <br/>

The catalog in BDC Cockpit provides a structured inventory of business data, while the SAP Datasphere Catalog offers powerful tools for discovering, evaluating, and installing data products, with features that enhance data lineage and integration across various SAP and non-SAP sources.

1. In SAP Business Data Cloud Cockpit, you can create the users in the Security> Users tab and assign them the following roles.
    - BD Viewer: This role is required to view the Cockpit
    - BD Administrator: This role is required to install data packages and intelligent applications
    - Catalog User: This role is required to view the **Catalog & Marketplace** tab inside SAP BDC Cockpit i.e One Data Catalog concept of SAP Business Data Cloud
    - Catalog Administrator: This role is required to install data products.
> <img src="./images/IA_BDC_CockpitRoles.png"  width="1000"/><br/>


2. Access the application ***Catalog & Marketplace*** from the SAP Business Data Cloud Cockpit.
> <img src="./images/catalog_overview.png"  width="1000"/><br/>


3. Select the tab named  ***SAP Business Data Cloud Data Products***. You see all Data Products available. In the Catalog screen, under the tab SAP Business Data Cloud Data Products tab, you can find all the data products that can be now installed in the consumption spaces in SAP Datasphere. They cannot be installed from here. This is just for exploration and sharing with DBX.
<img src="./images/catalog_bdc.png"  width="1000"/><br/>

4. You can apply a filter to only see the data products provided from a specific source system. In the example displayed on the screenshot, we filter for the source system ***HE4_400_BDCPD***, which is an S/4HANA PCE tenant. **Please note that in your system, the name might be different**
<!-- <img src="./images/catalog_filter_S4_HE4.png"  width="1000"/><br/>  -->
<img src="./images/catalog_filter_s4.png"  width="1000"/>

5. Data products are either ***active*** or ***inactive*** as displayed in the overview. 
<!--<img src="./images/catalog_active_inactive_HE4.png"  width="1000"/><br/>  -->
<img src="./images/catalog_active_inactive.png"  width="1000"/> 

6. If you select an inactive data product (in the example displayed on the screenshot: **Real Estate Architecture Object**), the banner on top displays that this data product is disabled and not available for consumption. This means it is not installed for your system yet. It needs to be installed by the BDC Admin in the BDC Cockpit, as explained in the following steps.
<!--<img src="./images/catalog_inactive_HE4.png"  width="1000"/> <br/> -->
<img src="./images/catalog_inactive.png"  width="1000"/>  

> [!NOTE]
> If a data product is not available for consumption yet, its definition is derived from the standard ORD definition. The ORD specification provides a structured way to describe data products. Please find more information about ORD [here](https://open-resource-discovery.github.io/specification/) .

## Steps
### Activate Data Packages in BDC Cockpit

To familiarize yourself with the steps involved, you can read through the following chapter showing the installation of **SAP S/4HANA Financial Operations Data Products**.<br/>

> <img src="../../resources/images/bdc_admin.png" alt="BDC Admin" width="100"/>

1. Log into the SAP Business Data Cloud Cockpit.
<img src="./images/BDCCockpit_login.png"  width="1000"/><br/>

2. In the cockpit, open the tab **Insight Applications and Data Packages**. This tab shows all the Intelligent Applications and Data Packages that are available for installation. <br/>
<img src="./images/insight_apps_data_packages.png"  width="1000"/><br/>

3. Search for the Data Package that you want to activate. In this example, we will activate the **SAP S/4HANA Financial Operations Data Products**. This data package is available for activation and includes two data products. 
<img src="./images/DataPackage_screen.png"  width="1000"/><br/>


> [!IMPORTANT]
When activating a data package, make sure the source system is correctly identified and accessible. Check that the source system's version meets or exceeds the minimum required by each data product in the package. Data products will only activate if their minimum version requirements are met. For example, if one product requires version 2021 and another requires 2025, and your S4 system is on version 2024, only the product requiring version 2021 will activate. Additionally, the data package itself may have a minimum version requirement; if the source system doesn't meet this, no data products will install. The installation of data products can be partial or full based on the source system's version compatibility.

4. Click on ***Activate*** to start the installation process. You will be asked to select the source system. Activating the Data Package will make the Data Products available in the Catalog. :wrench: <br/>
<img src="./images/Datapackage_sourcesystem.png"  width="1000"/><br/>
 

5. The status changes to **Activating**. This takes some time depending on the volume of the data in the underlying source system. SAP Business Data Cloud takes care of the data extraction and processing in the background. Once, the activation completes, the Data Products that are comprised in this Data Package are available for consumption. :wrench:<br/>
<img src="./images/Datapackageactivation_screen.png"  width="1000"/><br/>

6. The Data package and the Data Product comprised in it is now **Active**,if there are updates available, they will also be shown at the data package level, and you could trigger an update. 
<img src = "./images/DataPackage_active.png" width= "1000"/><br/>

7. After installation of the data package **SAP S/4HANA Financial Operations Data Products**, you will find under the **Installed** tab in Intelligent Applications and Data Packages.
<img src = "./images/Insightappandpackage_active.png" width= "1000"/><br/>

### Share Data product to SAP Databricks
The SAP-managed data product can be shared with SAP Databricks to be used in AI/ML use cases. One would require an admin role to share the data product to SAP Databricks or otherwise.
For this use case, we will need to share three data products to SAP Databricks. The data products are the following:
- `Supplier`
- `SupplierInvoice`
- `PurchaseOrder`

> [!NOTE]
> Below are the steps to share the `Cashflow` data product. The process is identical to share any other data product to the desired SAP Databricks workspace

1. In the SAP BDC Cockpit, click on `Search`to navigate to the Data Catalog.

    ![./images/img_10.jpg](./images/login_bdc_cockpit.png)<br/>

    <hr>

2. Search for the data product **Cashflow** and click on the tile to open.

    ![./images/search_cashflow_dp.png](./images/search_cashflow_dp.png) <br/>

    <hr>

3. On the detail page click on the *`Share`*-button to open the dialog

    ![./images/share_cashflow_dp.png](./images/share_cashflow_dp.png)<br/>

    <hr>

4. Enter a `Share Name` and target SAP Databricks `Workspace` and click on `<Share>`-button.

    ![./images/target_cashflow_workspace.png](./images/target_dbx_cashflow_workspace.png)<br/>

    <hr>

5. Login SAP Databricks and navigate to the Unity Catalog.

    ![./images/unity_catalog.png](./images/unity_catalog.png)<br/>

    <hr>

6. Navigate to the `Delta Shares Received`, find the table `cashflow` and click on the tab `Sample Data`.

    ![./images/cashflow_sample_data.png](./images/cashflow_sample_data.png)<br/>

    <hr>

7. Click on `Select Compute`and select `Serverless Starter Warehouse`, then click on `Start and Close`.

    ![./images/cashflow_sample_data.png](./images/cashflow_serverless_compute.png)<br/>

    <hr>

8. Preview the `cashflow`sample data

    ![./images/cashflow_sample_data_preview.png](./images/cashflow_sample_data_preview.png)<br/>

    <hr>
