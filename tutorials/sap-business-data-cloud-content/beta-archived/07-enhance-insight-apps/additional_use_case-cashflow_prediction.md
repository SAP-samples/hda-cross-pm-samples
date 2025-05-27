# Enhance Intelligent Application - Cashflow Prediction

## Persona 

Actor: <br/>
<img src="../resources/images/business_analyst.png" alt="Business Analyst" width="100"/>

Stakeholder:
<br/>
<img src="../resources/images/business_user.png" alt="Business User" width="100"/>

## Use Case
In the [previous additional exercise](../06-enhance-analytic-model/additional_use_case-cashflow_prediction.md), you created an Analytic model for the cash flow predicted using Databricks. 
You add this model to the story in SAP Analytics Cloud to fulfill the reporting needs of your business users. 

# Prerequisites
* SAP Analytics Cloud User Permissions: 
    - Modeler

## Steps

1. Open the story created in [the previous exercise](../07-enhance-intelligent-applications/README.md). Switch to ***edit*** mode.
<img src="./images/edit_story_2.png"  width="1000"/>

2. Add a new chart.
<img src="./images/insert_chart_2.png"  width="1000"/>

3. The chart should display data of the new created Analytic Model ***AM Databricks Cashflow Prediction*** (***AM_Databricks_Cashflow_Prediction***). Switch the data source accordingly.
<img src="./images/select_model_3.png"  width="1000"/>

4. Select the space in Datasphere in which  ***AM Databricks Cashflow Prediction*** was created.
<img src="./images/select_model_4.png"  width="1000"/>

5. Define the following for the new chart:
- Currently Selected Chart: ***Line***
- Left Y-Axis: ***forecast***, ***upper_forecast***, ***lower_forecast***
- Dimensions: ***date***
<img src="./images/select_measures.png"  width="1000"/>

6. To minimize white space in the chart, optimize the axis range. 
<img src="./images/edit_axis.png"  width="1000"/>

7. Set the minimum and maximum axis values dynamically. By this, you can eliminate more of the before empty space.
<img src="./images/dynamically_min_max.png"  width="1000"/>

8. The prediction now displays the forecasted cash flow, as well as the forecasted lower and upper ranges.
<img src="./images/add_header_scaling.png"  width="1000"/>

9. To allow filtering across all charts, add a new model link. 
<img src="./images/add_model_link.png"  width="1000"/>

10. Select the recently added model ***AM_Databricks_Cashflow_Predict*** and ***Cash_Flow_Forecast_Model***. Match the dimension ***Company Code*** and click ***Set***.
<img src="./images/link_dimensions_settings.png"  width="1000"/>

11. Do the same for  ***AM_Databricks_Cashflow_Predict*** and ***Cash_Flow_Actuals_Model***. Confirm the settings and confirm with ***Done***.
<img src="./images/linking_confirm.png"  width="1000"/>

12. Save the story.

13. Switch to ***View*** mode. Select a company code in the cluster chart, the other charts will be filtered according to the selection.
<img src="./images/cash_flow_story_view.png"  width="1000"/>

You have now enhanced the customized story with the cash flow predictions created in Databricks.

## Next steps
Continue with the [use case about native data integration capabilities](../09-native-data-integration/README.md).