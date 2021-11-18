# COVID-19 Case Analysis
This repository is updated and maintained by Eduardo Flores, Raquel Gaucin, and Caroline Shipley as part of participation in the Data Analytics and Visualzation Boot Camp from the University of Texas and Trilogy Education.

## Overview
Our project focuses on outcomes of COVID-19 cases in the US, and specific patient health factors that may influence them. The COVID-19 pandemic is an ongoing health crisis, and quantifying the relationship between patient information and death from COVID can be instrumental in discovering issues that may be contributing to the disease's death toll. It can also be valuable in reducing the impact of future pandemics. This analysis aims to develop a machine learning model that will accurately predict COVID-19 case outcome given various patient data.

## Project Protocols

### Communication
Our main line of communication will come from using Slack to coordinate which parts of the project we are working on and will begin working on as well as weekly Team Meetings via Zoom. All updates regarding the project will be posted within Slack and communicated to Eduardo as he is fulfilling the role responsible for maintaining the GitHub repository.

In addition, any pull requests to any branch(es) will be communicated to each team member during a team meeting and we will all go through the data together and see if we approve of the outcome.  

### Roles
 - **Eduardo** is responsible for overseeing the repository and any actions taken by team members to update it, including pull requests and merging. 
 - **Caroline** is responsible for developing the machine learning model to identify COVID-19 case outcome. This includes integrating the model with the database in which the data is stored.
 - **Raquel** is responsible for conducting an ETL process on the CDC data, including data cleaning and wrangling, and database design and creation. She is also responsible for all dashboard and visualization design.

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

## Tableau Visualization

We decided to map out the data we had on hand to get a look at what would be in store for this project. All visualizations used for this project will be located in a Tableau Public [webpage](https://public.tableau.com/app/profile/raquel.gaucin/viz/COVID-19CaseAnalysis/COVID-19CaseAnalysisDashboard).

### Surface-Level Visualizations

#### Medical Condition
Our curiosity begins when we look at the death rate while having a medical condition at the time.Approximately 6% of those with a medical condition succumbed to the virus, whereas almost 2% of those without a medical condition passed away. This means that having a medical condition while infected with COVID-19 implies a 300% higher chance of death. 

<img width="673" alt="death_rate_by_med_cond" src="https://user-images.githubusercontent.com/46951897/142105662-4bb0e531-c2e8-48ee-8930-780cf3566e93.png">

#### Sex

After medical condition, we looked at the death rate by sex. We observe in the visualization below that females had an approximate death rate of 2% and males 3%. However, within the data, there is an "unknown" gender whose death rate is at approximately 1.5%.  

<img width="677" alt="death_rate_by_sex" src="https://user-images.githubusercontent.com/46951897/142095573-c62956bf-6ec8-4e63-914d-5a8bb7a6d47f.png">

#### Age

For our next simple comparison, we decided to examine the age cohorts where each cohort spanned a range of 10 years. The most dominant death rate by far is for those who are past 80 years of age since there death rate is approxmately 29%. This is close to saying that 3 in 10 adults 80+ years old who contracted COVID would succumb to the virus. This graph is also interesting because there is an almost exponential increase in the probability of dying as a person ascends through each age group.

<img width="677" alt="death_rate_by_age" src="https://user-images.githubusercontent.com/46951897/142096388-22b024b3-cbb6-46c6-8cef-7d74deb38aa8.png">

#### Race/Ethnicity

Here is where some of the group found their inital surprises when comparing general death rates across only race/ethnicity (r/e). We found that American Indian/Alaskan Natives had the highest death rate among the other r/e's by half a percentage point at aproximately 4%. The r/e that followed was the White r/e at approximately 3.5%. 

<img width="676" alt="death_rate_by_race" src="https://user-images.githubusercontent.com/46951897/142100531-2111c16c-606d-4fbd-941d-b08436624727.png">

### In-Depth Visualiztions

#### Death Rate by Age and Sex

<img width="497" alt="age_sex_heatmap" src="https://user-images.githubusercontent.com/46951897/142118875-f539649a-c61e-4c0c-9295-260ccced7471.png">

#### Death Rate by Medical Condition and Race/Ethnicity

<img width="408" alt="race_med_cond_heatmap" src="https://user-images.githubusercontent.com/46951897/142118207-9fd30770-3cf3-4661-bfd9-ccc5b898d7c7.png">

## Analysis

### Supervised Machine Learning
A classification Supervised Machine Learning model was selected for this analysis, to be able to accurately predict COVID-19 case outcome given various patient data, with an accuracy and recall target of 90%.

To be able to achieve the target of 90%, two different ensemble classifiers were tested, [Random Forest and Easy Ensemble](https://github.com/bazinga183/COVID_deaths_analysis/blob/main/Final_Project_ensemble.ipynb). 

For this analysis, two models were tested. The first model was taking hospitalization data into account and the second model was tested without hospitalization data.

### Results with hospitalization data

#### Random Forest

* Accuracy Score: 62%
* Precision Survivals: 97%
* Precision Deaths: 57%
* Recall Survivals: 99%
* Recall Deaths: 24%

![Random](https://github.com/bazinga183/COVID_deaths_analysis/blob/main/Resources/Results/Random_Forest.PNG)

#### Easy Ensemble

* Accuracy Score: 92%
* Precision Survivals: 100%
* Precision Deaths: 29%
* Recall Survivals: 93%
* Recall Deaths: 91%

![Easy](https://github.com/bazinga183/COVID_deaths_analysis/blob/main/Resources/Results/Easy_Ensemble.PNG)

### Results without hospitalization data

#### Random Forest

* Accuracy Score: 51%
* Precision Survivals: 97%
* Precision Deaths: 59%
* Recall Survivals: 100%
* Recall Deaths: 2%

![Random](https://github.com/bazinga183/COVID_deaths_analysis/blob/main/Resources/Results/Random_without_hospital.png)

#### Easy Ensemble

* Accuracy Score: 85%
* Precision Survivals: 99%
* Precision Deaths: 14%
* Recall Survivals: 82%
* Recall Deaths: 88%

![Easy](https://github.com/bazinga183/COVID_deaths_analysis/blob/main/Resources/Results/Easy_without_hospital.png)

### Summary
To be able to predict the COVID outcome, the model needs to allow the least amount of false positives results. The statistic used for this is the recall for death outcomes.

Comparing both models, the model that took hospitalization data as an input was more accurate, reaching the goal of 90%. The model without hospitalization data was also very accurate, reaching 88%. With that said we can conclude that hospitalization helps determining the outcome of COVID cases.

Analyzing the results of the model that takes hospitalization data as an input, compering the two different methods utilized was observed that Easy Ensemble presented the highest recall with 91% while Random Forest presented only 24%.

Analyzing the accuracy score to see the model's overall performance, we can see that the model with the highest accuracy score was Easy Ensemble  with 92%, while Random Forest presented 62%.

After analyzing these two main statistics, the model that was able to accurately predict COVID outcomes is the Easy Ensemble Classifying model.
