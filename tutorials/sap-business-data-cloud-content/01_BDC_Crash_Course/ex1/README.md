# Exercise 1 - Provision BDC via SAP for Me (10 min)

When you subscribe to SAP BDC, you use SAP for Me to provision an SAP BDC tenant. 
You will need the following to perform this activity:
- An SAP for Me account
- Successful purchase of the SAP Business Data Cloud product and the corresponding entitlements


## Exercise 1.1 Read-only: Provision SAP Business Data Cloud Cockpit in SAP for Me

Due to the technical and time limitations, activities in this exercise will be read-only. 

In the SAP for Me account, under the **Portfolio & Products** Tab, the tile **SAP Business Data Cloud** tile is visible since the product has been purchased and the commercial entitlement for SAP Business Data Cloud also exists in your URM organization. By clicking it, you can explore all the technical entitlements, also known as Eligibilities. The are the set of eligible applications that are part of the SAP BDC.

<img src="images/sap4me-images/sap4me-entry.png" alt="internalHost" width="1500"/><br/>

You can choose to provision them whenever needed and as many times as needed. To start provisioning, choose 'Enable' as shown in the following image.

<img src="images/sap4me-images/enableCoreProduct.png" alt="enableCoreProduct" width="1500"/><br/>


1. To start provisioning the SAP BDC apps, you must first enable the SAP Business Data Cloud Core product. By doing so, the apps will become enabled and available for provisioning. SAP BDC Core product pertains directly to the application SAP BDC Cockpit.

<img src="images/sap4me-images/enableBdcCoreProduct.png" alt="enableBdcCoreProduct" width="1500"/><br/>

2. After adding general information, by default a new SAP BDC tenant is initiated for provisioning.

<img src="images/sap4me-images/addNewSystemAuto.png" alt="addNewSystemAuto" width="1500"/><br/>

3. Then, you provide the relevant input parameters using a guided wizard. This wizard is generated on the fly, based on configuration placed by the application owner.

<img src="images/sap4me-images/coreProductInfo.png" alt="coreProductInfo" width="1500"/><br/>
 
4. Finish the setup. <br/>
<img src="images/sap4me-images/finishProvisioning.png" alt="finishProvisioning" width="1500"/><br/>

5. When the provisioning is complete, you can explore the solution and tenant resources that were just created for the app. Information on each resource is displayed, including the allocated quota and the status. Finally, you can launch the provisioned application. <b> The provisioning of the SAP Business Data Cloud Cockpit is successful.</b><br/>

<img src="images/sap4me-images/viewResources.png" alt="viewResources" width="1500"/><br/>

6. In the **Resources** tab that opens, the application SAP BDC Cockpit displays. You can view the solution and the tenant resources that were just created for the cockpit application, including the quota and the allocated status. The status shows as **Processing** and then changes to **Ready**.
<img src="images/sap4me-images/viewResourcesCoreProduct.png" alt="viewResourcesCoreProduct" width="1500"/><br/>

You have successfully provisioned the BDC Cockpit.

## Exercise 1.2 Guided Tour: Configure SAP Business Data Cloud in SAP for Me

Due to the technical and time limitations, we will use guided tours for activities in this class which takes long time and affect the whole shared landscape.

Guided tour is a pre-built, step-by-step interactive walkthrough within a product's demo environment, using tooltips, clear instructions, and highlighted features to lead prospects through key workflows and functionalities. When accessing a guided tour, please click the highlighted area to proceed to the next step.

Access the guided tour and follow the steps in SAP for Me.

During the guided tour, you will:

- Provision SAP Datasphere
- Provision SAP Analytics Cloud
- Create Formation and include systems
- Provision and include SAP Databricks

### Guided Tour: 
A guided tour is a clickthrough where the next click is pre-determined. The element to be explored next will be highlighted when you click anywhere on the screen.

