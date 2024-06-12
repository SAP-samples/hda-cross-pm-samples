# SAP Analytics Cloud Tailored Story

SAP Analytics Cloud, often abbreviated as SAC, is an all-in-one cloud platform that combines business intelligence (BI), planning, and predictive analytics into a single, unified solution. It's offered as a Software as a Service (SaaS), meaning you can access and use it through a web browser without needing to install or manage any software yourself. SAC can help businesses of all sizes make data-driven decisions, improve performance, and achieve their strategic goals as an intuitive easy-to-use solution that simplifies data analysis drastically.

SAP Analytics Cloud consumes data from SAP Datasphere via a live connection to create stories and analytic applications.

## Prerequisites
 - You have [imported your dataset into your Space.](../dsp_modeling_1-import-dataset/dsp_modeling_1-import-dataset.md)
 - You have [adjusted the Semantic Types and created Associations using the Entity-Relationship Model](../dsp_modeling_2-create-relationships/dsp_modeling_2-create-relationships.md)
 - You have [created a graphical view combining data about Sales Orders and Sales Order Items](../dsp_modeling_3-create-graphical-view/dsp_modeling_3-create-graphical-view.md)
 - You have [created an Analytic Model](../dsp_modeling_4-create-analytic-model/dsp_modeling_4-create-analytic-model.md)
 - You have [imported the Partner Workshop Story template into SAC](../dsp_analytics_1-import-template/dsp_analytics_1-import-template.md)

## You will learn
  - Prerequisites to create a live connection between SAP Analytics Cloud and Datasphere.
  - Creating a story accessing data from Datasphere.
  - Utilizing semantics and measures which have been defined in DSP before.
  - Using templates in order to speed up the process of creating corporate dashboards.
  - Tailoring the story to add interactivity and innovation with scripting and custom widgets.

---

### Get to know SAC Templates

One key aspect of an analytical solution is its ability to be used by different types of users regardless of the skills and background.

Typically, Analytics solutions, just like any other solution, come equipped with lots of features, menus, buttons, etc. that could make it complex for all the users to be able to get the most of out of the application. We live now in a world where ease of use, simplicity, efficiency are paramount. Therefore, it is indispensable that any complexity is made transparent to the final consumers, and you will experience now how easy it is to create and consume content leveraging SAC Templates.

SAC Templates are pre-designed layouts to help users quickly build impactful data visualizations and stories. By using SAC Templates users will:

- Create stories **faster** with a ready-made structure. User will only need to add a datasource to each widget (**chart**, **table**, **input control**...) in the template.
- Deliver **consistency** ensuring all stories follow the same corporate design standards.
- Use embedded scripting logic in a transparent way to speed up some basic tasks that otherwise would require additional cliks and skills. 

### Access SAP Analytics Cloud & Connectivity to Datasphere

1. If the product switch between SAP Datasphere and SAP Analytics Cloud has been configured, you can use the product switch button in the top right of the shell to easily navigate between both solutions. 

  ![SAC Connectivity](./images-dsp_analytics_3-create-tailored-story/DS_SAC_Switch.png)

2. In SAP Datasphere, the URL of the SAC system needs to be added as a **Trusted Origin** in `System->Administration->App Integration`.

  ![SAC Trusted Origin](./images-dsp_analytics_3-create-tailored-story/DS_SAC_TrustedOrigin.png)

3. In SAP Analytics Cloud, a live connection has been created so that data from SAP Datasphere can be accessed. You can validate this in the **Connections**.

  ![SAC Connections](./images-dsp_analytics_3-create-tailored-story/DS_SAC_Connections.png)

### Create a new Tailored Story

#### Preparing the canvas

1. In **Stories**, create a new story clicking directly on the template thumbnail `Partner Workshop Template`. 

    ![SAC Story Template](./images-dsp_analytics_3-create-tailored-story/DS_SAC_NewFromTemplate.png)

2. Click `Create`.

    ![SAC Story Template](./images-dsp_analytics_3-create-tailored-story/DS_SAC_DesignModeType.png)


3. Close the right panel to make room for the canvas by clicking on the `Close` button. You could use this panel to select a different layout if needed, but you don't have to do it for this exercise.

    ![SAC Story Template](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CloseLayout.png)

 4. Click on the `Outline` tab of the left panel to see all the widgets that are part of this template. You can use that view to select, hide/show and delete widgets, among other things. In this panel you also have direct access to the `Assets` and `Filters` tabs.

    ![SAC Story Template](./images-dsp_analytics_3-create-tailored-story/DS_SAC_Outline.png)

