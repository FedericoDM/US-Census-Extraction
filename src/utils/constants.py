"""This script holds constants used throughout the project"""

# Extraction constants

DOWNLOAD_API = "https://data.census.gov/api/access/table/download"
OUTPUT_PATH = "./data"
TABLES_DICT = {
    "Demographics": "CP05",
    "Median Income": "S1901",
    "Education": "S1501",
    "Poverty": "S1701",
    "Housing": "S2501",
    "Foreign Born": "S0201",
}

ACS_IDS = {
    "Demographics": "ACSCP",
    "Median Income": "ACSST",
    "Education": "ACSST",
    "Poverty": "ACSST",
    "Housing": "ACSST",
    "Foreign Born": "ACSSPP",
}

TIME_SLEEP = 0.5
BOTTOM_YEAR = 2010

# Parsing constants
UNDESIRED_COLS = ["Unnamed", "Statistical Significance", "Margin of Error"]

# Desired Variables:

VARIABLES_DICT = {
    "Demographics": {
        "Total Population": "SEX AND AGE Total Population",
        "Share White": "RACE Total population One race White",
        "Share Black": "RACE Total population One race Black or African American",
        "Share Hispanic": "HISPANIC OR LATINO AND RACE Total population Hispanic or Latino (of any race)",
        "Share 65 and older": "2022 Estimate SEX AND AGE Total population 65 years and over",
        "Share 50 and older": [
            "2022 Estimate SEX AND AGE Total population 45 to 54 years"
            "2022 Estimate SEX AND AGE Total population 55 to 59 years",
            "2022 Estimate SEX AND AGE Total population 60 to 64 years",
            "2022 Estimate SEX AND AGE Total population 65 years and over",
        ],
        "Median Household Income": [
            "Households Estimate Median income (dollars)",
            "Families Estimate Median income (dollars)",
        ],
    },
    "Poverty": {
        "Poverty Rate": "Percent below poverty level Estimate Population for whom poverty status is determined",
        "Share Renter": [
            "Estimate Renter-occupied housing units Occupied housing units",
            "Estimate Occupied housing units Occupied housing units",
        ],
    },
    "Foreign Born": {
        "Foreign Born Status": "Estimate PLACE OF BIRTH, CITIZENSHIP STATUS AND YEAR OF ENTRY Foreign born"
    },
}
# Share College Graduate