<b>Start the tour [here](https://tour-viewer.platform.saleo.io/0e902660-fbc8-4d3f-888d-2470b23a80d3). </b> Explanations are provided below to help you understand the exercise.

### Explanations: 
> [!Note]
> The explanation section is optional reading material. Please feel free to skip this section if the guided tour was sufficient.

#### SAP for Me

In the SAP for Me account, under the **Portfolio & Products** Tab, under **My product suite** section, the tile **SAP Business Data Cloud** tile is visible since the product has been purchased and the commercial entitlement for SAP Business Data Cloud also exists in your URM organization. By clicking it, you can explore all the technical entitlements, also known as Eligibilities. that is, the set of eligible applications that are part of the BDC product.

<img src="images/sap4me-images/sap4me-entry.png" alt="internalHost" width="1500"/><br/>

You can go through the **Applications**, **Solutions**,**Resources** and **Customer Landscape** tabs to check the details of your BDC.

#### Create Resource Group
In a SAP Business Data Cloud Landscape, other than the data source systems, other products can be provisioned to leverage the different capabilities that are provided. To start provision these systems, we need to first create a resource group to group them together.

In the Resources tab, choose the *Create*, to create a resource group in your BDC.

#### Provisioning of SAP Datasphere and SAP Analytics Cloud

SAP Datasphere is the runtime where the data products can be installed and then enhanced.

Let's look at the example provisioning of SAP Datasphere.

1. In the Applications tab, choose the *Start Provisioning* for the SAP Datasphere application. A provision wizard will appear and guide you through the provision process.

2. Once the provisioning request is created, you can explore the solution and tenant resources that were just created for the app. Information on each resource is displayed, including the allocated quota and the status. Finally, you can launch the provisioned application. <b> The provisioning of the SAP Datasphere is successful.</b> <br/>

3. In the same way SAP Analytics Cloud can also be provisioned for leveraging them in the BDC landscape.

#### Creating a Formation
Formations allow you to combine SAP solution systems to simplify the connectivity setup and to provide a unified view of all components required for the implementation of your integration or enhancement scenario. Let us now look into the process of creating an SAP Business Data Cloud Formation.

1. **Customer Landscape > Systems** tab lists all the systems that are available or linked to the SAP For Me account. You can add specific systems to the Formation. To create a Formation, navigate to the **Customer Landscape > Formations** tab and select **Create Formation**.

2. Assign a meaningful name to the Formation and select the Formation type as **Integration with SAP Business Data Cloud**. Choose Next.

3. A specific order needs to be followed while creating the Formation. The sequence is as follows:
    - Add the newly activated SAP Business Data Cloud into the Formation first and create the Formation.
    - To the newly created Formation, add the systems in the following order:
        1. SAP Datasphere
        2. S/4HANA PCE system
        3. SAP Analytics Cloud

4. Review and finish the setup. The Formation is now in **Synchronizing** state. Once the Formation is in **Ready** state, SAP Business Data Cloud tenant is ready for use.
<img src="images/sap4me-images/formationSynchronizing.png" alt="formationSynchronizing" width="1500"/><br/>

#### Provisioning of SAP Databricks and include it into formation
After a formation is created, we can start provision SAP Databricks. 
In the Applications tab, choose the *Start Provisioning* for the SAP Databricks application. A provisioning wizard will appear and guide you through the provision process.
You will need to jump to Databricks homepage to activate the Databricks service.

After the provision of SAP Databricks, we need to switch to **Customer Landscape** to include the newly created SAP Databricks to our formation.

## Summary

In Exercise 1, you learned how to provision an SAP Business Data Cloud (BDC) tenant using SAP for Me. The exercise guides you through the foundational steps for enabling the SAP Business Data Cloud Cockpit, creating resource groups, and provisioning related applications such as SAP Datasphere, SAP Analytics Cloud, and SAP Databricks. You also followed a guided tour to configure BDC and learned how to create and manage formations that bring together different SAP systems to support integration and enhancement scenarios.


Continue to - [Exercise 2 - Administration Tools in SAP BDC cockpit](../ex2/README.md)