5. Close the left panel by clicking on the `X` sign. This way the whole screen will be available for the canvas.

    ![SAC Story Template](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CloseOutline.png)

#### Data Binding - Input Controls

Now you will start with the data binding widget by widget. As report designer and data consumer, the right information must be available at any time and filtering is a key capability that will enable to users to narrow down their analysis by selecting the exact data. **Input Controls** in SAP Analytics Cloud allow users to define both dimension and measure filters that can affect the whole story or just specific widgets.

 1. Click on `Create` on the Input Control on the top left.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_SelectInputControl1.png)

2. Select the connected Datasphere tenant. You see all spaces your Datasphere application user is allowed to access. Select your space and the Analytic Model that you created in the previous exercise, `AM_Sales_Report`.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_SelectModel2.png)
 
3. Click on `Dimensions`.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_DimensionsIC1.png)

4. Select `ADDRESSID`.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_SelectAddressID.png)

5. Select `REGION` and `Filter by Member`.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_SelectRegionMember.png)

6. Select `All Members` and click `OK`. Optionally, you can try the different options (Multiple/Single) available for the selection behavior in the bottom right dropdown box.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_SelectRegionAllMembers.png)

7. Repeat steps from **5** to **10** for the two remaining input controls using dimension `CREATEDAT` for the one in the middle and dimension `PRODUCTID` for the one at the bottom. For the `CREATEDATE` one, there is a slight change, you have to manually expand the **All  Members** tree, and select `2018` and `2019` values, and then select `Multiple Selection` on the bottom right dropdown box. See the picture below to confirm the configuration.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CreateDatIC.png)

#### Data Binding - Numeric Point Charts

1. Click on `Create a Numeric Point Chart` starting from the left.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CreateNumericPointChart.png)

2. Click on the `+` sign under **Primary Values**.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CreateNumericPointChartValue.png)

3. Select `NETAMOUNT` measure under **Measures**.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_NetAmount.png)

4. Now we can apply some **Styling** to the chart in order to increase readability. In order to do that, in the right panel, select `Styling` tab. Note: If the panel is not visible, select the `Right Side Panel` icon under the view **Menu** on the top bar.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_StylingTab.png)

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_StylingPanel.png)

5. In the **Styling** panel, scroll down until `Number Format` section and configure the `Scale` and `Decimal Places` as below screenshot.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_NumberFormat.png)

6. Now, you will hide the **Primary Value Label** as it is redundant. Select the chart, if not selected, and click on the `...` dots icon on top right of the chart, then in `More Options`, then `Show/Hide`, and finally untick `Primary Value Labels`

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_NPStylingHide.png)

7. **Optionally**, you can double click on the chart title and give it a more appropriate name.

8. Repeat steps from **13** to **19** for the rest of the numeric point charts using the following measures: `GrossAmount_Orders`, `TAXAMOUNT` and `QUANTITY`.

#### Data Binding - Bar Chart

1. Click on the `Create a Bar Chart` button.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CreateBarChart.png)

2. On the right panel, select **Measures** and **Dimensions** by clicking on `Add Dimension` and `Add Measure`, as per the screenshot below.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_BarChartDefinition.png)

3. To simplify analysis, you want the user to focus on the best performing countries. In order to add a **Ranking**, click on the `...` dots icon on top right of the chart, then in `Rank`, then `Country`, and finally `Top 5`.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_BarChartTop5.png)

#### Data Binding - Line Chart

1. Click on the `Create a Line Chart` button.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CreateLineChart.png)

2. On the right panel, select **Measures** and **Dimensions** by clicking on `Add Dimension` and `Add Measure`, as per the screenshot below.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_LineChartDefinition.png)

#### Data Binding - Table

Sometimes users need to perform detailed analysis and precise comparisons based on a detailed view of every data point, here is where the **Tables** come into play. You will configure the table widget now. 

1. Click on `Create a Table` button.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CreateTable.png)

2. On the right panel, move the following **Dimensions** to **Rows** by clicking on `Add Dimension` as per the screenshot below.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_TableRows.png)

3. Now move the following **Measures** to **Columns** by clicking on the `Funnel` icon inside the **Measures section** as per the screenshot below. Then click `OK` button.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_TableColumnsFilter.png)

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_TableColumns.png)

