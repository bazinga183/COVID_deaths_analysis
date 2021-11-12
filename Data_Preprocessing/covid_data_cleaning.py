
# dependencies
import pandas as pd
from sqlalchemy import create_engine
from config import db_password, db_name
import time

# import data
# data source: https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf
covid_data = pd.read_csv('COVID-19_Case_Surveillance_Public_Use_Data.csv')

# convert date column to date type
covid_data['date'] = pd.to_datetime(covid_data['cdc_case_earliest_dt '], yearfirst=True)

# reduce number of columns
covid_deaths = covid_data[[
    'date',
    'sex',
    'age_group',
    'race_ethnicity_combined',
    'medcond_yn',
    'hosp_yn',
    'death_yn',
]]

# sort data by date
covid_deaths = covid_deaths.sort_values('date')

# keep only records with 'Yes' or 'No' in death column
covid_deaths = covid_deaths[covid_deaths['death_yn'].isin(['Yes', 'No'])]

# keep records beginning 2020-10-01
covid_deaths = covid_deaths[covid_deaths['date'] >= '2020-10-01']

# standardize null and 'Missing' values as 'Unknown'
covid_deaths.fillna('Unknown', inplace=True)
covid_deaths.replace('Missing', 'Unknown', inplace=True)

# rename columns
covid_deaths.rename(inplace=True, columns={
    'race_ethnicity_combined':'race_ethnicity',
    'medcond_yn':'med_cond',
    'hosp_yn':'hospital',
    'death_yn':'death'
})

# convert death column to int
covid_deaths['death'] = covid_deaths['death'].apply(lambda value: 0 if value == 'No' else 1)

# reset index
covid_deaths.reset_index(inplace=True, drop=True)

# CREATE DATAFRAMES FOR EACH FIELD

# table with death and date
deaths = covid_deaths[['death', 'date']].copy()
deaths.rename(columns={'date':'cdc_date'}, inplace=True)

# table for sex
sex = pd.DataFrame(covid_deaths['sex'])
sex_drop_index = sex[sex['sex'] == 'Unknown'].index
sex.drop(sex_drop_index, inplace=True)

# table for age_group
age_group = pd.DataFrame(covid_deaths['age_group'])
age_drop_index = age_group[age_group['age_group'] == 'Unknown'].index
age_group.drop(age_drop_index, inplace=True)

# table for race and ethnicity
race_ethnicity = pd.DataFrame(covid_deaths['race_ethnicity'])
race_drop_index = race_ethnicity[race_ethnicity['race_ethnicity'] == 'Unknown'].index
race_ethnicity.drop(race_drop_index, inplace=True)

# table for medical conditions
med_conditions = pd.DataFrame(covid_deaths['med_cond'])
med_drop_index = med_conditions[med_conditions['med_cond'] == 'Unknown'].index
med_conditions.drop(med_drop_index, inplace=True)
med_conditions['med_cond'] = med_conditions['med_cond'].apply(lambda value: 0 if value == 'No' else 1)

# table for hospital care
hospital_care = pd.DataFrame(covid_deaths['hospital'])
hosp_drop_index = hospital_care[hospital_care['hospital'] == 'Unknown'].index
hospital_care.drop(hosp_drop_index, inplace=True)
hospital_care['hospital'] = hospital_care['hospital'].apply(lambda value: 0 if value == 'No' else 1)

# export all to csv
deaths.to_csv('Resources/Data/deaths.csv', index_label='id')
sex.to_csv('Resources/Data/sex.csv', index_label='id')
age_group.to_csv('Resources/Data/age_group.csv', index_label='id')
race_ethnicity.to_csv('Resources/Data/race_ethnicity.csv', index_label='id')
med_conditions.to_csv('Resources/Data/med_conditions.csv', index_label='id')
hospital_care.to_csv('Resources/Data/hospital_care.csv', index_label='id')

# EXPORT TO POSTGRESQL

db_string = f'postgresql://postgres:{db_password}@127.0.0.1:5432/{db_name}'
engine = create_engine(db_string)

rows_imported = 0
table = 'deaths'
start_time = time.time()
for data in pd.read_csv(f'Resources/Data/{table}.csv', chunksize=1000000):
    print(f'importing rows {rows_imported} to {rows_imported + len(data)}...', end='')
    data.to_sql(name=table, con=engine, index=False, if_exists='append')
    rows_imported += len(data)

    # add elapsed time to final print out
    print(f'Done. {time.time() - start_time} total seconds elapsed')

rows_imported = 0
table = 'sex'
start_time = time.time()
for data in pd.read_csv(f'Resources/Data/{table}.csv', chunksize=1000000):
    print(f'importing rows {rows_imported} to {rows_imported + len(data)}...', end='')
    data.to_sql(name=table, con=engine, index=False, if_exists='append')
    rows_imported += len(data)

    print(f'Done. {time.time() - start_time} total seconds elapsed')

rows_imported = 0
table = 'age_group'
start_time = time.time()
for data in pd.read_csv(f'Resources/Data/{table}.csv', chunksize=1000000):
    print(f'importing rows {rows_imported} to {rows_imported + len(data)}...', end='')
    data.to_sql(name=table, con=engine, index=False, if_exists='append')
    rows_imported += len(data)

    print(f'Done. {time.time() - start_time} total seconds elapsed')

rows_imported = 0
table = 'race_ethnicity'
start_time = time.time()
for data in pd.read_csv(f'Resources/Data/{table}.csv', chunksize=1000000):
    print(f'importing rows {rows_imported} to {rows_imported + len(data)}...', end='')
    data.to_sql(name=table, con=engine, index=False, if_exists='append')
    rows_imported += len(data)

    print(f'Done. {time.time() - start_time} total seconds elapsed')

rows_imported = 0
table = 'med_conditions'
start_time = time.time()
for data in pd.read_csv(f'Resources/Data/{table}.csv', chunksize=1000000):
    print(f'importing rows {rows_imported} to {rows_imported + len(data)}...', end='')
    data.to_sql(name=table, con=engine, index=False, if_exists='append')
    rows_imported += len(data)

    print(f'Done. {time.time() - start_time} total seconds elapsed')

rows_imported = 0
table = 'hospital_care'
start_time = time.time()
for data in pd.read_csv(f'Resources/Data/{table}.csv', chunksize=1000000):
    print(f'importing rows {rows_imported} to {rows_imported + len(data)}...', end='')
    data.to_sql(name=table, con=engine, index=False, if_exists='append')
    rows_imported += len(data)

    print(f'Done. {time.time() - start_time} total seconds elapsed')
