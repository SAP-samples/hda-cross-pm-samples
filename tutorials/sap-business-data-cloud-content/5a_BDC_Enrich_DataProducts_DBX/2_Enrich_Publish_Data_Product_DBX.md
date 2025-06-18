
## Contents
  - Persona
  - Log On to SAP Databricks
  - SAP Databricks Enhancing Data Products
  - Usage of sap-bdc-connect-sdk
  - Verify Published Data Product

## Persona 

![](../500_BDC_Personas/Images/Data_Scientist_Derek_Ian.png)

In this lesson we will work with a data product in **SAP Databricks** shared from **SAP Business Data Cloud** and create an enhanced version of it. Then we will share the new data product to **SAP Datasphere** using **SAP Business Data Cloud SDK**.

## Prerequisites
- You are logged on to SAP Databricks.

## Log On to SAP Databricks

1. Open a Chrome browser or Microsoft Edge browser and enter the **SAP Databricks** URL.
   
    Alternatively, click <a href="{link|dbx}" target="_blank">here</a>.
   
   <!-- Access **SAP Databricks** using the link in the **Basic Trial BDC** formation.
   ![525_2_image01](./Images/525_2_image01.png)-->

2. Provide **Email** and select **Continue**. 

   Email: **{placeholder|userid}@sapexperienceacademy.com**

   ![525_2_image02](./Images/525_2_image02.png)

3. Select **Continue with SSO**.
   
   ![525_2_image03](./Images/525_2_image03.png)

4. Select default **workspace** to continue.
   
   ![525_2_image04](./Images/525_2_image04.png)

5. SAP Databricks welcome page will open.
   
   ![525_2_image05](./Images/525_2_image05.png)

<!-- ["","",""] -->   

## SAP Databricks Enhancing Data Products

6. Select **Catolog** in the navigation menu on the left. 
   
    ![525_2_image35](./Images/525_2_image35.png)

7. Under **Delta Shares Received**, expand **companycode_share** -> **companycode** ->  and select the **companycode** table. 
   
   This **Data Product** was shared from the **SAP Business Data Cloud** to **SAP Databricks** and it's available for consumption.
   
   ![525_2_image36](./Images/525_2_image36.png)

   <!-- ![525_2_image06](./Images/525_2_image06.png)-->

8.  Switch to the **Sample Data** tab. If a compute resource isn't started choose **Select compute**. 
   ![525_2_image07](./Images/525_2_image07.png)

9.  Select **Serverless** and **Start and Close**.
   ![525_2_image08](./Images/525_2_image08.png)

10. Once the service starts the sample data should appear. 
    
    Here we are accessing remote the data shared from **SAP Business Data Cloud**.
    
    ![525_2_image09](./Images/525_2_image09.png)

<!-- ["","",""] -->

11. Under **My organization** catalog section, expand **company_code_data_product** -> **company_code** -> and  select the **company_code_cluster** table.
    
    This table has been populated with company code clusters. It's the enhanced dataset we will share back to **SAP Datasphere** after reviewing how we created the table.
    
    ![525_2_image10](./Images/525_2_image10.png)

12. Switch to the **Sample Data** tab to view data. 
    
    This table has been created and populated to store company code clusters using a **Python** notebook. We won't be reprocessing the notebook again as part of this lesson but will review how data has been enhanced in the next step.
     
    ![525_2_image11](./Images/525_2_image11.png)

13. Download the notebook used to create & populate this table [here](./Files/Company_Clustering.py) (Right click and **Save link as**).

<!-- ["","",""] -->

14. After saving the notebook locally, select **Workspaces** in the left navigation menu.
    
    ![525_2_image37](./Images/525_2_image37.png)

15. Expand **Workspace** -> **Users** and right click on your username and select **Import**.

    ![525_2_image38](./Images/525_2_image38.png)

    <!--![525_2_image12](./Images/525_2_image12.png)-->

