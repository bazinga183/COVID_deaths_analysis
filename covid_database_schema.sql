-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/

CREATE TABLE "deaths" (
    "id" int   NOT NULL,
    "death" int   NOT NULL,
    "date" date   NOT NULL,
    CONSTRAINT "pk_deaths" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "sex" (
    "id" int   NOT NULL,
    "sex" varchar(6)   NOT NULL,
    CONSTRAINT "pk_sex" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "age_group" (
    "id" int   NOT NULL,
    "age_group" varchar(20)   NOT NULL,
    CONSTRAINT "pk_age_group" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "race_ethnicity" (
    "id" int   NOT NULL,
    "race_ethnicity" varchar(80)   NOT NULL,
    CONSTRAINT "pk_race_ethnicity" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "hospital_care" (
    "id" int   NOT NULL,
    "hospital" int   NOT NULL,
    CONSTRAINT "pk_hospital_care" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "med_conditions" (
    "id" int   NOT NULL,
    "med_cond" int   NOT NULL,
    CONSTRAINT "pk_med_conditions" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "sex" ADD CONSTRAINT "fk_sex_id" FOREIGN KEY("id")
REFERENCES "deaths" ("id");

ALTER TABLE "age_group" ADD CONSTRAINT "fk_age_group_id" FOREIGN KEY("id")
REFERENCES "deaths" ("id");

ALTER TABLE "race_ethnicity" ADD CONSTRAINT "fk_race_ethnicity_id" FOREIGN KEY("id")
REFERENCES "deaths" ("id");

ALTER TABLE "hospital_care" ADD CONSTRAINT "fk_hospital_care_id" FOREIGN KEY("id")
REFERENCES "deaths" ("id");

ALTER TABLE "med_conditions" ADD CONSTRAINT "fk_med_conditions_id" FOREIGN KEY("id")
REFERENCES "deaths" ("id");