#### Data Binding - Geo Map

Now, you would like to be able to **identify geographic patterns** -like if certain products sell better in specific regions- , **understand location-based impacts** and *plan and optimize geographically dispersed operations* among other things. Tables and charts fail to provide such capabilities. However, by leveraging SAP Analytics Cloud **Geo capabilities** you will be able add a spatial dimension to your data analysis, leading to deeper insights, better communication, and data-driven decisions with strong regional context.

1. Click on `Create a Geo Map` button.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CreateGeoMap.png)

2. Click on `Add Layer`.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_GeoMapAddLayer.png)

3. Select `Location` dimension under **Location Dimension** section. 

4. Select `NETAMOUNT` measure under **Bubble Color** section. 

5. Switch `to Choropleth/Drill` using the dropdown box under **Layer Type** section.

6. The **Geo Map** configuration should look like this. 

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_GeoMapSelections.png)

7. Click on `Done` button on the bottom right to exit the Layer configuration panel.

#### Data Binding - Custom Pie Chart

1. Click on the **Bar Chart**. Then, go to **Outline** section of the left panel, and then click on the `Eye` icon beside the highlighted Chart. This will hide the chart on the canvas.

![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_HideBarChart.png)

2. Now, you have to make **Custom Pie Chart** visible. Go to **Outline** section of the left panel, and then click on the `Eye` icon beside the **CustomPie** widget.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CustomPieWidget.png)

3. Click on the `Create a Custom Widget` button.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_CreateCustomWidget.png)

4. On the right panel, select **Measures** and **Dimensions** by clicking on `Add Dimension` and `Add Measure`, as per the screenshot below.

    ![SAC Story Data Binding](./images-dsp_analytics_3-create-tailored-story/DS_SAC_DataBindingCustomPieChart.png)

#### Further customization of the SAC story

At this step, you are almost done with the **Story** design, however there are circumstances where a specific requirement is needed, and it cannot be covered with the standard functionality. Luckily, in SAP Analytics Cloud, there are two alternatives to provide additional customization capabilities.

- Adding **custom widgets** to create special visualizations to match user's requirements. Custom widgets let you extend the predefined set of widgets provided by SAP Analytics Cloud. You have seen this in the previous exercise.

- Adding some **scripting** to define a more complex logic to our dashboard. Scripting language is a limited subset of **Javascript**.

You will experience now how to apply **scripting logic** to SAC story widgets.

There are some buttons already available in the story template. Some of them have already defined scripting logic in order to make it simple to test the functionality. 

![SAC Story Scripting](./images-dsp_analytics_3-create-tailored-story/DS_SAC_ScriptEnabledButtons.png)

![SAC Story Scripting](./images-dsp_analytics_3-create-tailored-story/DS_SAC_ButtonExplorer.png) -> `Explorer` button open the **Data Analyzer** application in a new tab allowing the user to perform ad-hoc analysis without making an impact to the current story layout, and save the drill-down data state and analysis as insights.

![SAC Story Scripting](./images-dsp_analytics_3-create-tailored-story/DS_SAC_ButtonPdf.png) -> `Pdf` button exports the whole story to a **pdf** document.

![SAC Story Scripting](./images-dsp_analytics_3-create-tailored-story/DS_SAC_ButtonChart.png) -> `Chart` button allows the user to interactively switch from **Bar Chart** to **Custom Pie Chart** visualization.

`Pdf` and `Chart` buttons work without any change in the scripting code, however there are some adjustments required for `Explorer` button.

1. Click on the `...` dots menu of the `Explorer` button. And then, click on `Edit Scripts` -> `onClick`

    ![SAC Story Scripting](./images-dsp_analytics_3-create-tailored-story/DS_SAC_ButtonExplorerSetup.png)

2. Modify the scripting line like this.

NavigationUtils.openDataAnalyzer('`%Connection_Name%`','[`%SPACE%`][][`%Analytic_Model_Name%`]',UrlParameter.create("systemType","DATASPHERE"),true);

    Example: 

    NavigationUtils.openDataAnalyzer('DSP','[USER_SPACE][][AM_SalesReport]',UrlParameter.create("systemType","DATASPHERE"),true);

---

You have successfully created a fully customized story based on a SAC template where most of the layout was already defined following company's guidelines.