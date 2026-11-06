# Share Data Products with Zero Copies using SAP Business Data Cloud Connect

Discover how to share data products across the SAP Business Data Cloud solution and third-party platforms with zero-copy access. In this session, you will learn about SAP Business Data Cloud (SAP BDC) and how the BDC Connect capability enables secure, bidirectional sharing of semantically rich data products with external platforms (here: Snowflake) without duplicating or moving data. You will see how zero-copy sharing preserves business context, governance, and metadata across environments, and walk through the end-to-end flow: from discovering data products in the BDC Catalog, to sharing them with a connected partner system via Delta Sharing, to consuming them directly in the target platform. Whether you are a data architect, analytics lead, or IT decision-maker, this session will show you how to break down data silos while keeping your trusted SAP data in place.


## Getting Started
In this Hands-on, you will explore a SAP BDC use case where you learn how to share and consume data products.

Some of the activities within the end-to-end use case are one-time activities. Hence, this session is a combination of Product tours, reading material and Hands-on. You will use the following labels throughout the exercises to categorize them:</br>

<b>Read-only:</b> Content tagged as 'Read-only' is reading material for you to better understand certain components and processes.</br>
<b>Guided Tour:</b> Content tagged as 'Guided-tour' are pre-defined clickthroughs designed in an environment mimicing the product truth. These clickthroughs will guide you through the real process to get a better understanding of one-time but essential configuration activities and features.</br>
<b>Hands-on:</b> Content tagged as 'Hands-on' are steps that you can perform in the tenant provided to you. Some steps in the process flow can be performed by you to gain a full working understanding.</br>

<b>Please check the label on the exercise before you begin.</b> 

## Use case Description
S/4HANA procurement data products are shared from SAP BDC to Snowflake via BDC Connect, enriched using SQL-based statistical anomaly detection to flag purchase order line items with unusual pricing, and published back to the BDC Catalog as a governed, enriched data product ready for downstream consumption in SAP Datasphere. Walk through the end-to-end flow — from zero-copy sharing and ML enrichment to custom data product creation — and see how procurement teams can answer questions like "Which purchase orders have pricing anomalies that need immediate review?" directly from trusted, context-rich SAP data.

<br>![Use Case](/exercises/ex0/images/useCase.png)

The exercises are as follows:
- [Exercise 1 - Provision SAP BDC Connect and include Enterprise Snowflake in a SAP BDC Formation](../ex1/README.md)
- [Exercise 2 - Install SAP-managed Data products from SAP BDC Catalog into Snowflake Horizon Catalog using SAP BDC Connect](../ex2/README.md)
- [Exercise 3 - Consume SAP-managed Data product in Enterprise Snowflake](../ex3/README.md)
- [Exercise 4 - Create and publish custom derived data product in Enterprise Snowflake using CoCo Agent](../ex4/README.md)
- [Exercise 5 - Install custom data product in SAP Datasphere](../ex5/README.md)

## Access to Tenants
- [SAP Business Data Cloud Cockpit](https://trial-bdc-core-3.eu10.hcs.cloud.sap/bdc-ui/index.html)
- [SAP Analytics Cloud](https://trial-bdc-sac-3.eu10.sapanalytics.cloud/)
- [SAP Datasphere](https://trial-bdc-datasphere-3.eu10.hcs.cloud.sap/)
- [Snowflake](https://6d0992e5-7283-4685-a3c8-4c4f7289eb0a.sharing.hdl.prod-eu10.hanacloud.ondemand.com/)

ObS2fy3Rd11!