# Getting Started (5 min)

SAP Business Data Cloud from Setup to Streamline: Practical Walkthrough.

In this exercise, you will explore the core components of SAP Business Data Cloud, learn how to activate and manage them, and practice strategies to streamline data integration, governance, and access.

Some of the activities required for the complete instantiation of an SAP BDC tenant are one-time actions. Hence, this session is a combination of Product tours, reading material and Hands-on. We will use the following labels throughout the exercises to categorize them:
- **Read-only**: Content tagged as 'Read-only' is reading material for you to better understand certain components and processes.
- **Guided Tour**: Content tagged as 'Guided-tour' are pre-defined clickthroughs designed in an environment mimicing the product truth. These clickthroughs will guide you through the real process to get a better understanding of one-time but essential configuration activities and features.
- **Hands-on**: Content tagged as 'Hands-on' are steps that you can perform in the tenant provided to you. Some steps in the process flow can be performed by you to gain a full working understanding.
- **Explanations**: This is optional reading if you want to gather more context for the guided-tour sections.

To proceed effectively with the subsequent exercise, let's first review some basic information regarding SAP Business Data Cloud. 

## What is SAP Business Data Cloud?

SAP Business Data Cloud is a fully managed SaaS solution that unifies and governs all SAP data and seamlessly connects with third-party data—giving line-of-business leaders context to make even more impactful decisions. Built as part of SAP’s broader data and analytics strategy, BDC is designed to bring together both SAP and non-SAP data sources into a single, trusted environment. By harmonizing enterprise data and embedding governance frameworks, it ensures accuracy, consistency, and compliance, thereby reducing the risks often associated with fragmented data landscapes.

SAP Business Data Cloud was launched at SAP Business Unleashed on Feb 13, 2025, and is now generally available.

## What are the core components of SAP Business Data Cloud formation?

A formation is used to connect a group of application tenants together into a virtual BDC landscape. Formations allow you to combine SAP solution systems to simplify the connectivity setup and to provide a unified view of all components required for the implementation.

Every SAP BDC Formation can include:
- One SAP Business Data Cloud Cockpit
- Zero or more SAP S/4HANA PCE systems
- Zero or more SAP SuccessFactors HCM systems
- Zero or one SAP Datasphere
- Zero or one SAP Analytics Cloud
- Zero or more SAP Databricks
- Zero or more SAP BW PCE (via SAP Datasphere)

### SAP Business Data Cloud Cockpit:

A unified management interface for administering BDC: browse/install Intelligent Apps, manage data products, monitor integrations (e.g., with Databricks), and oversee system health.

### S/4HANA Private Cloud Edition System:

SAP S/4HANA plays a significant role in the SAP Business Data Cloud (BDC) ecosystem, primarily as a source of enterprise data that can be leveraged for advanced analytics and business intelligence for Core ERP. 

### SAP SuccessFactors:
A people analytics solution is offered within SAP BDC which automatically transforms people, skills, and business data – from SAP SuccessFactors HCM and beyond – into readily available insights to help drive better people and business decisions.

### SAP Datasphere:

Functions as the data integration and modeling layer, provides a unified semantic model with governance, enabling users to work in business terms rather than raw data tables.

### SAP Analytics Cloud:

Delivers analytics, reporting, dashboards, and enterprise planning—all in one platform—facilitating interactive insights and scenario modeling.

### SAP Databricks:

Brings advanced AI, machine learning, and data science capabilities by enabling seamless access to SAP and third-party data without complex data replication.

### SAP BW PCE:

SAP BDC offers the flexibility and capability to expose SAP BW data in a modern data fabric environment. One can lift their SAP BW NetWeaver or SAP BW/4HANA on-premise deployments as-is into the private cloud component of SAP BDC. With the newly introduced component Data Product Generator for SAP BDC, creation of BW data products based on selected BW data can be carried out.

## Summary

Now that you have a good understanding of the different components within SAP BDC, let's get started with the first exercise.

Continue to - [Exercise 1 - Provision BDC via SAP for Me](../ex1/README.md)
