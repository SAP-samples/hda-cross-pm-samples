## Contents
  - Persona
  - Install Data Product

## Persona 

![](../500_BDC_Personas/Images/Data_Analyst_John_Smith.png)

In this lesson we will install a data product in **SAP Datasphere** shared from **SAP Databricks**. In the previous exercise you published your own data product from SAP Databricks. 

We will be using a previously published data product because of 2 reasons:
-   You can continue with rest of the lessons, even if you did not complete the previous Databricks lesson
-   It reduces the number of duplicate data products within the SAP-Managed space in SAP Datasphere

<!-- ["","",""] -->

## Install Data Product

Log On to SAP Datasphere if not already.

1. Open a Chrome browser or Microsoft Edge browser and enter the **SAP Datasphere** URL.
   
   Alternatively, click <a href="{link|dwc}" target="_blank">here</a>.
   
    <!-- Access **SAP Datasphere** using the link in **SAP Business Data Cloud** under **System Landscape** in the **Basic Trial BDC** formation. 
    ![525_3_image01](./Images/525_3_image01.png)-->

2. Login with your user credentials. 
   
   Username: **{placeholder|userid}**

    Password: **enter provided password**

   ![525_3_image08](./Images/525_3_image08.png)

<!-- ["","",""] -->

Search for the Data Product to install.

3. Select **Catalog & Marketplace** from the **side navigation area**, then **Search**.
   
   ![525_3_image09](./Images/525_3_image09.png)

4. Select the **Filter** icon and filter on **All->Data Products** and **databricks-ee9691c9** System Instance Name.
   
    ![525_3_image10](./Images/525_3_image10.png)

5. In the search bar type **cluster** and select the **Company Code Clustering Data Product** `without` a username in the title.
   
    > **Note:** When publishing a data product from SAP Databricks to SAP Datasphere for the first time, there might be a latency for the initial flow of data because the procedures run in predefined intervals. That's another reason why we are installing a previously published & used data product so we can continue the exercise without waiting.

    <!--- ![525_3_image02](./Images/525_3_image02.png) --->

    ![525_3_image10](./Images/525_3_image11.png)

<!-- ["","",""] -->

Install the Data Product.

6. Verify you chose the correct data product (no username in the title) and select **Install**.

    ![525_3_image03](./Images/525_3_image03.png)

    If you pressed **Enter/Return** or selected **Search** after typing **cluster** (instead of choosing the data product directly from search suggestions), then it will list all data products with **cluster** in the name. To easily locate the correct data product switch to **List View** using the icon shown in the screenshot. The data product `without` your username is the one we will be installing (the first data product). Select it a continue with Install.

    ![525_3_image03_01](./Images/525_3_image03_01.png)

7. Select the **{placeholder|userid}** space and continue with **Next Step**.

    ![525_3_image04](./Images/525_3_image04.png)

8. Select the **company_code_cluster** data product and **Start Import and Deploy**.

    ![525_3_image05](./Images/525_3_image05.png)

9.  Under **Data Builder** select your space **{placeholder|userid}**.

    ![525_3_image06](./Images/525_3_image06.png)

10. The new data product is now available in your space. 
    
    Notice that the data product is in **SAP-Managed** space and shared with you. The reason for this is to prevent data duplication. Even if the data product is installed many times by multiple users, data will be shared from SAP Databricks to SAP Datasphere only once.

    > **Note:** Installation and deployment might take up to a minute. If you don't see the data product, then refresh the page.

    ![525_3_image07](./Images/525_3_image07.png)

11. Go back to **Home**.

    ![525_3_image07](./Images/525_3_image12.png)

<!-- ["","",""] -->

<br/>

**Congratulations!** You have successfully installed a Data Product.

<br/>