16. Select **Browse** to locate the file.
    
    ![525_2_image13](./Images/525_2_image13.png)

17. **Import** the **Company_Clustering.py** notebook.
    
    ![525_2_image14](./Images/525_2_image14.png)

<!-- ["","",""] -->

18. Select the **Company_Clustering** file to open the notebook.
    
    ![525_2_image15](./Images/525_2_image15.png)

19. Read thru the explanations and the code in the notebook explaining step by step how we were able to create the company code clusters. 

    > **Note:** Please do `NOT` execute any of the code piece
    ![525_2_image16](./Images/525_2_image16.png)

<!-- ["","",""] -->

20. Now we will share the comany code clusters table via **Delta Share** and publish it to **SAP Datasphere** as a new data product.
    
21. Select **Catalog** in the left navigation menu.
    
    ![525_2_image39](./Images/525_2_image39.png)

22. Under **My organization** catalog section, expand **company_code_data_product** -> **company_code** and select the **company_code_clusters** table.
    
    ![525_2_image40](./Images/525_2_image40.png)

23. Next select **Actions** and choose **Share via Delta Sharing** (under 3-dot kebab icon on the upper right).
    
    ![525_2_image41](./Images/525_2_image41.png)

    <!--![525_2_image17](./Images/525_2_image17.png)-->

24. Select **Create a new share with the table**.
    
    Provide **Share name** and **Recipients**:

    - **Share name** : company_code_clustering_share_{placeholder|userid}

        > **Note:** Make sure **username** in the **Share name** is lowercase. In the following steps we will execute codes in a notebook. They are case-sensitive. So make sure all characters in the username are lowercase

    - **Recipients (optional)** : sap-business-data-cloud  

    Select **Share**.

    ![525_2_image18](./Images/525_2_image18.png)

<!-- ["","",""] -->

25. Select the **Gear** icon on the catalog and then select **Delta Sharing**.
    
    ![525_2_image19](./Images/525_2_image19.png)

26. Switch to **Shared by me** and filter for your username **{placeholder|userid}** (no space at the end) and select the delta share just created.

    > **Note:** Refresh the browser if the data share does not appear.
    
    ![525_2_image20](./Images/525_2_image20.png)

27. Assets in the share you created will be displayed. 
    
    ![525_2_image21](./Images/525_2_image21.png)

<!-- ["","",""] -->

## Usage of sap-bdc-connect-sdk

In this section we will import another notebook and execute 5 code pieces:
  - Install SDK
  - Create a client
  - Create a share
  - Create the share CSN
  - Publish a Data Product
  


28. Download the notebook we will use to publish a data product from **SAP Databricks** [here](./Files/Publish_Data_Product.py) (Right click and **Save link as**).
    
29. After saving the notebook locally, select **Workspace** in the left navigation and expand **Workspace** -> **Users** and right click on your username and select **Import**.

    ![525_2_image12](./Images/525_2_image12.png)

30. Select **Browse** to locate the file.
    
    ![525_2_image23](./Images/525_2_image23.png)

31. **Import** the **Publish_Data_Product.py** notebook.
    
    ![525_2_image24](./Images/525_2_image24.png)

<!-- ["","",""] -->

32. Select the **Publish_Data_Product** file to open the notebook.
    
    ![525_2_image25](./Images/525_2_image25.png)

33. Execute the **first** code block by clicking **Run** on the upper left corner of the cell.
    
    This code will install the SDK. It should take about a min to complete. A green check will appear next to Run once it completes.

    > **Note:** Ignore version related warnings and pip dependency errors.    

    ![525_2_image26](./Images/525_2_image26.png)

34. Execute the **second** code block. 
    
    This code creates a client: 
    -   DatabricksClient receives dbutils as a parameter, which is a SAP Databricks utility that can be used inside the Databricks notebooks
    -   BdcConnectClient receives the DatabricksClient as a parameter to get information from the SAP Databricks environment (e.g. secrets, api_token, workspace_url_base)
  
    
    ![525_2_image27](./Images/525_2_image27.png)

