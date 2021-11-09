# COVID-19 Case Analysis
This repository is updated and maintained by Eduardo Flores, Raquel Gaucin, and Caroline Shipley as part of participation in the Data Analytics and Visualzation Boot Camp from the University of Texas and Trilogy Education.

## Overview
Our project focuses on outcomes of COVID-19 cases in the US, and specific patient health factors that may influence them. The COVID-19 pandemic is an ongoing health crisis, and quantifying the relationship between patient information and death from COVID can be instrumental in discovering issues that may be contributing to the disease's death toll. It can also be valuable in reducing the impact of future pandemics. This analysis aims to develop a machine learning model that will accurately predict COVID-19 case outcome given various patient data.

## Project Protocols

### Communication
Our main line of communication will come from using Slack to coordinate which parts of the project we are working on and will begin working on as well as weekly Team Meetings via Zoom. All updates regarding the project will be posted within Slack and communicated to Eduardo as he is fulfilling the role of the Square for this project; the role responsible for maintaining the GitHub repository.

In addition, any pull requests to any branch(es) will be communicated to each team member during a team meeting and we will all go through the data together and see if we approve of the outcome.  

### Roles
 - **Eduardo** is responsible for overseeing the repository and any actions taken by team members to update it, including pull requests and merging. 
 - **Caroline** is responsible for developing the machine learning model to identify COVID-19 case outcome. This includes integrating the model with the database in which the data is stored.
 - **Raquel** is responsible for conducting an ETL process on the CDC data, including data cleaning and wrangling, and database design and creation.

## Source Data

### Data Description
Our primary source will be [COVID-19 Case Surveillance Data](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf) from the CDC. The data set records both probable and confirmed COVID-19 cases in the US, as well as details about the patient, including sex, age group, race, ethnicity, presence of underlying health conditions, whether the patient received hospital care, and whether case resulted in death. With this data, we hope to discover which factors contribute most strongly to COVID-19 case outcome.

The data fields used in this analysis are as follows:

- **date** - A CDC-calculated field equal to the earlier of two potentially differing dates: that of a patient's COVID-19 first positive specimen collection or that of a case's first report to the CDC. While the raw data set contains fields for both of those dates, the CDC recommends reasearchers use this calculated date in time series and other analyses. This project uses a year's worth of CDC case data, spanning from 10/1/2020 to 10/9/2021.
- **sex** - The patient's sex, reported as Male, Female, or Other.
- **age_group** - The patient's age, binned by decades, i.e. 0-9 Years, 10-19 Years, 20-29 Years, etc., with a final bin of 80+ Years
- **race_ethnicity** - The patient's race and ethnicity. If more than one race was reported, the patient was categorized into "Multiple/Other." The reported values are:
  - American Indian/Alaska Native, Non-Hispanic
  - Asian, Non-Hispanic
  - Black, Non-Hispanic
  - Native Hawaiian/Other Pacific Islander, Non-Hispanic
  - White, Non-Hispanic
  - Multiple/Other, Non-Hispanic
  - Hispanic/Latino
- **hospital**: A binary field indicating whether a patient was hospitalized.
- **med_cond**: A binary field indicating the presence of any underlying comorbidity or disease.
- **death**: A binary field indicating whether a case resulted in death.

For binary fields, 0 corresponds to "No" and 1 to "Yes".

### Data Limitations
The raw CDC data set contains many unknown or missing values across every health factor. As our analysis aims to measure the influence of certain health factors relative to others on COVID-19 case outcome, we have chosen to focus on case records that have clearly reported values for each factor. Further analysis might focus on fewer factors to allow the use of more cases, as some metrics have fewer unknowns than others. We see our analysis as one that can point to relationships between COVID-19 case outcome and patient information, so that those relationships can be more closely targeted by future investigation.
