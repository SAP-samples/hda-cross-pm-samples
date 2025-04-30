# Access Data Products of Customized S/4HANA CDS Views
 
## Introduction
This chapter does not contain an exercise yet, but describes the behavior when working with customizations in S/4HANA PCE. 

## Current Understanding of S/4HANA PCE Customization Use Cases
We differentiate between two different scenarios:

### 1. Customer CDS views
Customer-created Z-CDS Views won't be represented as Data Products as of today.
It's required to use Datasphere standard data access options (federated and replicated data access).

### 2. Customer appended fields to CDS views
Customer appended fields to CDS views (clean core compatible) are automatically added and data gets processed to the according SAP Data Products. 
The SAP Data Products data and semantics are replicated to Datasphere / accessible using the Datasphere Data Builder Editors.   

SAP delivered Datasphere and SAC Insight-App artifacts are based on SAP standard configured CDS-Views.
Customer appended fields available by SAP Data Products are accessible for Datasphere Data Builder Editors. As of now, all extension fields are defaulted to String(128).
The Datasphere Insight-App artifacts can be customized or extended by the SAP Data Product provided customer- appended fields by copying the content to a customer-managed space and adapting the copied artifacts.   
