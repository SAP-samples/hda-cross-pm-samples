# SAP Business Data Cloud Enablement

:warning: **Please note that not all use cases have been directly tested end-to-end by the authors. Some of the information presented was gathered from various cluster teams and is based on second-hand knowledge. If you have feedback to improve the content, please get in touch with [Neetha Pucknat](https://github.tools.sap/D072636).**

:lock: **Content in this repository is strictly confidential. Do not share any information outside of the Beta program. Since this repository is on internal Enterprise GitHub, no access will be provided to the SAP BDC Beta customers directly.** <br>

:warning: **The current use case descriptions are based on the scope for Beta. The content is subject to change due to ongoing development.** <br>

This repository contains the enablement material for SAP Business Data Cloud. The exercises are targeted towards SAP Business Data Cloud end-user personas. It describes responsibilities of the different personas that range from business users to system administrators. Each of the chapters describes which persona(s) it addresses.


## Use Cases Description

<table style="wdith:100%">
<thead>
<tr>
<th style="width:30%">Topic</th>
<th style="width:70%">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1. Basic Configuration of SAP Business Data Cloud</td>
<td>
  <ul>
  <li>Prerequisites in SAP Datasphere and SAP Analytics Cloud</li>
  <li>Configuration of the SAP BDC Cockpit</li>
  <li>S/4HANA PCE Configuration</li>
  <li>SAP Cloud Connector Configuration for SAP BDC and S/4HANA PCE integration</li>
  <li>Formation Creation</li>
  <li>Preparation of S/4HANA PCE connection for use in SAP Datasphere spaces</li>
</ul>
​ </td>
</tr>
<tr>
<td>2. Installation of Intelligent Applications</td>
<td>
  <ul>
  <li>Intelligent Applications are one of the most important key highlights which are all SAP managed</li>
  <li>Onboard Intelligent Applications easily via the SAP BDC Cockpit</li>
  <li>Assign users to the deployed content</li>
</ul>
</td>
</tr>
<tr>
<td>3. Consumption of Intelligent Applications</td>
<td>

<ul>
  <li>Work with out-of-the-box SAP managed Intelligent Applications & have a detailed look into the delivered dashboard </li>
  <li>Learn how you can reduced time to value due to reduction of time to gather required datasets, building data models and stories to derive data insights.​</li>
</ul>

 </td>
</tr>
<tr>
<td>4. Activating Data Packages in Business Data Cloud Cockpit & Installing Data Products in Datasphere</td>
<td>

<ul>
  <li>Many customers will use data products to build their own Analytic Model or a Customer Managed Intelligent Application on top. </li>
  <li>By onboarding a 	data 	package, all assigned data products can be easily deployed in SAP Datasphere to build a strong data foundation.​</li>
</ul>
​ </td>
</tr>
<tr>
<td>5. Enrich Data Products with ML Capabilities leveraging Databricks</td>
<td> 

<ul>
  <li>Goal of this use case: use an existing data product as a source for ML/AI scenarios</li>
  <li>This use case shows how easy it is to exchange data with Databricks and to consume an ML model from Databricks as a data product in SAP Datasphere​ </li>
</ul>
</td>
</tr>
<tr>
<td>6. Enhance an Analytic Model</td>
<td> 

<ul>
  <li>Many customers for sure have to extend / change SAP managed data products due to different processes and customizations</li>
  <li>Extensions are added to the Analytic Model in SAP Datasphere to test the overall data model provisioning experience</li>
  </ul>

 ​</td>
</tr>
<tr>
<td>7. Enhance an Intelligent Application</td>
<td>
<ul>
  <li>After the enhancement of the Analytic Model in SAP Datasphere, it’s necessary to enhance the Intelligent Application for a Business User to gain insights. </li>
  </ul>
 ​</td>
</tr>
<tr>
<td>9. Native Integration Capabilities</td>
<td>  ​</td>
</tr>
<tr>
<td>10. BW Modernization Story</td>
<td>  ​</td>
</tr>
<tr>
<td>11. SAC - Just Ask</td>
<td>  ​</td>
</tr>
<tr>
<td>12. SAC - Planning</td>
<td>  </td>
</tr>
<tr>
<td>13. Access Data Products of Customized S/4HANA CDS Views</td>
<td> 
<ul>
  <li> This chapter does not contain an exercise yet, but describes the behavior when working with customizations in S/4HANA PCE.  </li>
  </ul>
 ​</td>
</tr>
</tbody>
</table>

## Disclaimer
The use cases described in this repository do not take potential data quality issues into account.

The results will be best presented if and only if: 
- there is a unique global currency (column name: *GlobalCurrency*)
- there is only one global currency per company code. (column name: *CompanyCodeCurrency*)

If there are multiple global currencies and multiple currencies per company code, then please note that a currency conversion may need to be performed to yield better results as outcome of the exercises.


## Use Cases Status

<table style="wdith:100%">
<thead>
<tr>
<th style="width:30%">Topic</th>
<th>Beta Use Cases</th>
<th>Status Beta</th>
<th>Beta</th>
<th>Reponsib.</th>
<th>Reviewed by</th>
</tr>
</thead>
<tbody>
<tr>
<td>1. Basic Configuration of SAP Business Data Cloud</td>
<td>:white_check_mark: </td>
<td>:white_check_mark:</td>
<td><a href="01-basic-config-bdc/README.md">link</a></td>
<td><a href="https://github.tools.sap/D072636">Neetha Pucknat</a></td>
<td> Bernd Krannich, Lukas Hudelmayer, Zili Zhou</td>
</tr>
<tr>
<td>2. Installation of Intelligent Applications</td>
<td>:white_check_mark: </td>
<td>:heavy_check_mark:</td>
<td><a href="02-install-intelligent-applications/README.md">link</a></td>
<td><a href="https://github.tools.sap/D072636">Neetha Pucknat</a> /  <a href="https://github.tools.sap/I501282">Faranak Rezaei Estabragh</a></td>
<td><a href="https://github.tools.sap/D033968">Rituparna Reddi</a></td>
</tr>
<tr>
<td>3. Consumption of Intelligent Applications</td>
<td> :white_check_mark: </td>
<td>:heavy_check_mark:</td>
<td><a href="03-consuming-intelligent-applications/README.md">link</a></td>
<td><a href="https://github.tools.sap/D072636">Neetha Pucknat</a> / <a href="https://github.tools.sap/I501282">Faranak Rezaei Estabragh</a></td>
<td><a href="https://github.tools.sap/D033968">Rituparna Reddi</a></td>
</tr>
<tr>
<td>4. Activating Data Packages in Business Data Cloud Cockpit & Installing Data Products in Datasphere</td>
<td> :white_check_mark: </td>
<td>:white_check_mark:</td>
<td><a href="04-onboard-data-products/README.md">link</a></td>
<td><a href="https://github.tools.sap/D067558">Nikola Braukmueller</a></td>
<td><a href="https://github.tools.sap/D033968">Rituparna Reddi</a></td>
</tr>
<tr>
<td>5. Enrich Data Products with ML Capabilities leveraging Databricks</td>
<td>:white_check_mark:  </td>
<td>:hourglass_flowing_sand:</td>
<td><a href="./beta-pipeline/05-enrich-data-products-with-databricks-ml/README.md">link</a></td>
<td><a href="https://github.tools.sap/D070547">Martin Boeckling</a></td>
<td> </td>
</tr>
<tr>
<td>6. Enhance an Analytic Model</td>
<td> :white_check_mark: </td>
<td>:white_check_mark:</td>
<td><a href="06-enhance-analytic-model/README.md">link</a> (<a href="06-enhance-analytic-model/README.md">link</a> for availability of Databricks Integration :hourglass_flowing_sand:)</td>
<td><a href="https://github.tools.sap/D067558">Nikola Braukmueller</a> / <a href="https://github.tools.sap/D031643">Axel Meier</a></td>
<td> <a href="https://github.tools.sap/D033968">Rituparna Reddi</a> </td>
</tr>
<tr>
<td>7. Enhance an Intelligent Application</td>
<td>:white_check_mark:  </td>
<td>:white_check_mark:</td>
<td><a href="07-enhance-intelligent-applications/README.md">link</a></td>
<td><a href="https://github.tools.sap/D067558">Nikola Braukmueller</a> / <a href="https://github.tools.sap/D031643">Axel Meier</a></td>
<td><a href="https://github.tools.sap/I051279">Laura Vega</a</td>
</tr>
<td>9. Native Integration Capabilities</td>
<td> :heavy_plus_sign: </td>
<td>:white_check_mark:</td>
<td><a href="09-native-data-integration/README.md">link</a></td>
<td><a href="https://github.tools.sap/I553687">Rithivika Archarya</a></td>
<td><a href="https://github.tools.sap/I540987">Sandy Tran</a></td>
</tr>
<tr>
<td>10. BW Modernization Story</td>
<td> :heavy_plus_sign: </td>
<td>:white_check_mark:</td>
<td> <a href="09-native-data-integration/README.md">link</a></td>
<td> <a href="https://github.tools.sap/D030516">Heiko Schneider</a> </td>
<td><a href="https://github.tools.sap/I540987">Sandy Tran</a></td>
</tr>
<tr>
<td>11. SAC - Just Ask</td>
<td>:x: </td>
<td>:hourglass_flowing_sand:</td>
<td><a href="beta-pipeline/11-sac-just-ask/README.md">link</a></td>
<td> <a href="https://github.tools.sap/D054984">Constantin Leyh</a> </td>
<td><a href="https://github.tools.sap/I051547">Francois Imberton</a>/<a href="https://github.tools.sap/I837895">Flavia Moser</a></td>
</tr>
<tr>
<td>12. SAC - Planning</td>
<td>:x:  </td>
<td>:construction:</td>
<td><a href="beta-pipeline/12-sac-planning/README.md">link</a></td>
<td><a href="https://github.tools.sap/D023312">Georg Meier</a></td>
<td><a href="https://github.tools.sap/D058058">Maximilian Gander</a></td>
</tr>
<tr>
<td>13. Access Data Products of Customized S/4HANA CDS Views</td>
<td>:heavy_plus_sign: </td>
<td>:white_check_mark:</td>
<td>tbd</td>
<td><a href="https://github.tools.sap/D067558">Nikola Braukmueller</a> / <a href="https://github.tools.sap/D031643">Axel Meier</a></td>
<td><a href="https://github.tools.sap/D041515">Jörg Franke</a></td>
</tr>
</tbody>
</table>

### Legend
:white_check_mark: finished and reviewed <br>
:hourglass_flowing_sand: use case documented but E2E flow not available yet <br>
:heavy_plus_sign: additional reading matarial / use case <br>
:heavy_check_mark: finished (with information available as of now, minor adjustments might be open) <br>
:construction: in progress <br>
:o: open, not started yet <br>



