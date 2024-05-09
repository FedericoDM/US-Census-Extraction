# Census Data Repository

Repository created to automatically get Census data of interest from the Census API. The pipeline consists of the extraction part, which downloads the data from the Census API, and the parsing part, which parses the downloaded files and stores the clean data in a `pandas` DataFrame. Note that the tables contain the for all 'places' in the US (i.e. cities).

The `src` folder contains the code to extract, parse, and store the data. The `data` folder contains the data that has been extracted, which is hidden from the repository.

## Extraction

The `Extraction` folder contains the `FileDownloader` class, which downloads a 'zip' file from the Census API and extracts the contents to a specified folder. The user can specify the year and the table to extract (the available tables are in the `src/utils/constants.py` file, in the 'TABLES_DICT' dictionary). The `FileDownloader` class can be used as follows:

```python
# Import the FileDownloader class
from FileDownloader import FileDownloader

# Table to download
table = "Housing"

# Create an instance of the FileDownloader class
file_downloader = FileDownloader("Housing")

# To download all the available years of the table
file_downloader.download_all_years()

# To download a specific year of the table
file_downloader.download_year(2022)
```

Note that, sometimes, the first tables are not downloaded when running the `download_all_years` method. What has worked for me is to run the `download_all_years` method again.

Also, note that not all the tables are available for all the years. The `download_year` method will raise an error if the table is not available for the specified year.

## Parsing

The `Parsing` folder contains the `FileParser` class, which parses the downloaded files and stores the clean data in a `pandas` DataFrame. The data will be saved in the same folder as the downloaded files.

 The `FileParser` class can be used as follows:

```python

# Import the FileParser class
from FileParser import FileParser

# Table to parse
table = "Housing"

# Create an instance of the FileParser class
file_parser = FileParser(table)

# To parse all the available years of the table
file_parser.parse_files()

# To parse a specific year of the table
file_parser.parse_yearly_df(2022)

# To parse specific file
path = "path/to/file"
file_parser.parse_df(path)
```

## Run the complete process

The `main.py` file contains the code to run the complete process of downloading and parsing the data. The user can specify the table and the year of interest. Note that, sometimes, the first tables are not downloaded when running the `download_all_years` method. What has worked for me is to run the `download_all_years` method again. Also, note that not all the tables are available for all the years. The `download_year` method will raise an error if the table is not available for the specified year.


The `main.py` file can be used as follows:

