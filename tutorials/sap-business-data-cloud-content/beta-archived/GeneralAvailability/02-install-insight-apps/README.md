# Install Intelligent Applications
*:construction_worker: [@NeethaPucknat](https://github.tools.sap/D072636)* 

Insight apps are a premium offering exposed through BDC (Business Data Cloud). They are innovative applications designed to streamline data analytics processes from observation to action. 
Insight apps are intended to provide comprehensive dashboards, facilitate data analysis, and suggest viable actions based on the analysis; using artificial intelligence when applicable.
:wrench: The market entry version of BDC offers two SAP-managed intelligent applications. In this exercise, let us look at how we can install one of these intelligent applications called the **Working Capital Dashboard** so that we can start using our the underlying data products to their full potential.


## Persona 
Actor: <br/>
<img src="../resources/images/bdc_admin.png" alt="BDC Admin" width="85"/><br/>
Stakeholders: <br/>
<img src="../resources/images/business_analyst.png" alt="Business Analyst" width="105"/>
<img src="../resources/images/business_user.png" alt="Business User" width="100"/>

## Prerequisites
You have completed the configuration of the SAP BDC Cockpit which can be found [here](01-basic-config-bdc-cockpit/README.md).

## Use Case
This exercise describes the installation of the Intelligent Application called Working Capital Dashboard. This exercise will also be describing how the content authorisations will be configured.

Working Capital Dashboard provides:
<ul>
<li>an overview of financial positions like
<ul>
<li>Accounts Payables/ Receivables</li>
<li>Cash & Liquidity</li>
<li>Inventory etc.</li>
</ul>
</li>
 <li>
KPIs to assess working capital management performance like
<ul>
<li>NWC/TNS: Net Working Capital/ Total Net Sales</li>
<li>Cash Conversion Cycle</li>
<li>DSO/DPO: Days Sales Outstanding/ Days Payables Outstanding etc.</li>
</ul>
</li>
</ul>

The illustration below gives an impression of the look and feel of the Insight app:<br/><br/>
![IA_Overview](images/IA_Overview.png) 


## Steps
1. Open the **Insight Applications and Data Packages** module in SAP Business Data Cloud. 
![IA_Entry](images/IA_Entry.png) 

2. This module shows the “Working Capital” Insight Application which is available for installation.
![IA_WCB](images/IA_WCB_1.png)

3. Opening the overview page shows the corresponding data products and content.
![IA_WCB_DP](images/IA_WCB_DP.png)

4. Click on the 'Install' button to kick off the installation. A dialog opens up to confirm the installation details. Click on 'Install' again to confirm.
![IA_WCB_Properties](images/IA_WCB_Properties.png)
> [!NOTE]
> This will save the related content in an SAP-Managed space in SAP Datasphere (DSP) and an SAP-Managed folder in SAP Analytics Cloud (SAC).

5. The status of the installation changes to 'Installing' and then 'Active' when the installation has finished.
![IA_WCB_Installing](images/IA_WCB_Installing.png)
> [!NOTE]
> This step can take upto from upto several minutes to hours since the step also entails fetching all the underlying data products data into the storage and semantic layer of BDC.

6. To view the content, SAP Datasphere can be opened.
![IA_WCB_Active](images/IA_WCB_Active.png)
> [!NOTE]
> There is no additional log in required since SAP Datasphere and SAP Business Data Cloud are on one tenant mode.

7. In the **Security> Roles** tab, a new scoped role has to be created to manage access. The scoped role has the newly created **Working Capital** space as the scope and the permissions as shown.
![IA_Role](images/IA_Role.png)<br/>
![IA_Permission](images/IA_Permission.png)

8. After this, in the **Security> Users** tab, add all the users that will need access to this content.<br/>
![IA_CreateUsers](images/IA_CreateUsers.png)<br/>
![IA_AddUsers](images/IA_AddUsers.png)<br/>
> [!NOTE]
> For simplicity, the users are added manually and same scope role is provided to everyone. If there are existing user management concepts already in place, they can be applied using the existing user management and role management capabilities.

9. Open the Data Access Control of the installed Insight Application and add all the relevant users to it. If this step is not performed, the users would not be able to see any data (i.e. in data preview in SAP Datasphere, or in Story consumption).<br/>
![IA_EditDAC](images/IA_EditDAC.png)<br/>
![IA_DACUsers](images/IA_DACUsers.png)<br/>

10. Open SAP Analytics Cloud.
![IA_OpenSAC](images/IA_OpenSAC.png)<br/>

11. In SAC, in the **Security>Users** tab, add all the relevant users who will need access to content in SAC and so that the content can be shared with them. 
![IA_AddSACUsers](images/IA_AddSACUsers.png)<br/>
![IA_AddMoreSACUsers](images/IA_AddMoreSACUsers.png)<br/>

12. From the Managed content folder in the file repository, grant the access rights to the **Working Capital** folder to all relevant users.
![IA_ShareSACContent](images/IA_ShareSACContent.png)<br/>
![IA_ShareSACContentUsers](images/IA_ShareSACContentUsers.png)<br/>

13. **Working Capital** Insight Application and the **Working Capital dashboard** are now available for consumption.

## Next Steps
In the next [exercise](/03-consuming-intelligent-applications/README.md), you will learn how a business user can start consuming the Insight Application to draw meaningful insights from the underlying data product.