<!-- ["","",""] -->

35. Execute the **third** code block to create a share.

    A share is a mechanism for distributing and accessing data across different systems. Creating or updating a share involves including specific attributes, such as @openResourceDiscoveryV1, in the request body, aligning with the Open Resource Discovery protocol. This procedure ensures that the share is properly structured and described according to specified standards, facilitating effective data sharing and management.
     > **Note:** There are 2 places you need to modify in this code. **share_name** and **title**. Make sure **<lowercase_username>** in the **share_name** is lowercase.

    - **share_name** : "company_code_clustering_share_<lowercase_username>" <br>
    - **title** : "Company Code Clustering Data Product From {placeholder|userid}"
    <br>

    ![525_2_image28](./Images/525_2_image28.png)

36. Execute the **fourth** code block to create the CSN.

    The CSN serves as a standardized format for configuring and describing shares within a network. To create or update the CSN for a share, it's advised to prepare the CSN content in a separate file and include this content in the request body. This approach ensures accuracy and compliance with the CSN interoperability specifications, facilitating consistent and effective share configuration across systems.
    > **Note:** Make sure **share_name** is in lowercase as in the previous step.

    - **share_name**: "company_code_clustering_share_<lowercase_username>"

    ![525_2_image29](./Images/525_2_image29.png)

37. Execute the **fifth** code block to publish the data product to **SAP Datasphere**.

    A Data Product is an abstraction that represents a type of data or data set within a system, facilitating easier management and sharing across different platforms. It bundles resources or API endpoints to enable efficient data access and utilization by integrated systems. Publishing a Data Product allows these systems to access and consume the data, ensuring seamless communication and resource sharing.
     > **Note:** Make sure **share_name** is in lowercase as in the previous step.

    - **share_name**: "company_code_clustering_share_<lowercase_username>"   
    ![525_2_image30](./Images/525_2_image30.png)
  
<!-- ["","",""] -->

## Verify Published Data Product

Log on to SAP Datasphere.

38. Open a Chrome browser or Microsoft Edge browser and enter the SAP Datasphere URL.
   
    Alternatively, click <a href="{link|dwc}" target="_blank">here</a>.

   <!--In **SAP Business Data Cloud** access the **SAP Datasphere** tenant in the **Basic Trial BDC** formation. 
    Alternatively, click <a href="{link|dwc}" target="_blank">here</a>.
    ![525_2_image31](./Images/525_2_image31.png) -->

39. Login with your user credentials. 
   
    Username: **{placeholder|userid}**

    Password: **enter provided password**

   ![525_3_image08](./Images/525_3_image08.png)

40. Once **SAP Datasphere** welcome page opens select **Catalog & Marketplace** and **Search**.
    
    ![525_2_image32](./Images/525_2_image32.png)

<!-- ["","",""] -->

41. Filter for **All** -> **Data Products** and **System Instance** as shown, then enter **{placeholder|userid}** in the search bar. 
    
    The data product you just published from **SAP Databricks** should appear first under Data Products. 
    
42. Select your **Company Code Clustering Data Product from {placeholder|userid}**.
    
    > **Note:** Published data product will not appear instantly in **SAP Datasphere** since it triggers list of actions which happen on a pre-scheduled intervals. If you don't see your data products wait for a few minutes and try again.  
    
    ![525_2_image33](./Images/525_2_image33.png)

43. Open the data product to verify it's the one you published from **SAP Databricks**.
    
    ![525_2_image34](./Images/525_2_image34.png)

44. Go back to **Home**.
    
    ![525_2_image34](./Images/525_2_image42.png)

<!-- ["","",""] -->

<br/>

**Congratulations!** You have successfully published a Data Product from **SAP Databricks**.

<br/>