```bash

# To download and parse all the available years of the table
python3 main.py "Housing" "all_years"

# The output is the following (note that I had to run the process twice to get all the files):
Successfully downloaded file Housing/S2501_1Y_2010
Successfully downloaded file Housing/S2501_1Y_2011
Successfully downloaded file Housing/S2501_1Y_2012
Successfully downloaded file Housing/S2501_1Y_2013
Successfully downloaded file Housing/S2501_1Y_2014
Successfully downloaded file Housing/S2501_1Y_2015
Successfully downloaded file Housing/S2501_1Y_2016
Successfully downloaded file Housing/S2501_1Y_2017
Successfully downloaded file Housing/S2501_1Y_2018
Successfully downloaded file Housing/S2501_1Y_2019
Error extracting file Housing/S2501_1Y_2020: File is not a zip file
Year 2020 may not be available for the S2501 table
Successfully downloaded file Housing/S2501_1Y_2021
Successfully downloaded file Housing/S2501_1Y_2022
Error extracting file Housing/S2501_1Y_2023: File is not a zip file
Year 2023 may not be available for the S2501 table
Available files:
        S2501_1Y_2010
                 ACSST1Y2010.S2501-Column-Metadata.csv
                 ACSST1Y2010.S2501-Data.csv
                 Cleaning ACSST1Y2010.S2501-Data.csv
                 ACSST1Y2010.S2501-Table-Notes.txt
        S2501_1Y_2011
                 ACSST1Y2011.S2501-Column-Metadata.csv
                 ACSST1Y2011.S2501-Data.csv
                 Cleaning ACSST1Y2011.S2501-Data.csv
                 ACSST1Y2011.S2501-Table-Notes.txt
        S2501_1Y_2012
                 ACSST1Y2012.S2501-Column-Metadata.csv
                 ACSST1Y2012.S2501-Data.csv
                 Cleaning ACSST1Y2012.S2501-Data.csv
                 ACSST1Y2012.S2501-Table-Notes.txt
        S2501_1Y_2013
                 ACSST1Y2013.S2501-Column-Metadata.csv
                 ACSST1Y2013.S2501-Data.csv
                 Cleaning ACSST1Y2013.S2501-Data.csv
                 ACSST1Y2013.S2501-Table-Notes.txt
        S2501_1Y_2014
                 ACSST1Y2014.S2501-Column-Metadata.csv
                 ACSST1Y2014.S2501-Data.csv
                 Cleaning ACSST1Y2014.S2501-Data.csv
                 ACSST1Y2014.S2501-Table-Notes.txt
        S2501_1Y_2015
                 ACSST1Y2015.S2501-Column-Metadata.csv
                 ACSST1Y2015.S2501-Data.csv
                 Cleaning ACSST1Y2015.S2501-Data.csv
                 ACSST1Y2015.S2501-Table-Notes.txt
        S2501_1Y_2016
                 ACSST1Y2016.S2501-Column-Metadata.csv
                 ACSST1Y2016.S2501-Data.csv
                 Cleaning ACSST1Y2016.S2501-Data.csv
                 ACSST1Y2016.S2501-Table-Notes.txt
        S2501_1Y_2017
                 ACSST1Y2017.S2501-Column-Metadata.csv
                 ACSST1Y2017.S2501-Data.csv
                 Cleaning ACSST1Y2017.S2501-Data.csv
                 ACSST1Y2017.S2501-Table-Notes.txt
        S2501_1Y_2018
                 ACSST1Y2018.S2501-Column-Metadata.csv
                 ACSST1Y2018.S2501-Data.csv
                 Cleaning ACSST1Y2018.S2501-Data.csv
                 ACSST1Y2018.S2501-Table-Notes.txt
        S2501_1Y_2019
                 ACSST1Y2019.S2501-Column-Metadata.csv
                 ACSST1Y2019.S2501-Data.csv
                 Cleaning ACSST1Y2019.S2501-Data.csv
                 ACSST1Y2019.S2501-Table-Notes.txt
        S2501_1Y_2021
                 ACSST1Y2021.S2501-Column-Metadata.csv
                 ACSST1Y2021.S2501-Data.csv
                 Cleaning ACSST1Y2021.S2501-Data.csv
                 ACSST1Y2021.S2501-Data_clean.csv
                 ACSST1Y2021.S2501-Table-Notes.txt
        S2501_1Y_2022
                 ACSST1Y2022.S2501-Column-Metadata.csv
                 ACSST1Y2022.S2501-Data.csv
                 Cleaning ACSST1Y2022.S2501-Data.csv
                 ACSST1Y2022.S2501-Data_clean.csv
                 ACSST1Y2022.S2501-Table-Notes.txt

# To download and parse a specific year of the table
python3 main.py "Housing" "single_year" --year 2022

# The output is the following:
Successfully downloaded file Housing/S2501_1Y_2022
                 Cleaning ACSST1Y2022.S2501-Data.csv

```

For example, I had to run the command twice for the 'Education' table to get all the files:

