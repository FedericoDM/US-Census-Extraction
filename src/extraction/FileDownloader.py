"""This script downloads the corresponding files from the US Census API"""

import io
import zipfile
from datetime import datetime
import time

import requests

# Local imports
from src.utils.constants import (
    DOWNLOAD_API,
    OUTPUT_PATH,
    TABLES_DICT,
    ACS_IDS,
    TIME_SLEEP,
    BOTTOM_YEAR,
)


class FileDownloader:
    def __init__(self, table_name, year_to_query=2021, type_estimate="1Y"):
        # Set up constants
        self.DOWNLOAD_API = DOWNLOAD_API
        self.OUTPUT_PATH = OUTPUT_PATH
        self.TABLES_DICT = TABLES_DICT
        self.ACS_IDS = ACS_IDS
        self.TIME_SLEEP = TIME_SLEEP
        self.BOTTOM_YEAR = BOTTOM_YEAR

        if type_estimate not in ["1Y", "5Y"]:
            raise ValueError('type_estimate must be either "1Y" or "5Y"')
        self.year_to_query = year_to_query
        self.type_estimate = type_estimate
        self.table_name = table_name
        if self.table_name not in self.TABLES_DICT.keys():
            raise ValueError(
                f"table_name must be one of {list(self.TABLES_DICT.keys())}"
            )

        self.headers = {
            "authority": "data.census.gov",
            "method": "POST",
            "path": "/api/access/table/download",
            "scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
        }

        # Get table code and ACS ID
        self.table_code = self.TABLES_DICT[self.table_name]
        self.acs_id = self.ACS_IDS[self.table_name]

        self.payload = {
            "request": {
                "codeset": "",
                "comm": "",
                "download_estimate": False,
                "g": "010XX00US$1600000",
                "id": f"{self.acs_id}{self.type_estimate}{self.year_to_query}.{self.table_code}",
                "matfuel": "",
                "n": "",
                "napcs": "",
                "nkd": "",
                "p": "",
                "t": "",
            }
        }

        self.current_year = datetime.now().year
        self.years_list = list(range(self.BOTTOM_YEAR, self.current_year + 1))

    def download_file(self, year):
        """
        Downloading file of a given census table
        """

        new_id = f"{self.acs_id}{self.type_estimate}{year}.{self.table_code}"
        self.payload["request"]["id"] = new_id

        # print(self.payload)

        download_response = requests.post(
            self.DOWNLOAD_API, headers=self.headers, json=self.payload
        )

        if download_response.status_code == 200:
            response = download_response.json()
            download_url = response["response"]["url"]
            download_file = requests.get(download_url, headers=self.headers)
            file_dir = f"{self.table_code}_{self.type_estimate}_{year}"
            try:
                z = zipfile.ZipFile(io.BytesIO(download_file.content))
                z.extractall(f"{self.OUTPUT_PATH}/{self.table_name}/{file_dir}")
                print(f"Successfully downloaded file {self.table_name}/{file_dir}")
            except Exception as e:
                print(f"Error extracting file {self.table_name}/{file_dir}: {e}")
                print(
                    f"Year {year} may not be available for the {self.table_code} table"
                )

        else:
            print("Error getting download url")

    def download_all_years(self):
        """
        Downloads all the years for a given table
        """
        for year in self.years_list:
            self.download_file(year)
            time.sleep(self.TIME_SLEEP)
