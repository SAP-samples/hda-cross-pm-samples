# Exercise 6- Customization of Intelligent Application - Initiate

As explored in the previous exercises, the SAP BDC Admin is crucial for installing and configuring the Intelligent Applications. In this exercise, we will learn how the SAP BDC Admin initiates the customization of the Intelligent Application. To customize an SAP-managed Intelligent Application, we have to first copy the SAP-managed version into its custom-managed counterparts.

As we know, the analytic Intelligent Application is comprised of the following:
- SAP-managed data products
- Analytic Model and its underlying views and table in SAP Datasphere
- Stories for reporting in SAP Anayltics Cloud

For the customization, one would need to copy the spaces in SAP Datasphere and the story in SAP Analytics Cloud into custom-managed versions. It is in the custom-managed versions is where the customization can be performed.

In this exercise, we will continue with Working Capital Insights as basis. The exercise is divided into two parts:
- Copy the SAP Datasphere spaces below
    * SAP_WCI
    * SAP_S4H
- Copy the SAP Analytics story which under the package and Location below
    * SAP_SAC_WCI: INSIGHT_APPS / SAP S/4HANA / Finance

## Exercise 6.1 Read-only: SAP Datasphere Space Copy
> [!Note]
> This part of the exercise cannot be performed in the system. The space required to perform the exercises has already been provided to you. Your space is a condensed version of everything required for the customization exercise. This section shows how an SAP BDC Admin performs the copying of the spaces.

> [!IMPORTANT]
> This steps DO NOT need to be performed. Your space has already been provided to you. The following image shows the space already provided to you.
<br>![space](/exercises/ex6/images/03_your_space.png)

1. In SAP Datasphere, open the `Space Management` tab and navigate to the space ´SAP_S4H´.
<br>![space_mgmt](/exercises/ex6/images/01_space_mgmt.png)

2. Use the `Copy` button to copy the space.
<br>![space_copy](/exercises/ex6/images/02_copy_space.png)

3. Repeat the two steps above for the space ´SAP_WCI´ as well.


## Exercise 6.2 Hands-on: SAP Analytics Cloud Story Copy
1. Use the `Product Switch` button to switch to SAP Analytics Cloud.
<br>![product_switch](/exercises/ex6/images/04_product_switch.png)

2. Navigate to the folder Files > Intelligent Applications > S/4HANA. Copy the folder `Finance` using the `Copy` Button as shown in the following image
<br>![story_copy](/exercises/ex6/images/05_copy_story.png)

3. Append your User ID to the name of the story and select the `Copy` button.
<br>![name_story](/exercises/ex6/images/06_name_story.png)

4. The folder and the story is copied in the folder `My Files`.
<br>![07_story_copied](/exercises/ex6/images/07_story_copied.png)


## Next steps
SAP Datasphere spaces and the SAP Analytics Cloud story for `Working Capital Insights` Intelligent Application have are now made available by the SAP BDC Admin as custom-managed versions and are ready to be customized. 

## Possible Enhancements
This is the end of this Hands-on series. As a possible enhancement, one could integrate the results of the custom-build AI/ML data product back into the Intelligent Application. The data product can be used to enhance the cashflow Fact view, then enhance the Analytic Model and integrate the enhanced Analytic Model back into the custom-version of the SAC story seen above. Due to time constraints, this is not explored. However, this can be a possible assignment that you can take away from this Hands-on series.