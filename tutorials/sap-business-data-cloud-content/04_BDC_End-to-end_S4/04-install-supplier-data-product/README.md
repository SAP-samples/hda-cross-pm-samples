# Install Supplier Data Product in custom space in SAP Datasphere

For this exercise, let us proceed to install the data product **Supplier**.
In the Governance tab, an administrator or steward can set up the rules. For our case, we have already activated auto-approval on this data product. By doing this, anyone who wants to install the data product in SAP Datasphere does not need to wait for approval.

An administrator or data steward navigates to SAP BDC Cockpit > Governance > Data Product Management. Search for the data product and then, turn the flag **Auto-Approval** on.

Without auto-approval enabled, the steward must manually approve each data product installation request — a workflow suited for sensitive data products or those requiring compliance oversight.

## HANDS-ON: Install Data Product in SAP Datasphere
### Access Request creation and approval
1. Navigate to SAP Datasphere.
2. Open **Catalog & Marketplace** and search for the data product `Supplier`. 

3. Click on **Add to Cart**.

4. Proceed from the cart as shown below.


5. Add the space name and comments. Check the Terms and Conditions checkbox after reading it. For this data product, there are no terms and conditions set up in the governance process. Then click **Send**.


6. The Access Request gets auto-approved.


### Data Product Access
1. Navigate to **Catalog & Marketplace**. Open **Data Product Access**.
2. Navigate to the Data product in question and click on **Install Data Product**.


3. Select the Access Type as **Replication**. 

4. Click **Install**.

5. Once the installation is complete, you can view the data product remote tables in your space assigned to you. Open **Data Builder** and navigate to the space assigned to you. You can view that the tables are now shared from the Snowflake ingestion space into your custom space.


6. Optionally, create a graphical view to view the data.

>[!Note]
As the table ***Supplier*** is shared from the SAP-managed space. The table is automatically populated by the Replication Flow, so you don't need to manually start a run. 

You can now enhance the business use case by building on top of the installed data product.
