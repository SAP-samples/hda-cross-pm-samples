# Customize SAP Analytics Cloud Story of an Insight App

## Persona 

Actor:
 <br/>
<img src="../resources/images/business_analyst.png" alt="Business Analyst" width="105"/>

Stakeholder: <br/>
<img src="../resources/images/business_user.png" alt="Business User" width="100"/>

## Use Case
Insight Apps are SAP-managed. This means that any enhancements that need to performed have to performed on the copies of the content. You can duplicate the SAP managed asset to create and modify own assets. From then on, we refer to such assets as customer-managed assets.

## Overview
This exercise is separated into three sections:
- [Story Copy](#story-copy)
- [Modify and Enhance Copied Story](#modify-and-enhance-copied-story) (Prerequisites to share Data Products with Databricks or to install them in Datasphere.)

## Prerequisites
- SAP Analytics Cloud User Permissions: 
    - BI Admin role or another Admin role is required to view the tab **Insight Apps** under the **Files**. Hence, one of the admin roles is required to view and copy the Insight App.

## Steps

### Story Copy
1. Open the SAP Analytics Cloud tenant.

2. Navigate to ***Files*** -> ***Insight Apps*** inside of the SAP Analytics Cloud file repository.
<img src="./images/sac_file_repo.png"  width="1000"/>

3. Select the folder ***SAP Managed IA*** and click the ***copy*** button.
<img src="./images/sac_copy.png"  width="1000"/>

4. Navigate to the ***Public*** folder. Create a new folder **Copy Insight App - YOURUSERID**.
<img src="./images/create_folder.png"  width="1000"/>

5. Add "Copy" to the name and description, select ***Copy*** afterwards.
<img src="./images/copy_file.png"  width="1000"/>

### Modify and Enhance Copied Story

1. Open the copied story in edit mode.
![alt text](BDC_enhance_IApp/2025-04-15_12-18-09.png)

2. Select the ***Liquidity & Cash*** tab and duplicate the ***Cash Flow*** dashboard
![alt text](BDC_enhance_IApp/2025-04-15_12-12-50.png)

3. Rename it to ***Cash Flow Clustering by Company Code***
![alt text](BDC_enhance_IApp/2025-04-15_12-15-55.png)

4. Click ***Tools*** -> ***Add new data***, 
![alt text](BDC_enhance_IApp/2025-04-15_12-19-00.png)


5. Click on ***Data from an existing dataset or model***
<br>![alt text](BDC_enhance_IApp/2025-04-15_12-19-48.png)</br>

6. Click on ***Select other Model***
![alt text](BDC_enhance_IApp/2025-04-15_12-20-25.png)

7. Navigate to the folder where you saved your enhanced analytic model and select it
![alt text](BDC_enhance_IApp/2025-04-15_12-32-49.png)

8. A warning is displayed that replacing a model will impact story settings, click ***OK***.
![alt text](BDC_enhance_IApp/2025-04-15_14-56-26.png)

9. Select the ***Clustering Cash Flow by Company Code*** dashboard and replace the existing model by the enhanced one you imported in the steps above.
![alt text](BDC_enhance_IApp/2025-04-15_14-56-58.png)

10. Select from the list your previously added model ***Enhanced_AM***.
![alt text](BDC_enhance_IApp/2025-04-15_14-57-26.png)

11. Insert a new chart.
![alt text](BDC_enhance_IApp/2025-04-15_13-14-00.png)

12. Configure the scatterplot by selecting measures and dimensions as displayed in the screenshot below.
![alt text](BDC_enhance_IApp/2025-04-15_15-03-33.png)

13. Save the story.

14. Open the preview for the story.
![alt text](BDC_enhance_IApp/2025-04-15_13-36-44.png)

15. Filter for a dedicated company code.
![alt text](BDC_enhance_IApp/2025-04-15_13-38-03.png)

You have successfully copied the story and re-pointed to the Analytic Model within the copied space.

## Next Steps
As you are using mock data, skip the [additional use case](./additional_use_case-cashflow_prediction.md) for now which explains how to add the new Analytic Model ([previous description](../06-enhance-analytic-model/additional_use_case-cashflow_prediction.md)) in the SAP Analytics Cloud story.
Continue with the [use case about native data integration capabilities](../09-native-data-integration/README.md).
