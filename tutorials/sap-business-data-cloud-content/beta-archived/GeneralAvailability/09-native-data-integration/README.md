# Native Data Integration 

:construction_worker: tbd <br>

## Persona 
Actor:

Stakeholder:

## Use Case
This chapter demonstrates how customers can integrate data which is not available as a data product in Business Data Cloud.
It is a common use case that customers have custom CDS views, these won't be released as a data product. Secondly, it might be the case that the required data from S/4HANA is not available as a data product yet as development to increase the amount of data products available is ongoing from SAP side. 


## Knowledge Basis
* - [DSP - Semantic Onboarding with Replication Flows](https://sap.sharepoint.com/sites/126676/_layouts/15/stream.aspx?id=%2Fsites%2F126676%2FContent%20Overview%2FData%20Warehouse%2FCluster%20Page%20%2D%20Content%2FProduct%20Sites%2FSAP%20Datasphere%2FWhat%27s%20new%20in%20Datasphere%2F2024%2FRelease%202024%2E11%2D13%2F2024%2E13%20Import%20Meta%20Data%20Wizard%20%2D%20Using%20APE%20for%20S4HANA%20on%20Premise%20connections%20%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E2485da60%2Dec30%2D4f9b%2D88ed%2D8d96e2917d18) 

## Prerequisites
* BDC Customer
* S/4HANA PCE (Model Import to import semantics (Replication Flows) available if the connected system is SAP S/4HANA 2021 or higher (SAP_BASIS 756 and higher))

## Steps
1. Use Case: We have one CDS view which we want to access. 
2. There is no data product available containing this data (we, SAP, can check in the Git - customer should check in the catalog that there is no data product entry 
    -> No active but also no inactive data product (if it is inactive it could be installed in the BDC cockpit) 
3. Use the Semantic Onboarding capability to import semantically-rich entities from an SAP S/4HANA PCE.
4. Import a CDS view which has dependency on additional entities 
5. Semantic Onboarding creates a Replication Flow which replicates the CDS view + dependent entities (You can also create a Replication Flow by your own... Advantage of semantic onboarding is that you got that the dependent entities out of the box)
6. Either you work in the current space or you can share the entity with a different space

(7. If we want to show analytical modeling on top of the integrated data, we either describe the steps or could provide a CSN model to users to import. / Maybe combine with 06 Enhance Analytic Model)


-> Additional Deep Dive: Maybe talk about replication and federation?
-> maybe no detailed steps, but mention 3rd party integration capabilities : Access data from 3rd party solution (Microsoft SQL))

(3. Show how to use the embedded data lake in Datasphere? This will be the prerequisite to access the data in Databricks?)





