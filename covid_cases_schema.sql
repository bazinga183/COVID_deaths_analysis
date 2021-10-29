CREATE TABLE "covid_cases" (
    "id" int NOT NULL,
    "sex" varchar(6) NOT NULL,
    "age_group" varchar(20) NOT NULL,
    "race_ethnicity" varchar(40) NOT NULL,
    "hospital" varchar(7) NOT NULL,
    "med_cond" varchar(7) NOT NULL,
    "death" int NOT NULL,
    PRIMARY KEY ("id")
);

