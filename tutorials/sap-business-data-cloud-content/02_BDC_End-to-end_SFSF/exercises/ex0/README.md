# Transform business data into AI-supported insights

Discover how to share data products across the SAP Business Data Cloud solution and third-party platforms with zero-copy access. In this session, you will learn about SAP Business Data Cloud (SAP BDC) and how the BDC Connect capability enables secure, bidirectional sharing of semantically rich data products with external platforms (here: Snowflake) without duplicating or moving data. You will see how zero-copy sharing preserves business context, governance, and metadata across environments, and walk through the end-to-end flow: from discovering data products in the BDC Catalog, to sharing them with a connected partner system via Delta Sharing, to consuming them directly in the target platform. Whether you are a data architect, analytics lead, or IT decision-maker, this session will show you how to break down data silos while keeping your trusted SAP data in place.

## Getting Started
In this Hands-on, you will explore an end-to-end SAP BDC use case.

Some of the activities within the end-to-end use case are one-time activities. Hence, this session is a combination of Product tours, reading material and Hands-on. You will use the following labels throughout the exercises to categorize them:</br>

<b>Read-only:</b> Content tagged as 'Read-only' is reading material for you to better understand certain components and processes.</br>
<b>Guided Tour:</b> Content tagged as 'Guided-tour' are pre-defined clickthroughs designed in an environment mimicing the product truth. These clickthroughs will guide you through the real process to get a better understanding of one-time but essential configuration activities and features.</br>
<b>Hands-on:</b> Content tagged as 'Hands-on' are steps that you can perform in the tenant provided to you. Some steps in the process flow can be performed by you to gain a full working understanding.</br>

<b>Please check the label on the exercise before you begin.</b> 

## Use case Description
A leading enterprise seeks to harness workforce intelligence by integrating SAP SuccessFactors data with advanced ML capabilities on Snowflake. Ten curated data products — sourced from SAP Business Data Cloud — are federated into Snowflake, establishing a governed, analytics-ready foundation. Two Snowflake Cortex ML workflows are applied: ML.CLASSIFICATION segments employees into transformation readiness tiers, while ML.FORECAST projects 12-month learning completion trajectories at the department level. The resulting enriched dataset is packaged as a custom data product and published back to the SAP BDC Catalog, ensuring discoverability and reusability across the enterprise. Business stakeholders consume the insights through SAP Analytics Cloud dashboards, enabling HR and L&D leaders to make data-driven decisions on workforce upskilling and change readiness at scale.

<br>![Use Case](/exercises/ex0/images/useCase.png)

The exercises are as follows:
- [Exercise 1 - Share SAP-managed Data products from SAP BDC Catalog to SAP Snowflake Horizon Catalog](../ex1/README.md)
- [Exercise 2 - Consume SAP-managed Data product in Enterprise Snowflake and run ML Workflows](../ex2/README.md)
- [Exercise 3 - Create and publish custom derived data product in SAP Snowflake to SAP BDC Catalog using CoCo Agent](../ex3/README.md)
- [Exercise 4 - Install custom data product in SAP Datasphere](../ex4/README.md)
- [Exercise 5 - Consume and model custom data product in SAP Datasphere](../ex5/README.md)
- [Exercise 6 - Create a report in SAP Analytics Cloud](../ex6/README.md)
- [Exercise 7 - Bonus: Data & Analytics Insights Agent](../ex7/README.md)

## Access to Tenants
- [SAP Business Data Cloud Cockpit](https://trial-bdc-core-3.eu10.hcs.cloud.sap/bdc-ui/index.html)
- [SAP Analytics Cloud](https://trial-bdc-sac-3.eu10.sapanalytics.cloud/)
- [SAP Datasphere](https://trial-bdc-datasphere-3.eu10.hcs.cloud.sap/)
- [SAP Snowflake](https://188ec0ba-2073-4fff-9922-b677717b7e9a.sharing.hdl.prod-eu20.hanacloud.ondemand.com/)