```bash

# The first time, most of the files were not downloaded:
python3 main.py "Education" "all_years"

Error extracting file Education/S1501_1Y_2010: File is not a zip file
Year 2010 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2011: File is not a zip file
Year 2011 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2012: File is not a zip file
Year 2012 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2013: File is not a zip file
Year 2013 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2014: File is not a zip file
Year 2014 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2015: File is not a zip file
Year 2015 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2016: File is not a zip file
Year 2016 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2017: File is not a zip file
Year 2017 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2018: File is not a zip file
Year 2018 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2019: File is not a zip file
Year 2019 may not be available for the S1501 table
Error extracting file Education/S1501_1Y_2020: File is not a zip file
Year 2020 may not be available for the S1501 table
Successfully downloaded file Education/S1501_1Y_2021
Successfully downloaded file Education/S1501_1Y_2022
Error extracting file Education/S1501_1Y_2023: File is not a zip file
Year 2023 may not be available for the S1501 table
Available files:
        S1501_1Y_2021
                 ACSST1Y2021.S1501-Column-Metadata.csv
                 ACSST1Y2021.S1501-Data.csv
                 Cleaning ACSST1Y2021.S1501-Data.csv
                 ACSST1Y2021.S1501-Table-Notes.txt
        S1501_1Y_2022
                 ACSST1Y2022.S1501-Column-Metadata.csv
                 ACSST1Y2022.S1501-Data.csv
                 Cleaning ACSST1Y2022.S1501-Data.csv
                 ACSST1Y2022.S1501-Table-Notes.txt


# The second time, all the files were downloaded:
python3 main.py "Education" "all_years"

Successfully downloaded file Education/S1501_1Y_2010
Successfully downloaded file Education/S1501_1Y_2011
Successfully downloaded file Education/S1501_1Y_2012
Successfully downloaded file Education/S1501_1Y_2013
Successfully downloaded file Education/S1501_1Y_2014
Successfully downloaded file Education/S1501_1Y_2015
Successfully downloaded file Education/S1501_1Y_2016
Successfully downloaded file Education/S1501_1Y_2017
Successfully downloaded file Education/S1501_1Y_2018
Successfully downloaded file Education/S1501_1Y_2019
Error extracting file Education/S1501_1Y_2020: File is not a zip file
Year 2020 may not be available for the S1501 table
Successfully downloaded file Education/S1501_1Y_2021
Successfully downloaded file Education/S1501_1Y_2022
Error extracting file Education/S1501_1Y_2023: File is not a zip file
Year 2023 may not be available for the S1501 table
Available files:
        S1501_1Y_2010
                 ACSST1Y2010.S1501-Column-Metadata.csv
                 ACSST1Y2010.S1501-Data.csv
                 Cleaning ACSST1Y2010.S1501-Data.csv
                 ACSST1Y2010.S1501-Table-Notes.txt
        S1501_1Y_2011
                 ACSST1Y2011.S1501-Column-Metadata.csv
                 ACSST1Y2011.S1501-Data.csv
                 Cleaning ACSST1Y2011.S1501-Data.csv
                 ACSST1Y2011.S1501-Table-Notes.txt
        S1501_1Y_2012
                 ACSST1Y2012.S1501-Column-Metadata.csv
                 ACSST1Y2012.S1501-Data.csv
                 Cleaning ACSST1Y2012.S1501-Data.csv
                 ACSST1Y2012.S1501-Table-Notes.txt
        S1501_1Y_2013
                 ACSST1Y2013.S1501-Column-Metadata.csv
                 ACSST1Y2013.S1501-Data.csv
                 Cleaning ACSST1Y2013.S1501-Data.csv
                 ACSST1Y2013.S1501-Table-Notes.txt
        S1501_1Y_2014
                 ACSST1Y2014.S1501-Column-Metadata.csv
                 ACSST1Y2014.S1501-Data.csv
                 Cleaning ACSST1Y2014.S1501-Data.csv
                 ACSST1Y2014.S1501-Table-Notes.txt
        S1501_1Y_2015
                 ACSST1Y2015.S1501-Column-Metadata.csv
                 ACSST1Y2015.S1501-Data.csv
                 Cleaning ACSST1Y2015.S1501-Data.csv
                 ACSST1Y2015.S1501-Table-Notes.txt
        S1501_1Y_2016
                 ACSST1Y2016.S1501-Column-Metadata.csv
                 ACSST1Y2016.S1501-Data.csv
                 Cleaning ACSST1Y2016.S1501-Data.csv
                 ACSST1Y2016.S1501-Table-Notes.txt
        S1501_1Y_2017
                 ACSST1Y2017.S1501-Column-Metadata.csv
                 ACSST1Y2017.S1501-Data.csv
                 Cleaning ACSST1Y2017.S1501-Data.csv
                 ACSST1Y2017.S1501-Table-Notes.txt
        S1501_1Y_2018
                 ACSST1Y2018.S1501-Column-Metadata.csv
                 ACSST1Y2018.S1501-Data.csv
                 Cleaning ACSST1Y2018.S1501-Data.csv
                 ACSST1Y2018.S1501-Table-Notes.txt
        S1501_1Y_2019
                 ACSST1Y2019.S1501-Column-Metadata.csv
                 ACSST1Y2019.S1501-Data.csv
                 Cleaning ACSST1Y2019.S1501-Data.csv
                 ACSST1Y2019.S1501-Table-Notes.txt
        S1501_1Y_2021
                 ACSST1Y2021.S1501-Column-Metadata.csv
                 ACSST1Y2021.S1501-Data.csv
                 Cleaning ACSST1Y2021.S1501-Data.csv
                 ACSST1Y2021.S1501-Data_clean.csv
                 ACSST1Y2021.S1501-Table-Notes.txt
        S1501_1Y_2022
                 ACSST1Y2022.S1501-Column-Metadata.csv
                 ACSST1Y2022.S1501-Data.csv
                 Cleaning ACSST1Y2022.S1501-Data.csv
                 ACSST1Y2022.S1501-Data_clean.csv
                 ACSST1Y2022.S1501-Table-Notes.txt
```

If a year is not downloaded on the second run, it surely means that the table is not available for that year. In our previous example, the 'Education' table is not available for the years 2020 and 2023.


## Available tables

Note that the availble tables are in the `src/utils/constants.py` file, in the 'TABLES_DICT' dictionary. The tables are the following:

```python

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

```