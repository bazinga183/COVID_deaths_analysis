# create single table of containing all rows with no unknown values

SELECT d.id, d.death, d.date, s.sex,
	   ag.age_group, re.race_ethnicity, hc.hospital, mc.med_cond
INTO covid_case_data
FROM (((((deaths AS d
INNER JOIN med_conditions AS mc ON mc.id = d.id)
INNER JOIN hospital_care AS hc ON hc.id = d.id)
INNER JOIN age_group AS ag ON ag.id = d.id)
INNER JOIN race_ethnicity AS re ON re.id = d.id)
INNER JOIN sex AS s ON s.id = d.id);