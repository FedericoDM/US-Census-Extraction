"""This script will clean and parse the data from the US Census API"""

import os
import pandas as pd
import numpy as np

# Local imports
from src.utils.constants import (
    OUTPUT_PATH,
    TABLES_DICT,
    UNDESIRED_COLS,
)


class FileParser:
    def __init__(self, table_name):
        self.OUTPUT_PATH = OUTPUT_PATH
        self.TABLES_DICT = TABLES_DICT
        self.table_name = table_name

        if self.table_name not in self.TABLES_DICT.keys():
            raise ValueError(
                f"table_name must be one of {list(self.TABLES_DICT.keys())}"
            )

        self.table_code = self.TABLES_DICT[self.table_name]

    @staticmethod
    def clean_column(col):
        """
        This method cleans the column names
        """
        if "!!" in col:
            clean_col_split = col.split("!!")
            clean_col = " ".join(clean_col_split)
        else:
            clean_col_split = col.split("!!")
            clean_col = " ".join(clean_col_split)
        return clean_col

    def parse_df(self, path):
        """
        This method parses the downloaded data and returns a pandas DataFrame
        """
        ROW_INDEX = 1
        HEADER_INDEX = 0
        # Print the available files
        df = pd.read_csv(path)
        # Set first row as column names
        new_header = df.iloc[HEADER_INDEX]  # grab the first row for the header
        df = df[ROW_INDEX:]  # take the data less the header row
        df.columns = new_header  # set the header row as the df header

        # Drop columns if all values are NaN
        df.dropna(axis=1, how="all", inplace=True)
        undesired_cols = []
        clean_cols = []

        for col in df.columns:
            if any(undesired_col in col for undesired_col in UNDESIRED_COLS):
                undesired_cols.append(col)
            else:
                clean_col = self.clean_column(col)
                clean_cols.append(clean_col)

        df.drop(columns=undesired_cols, inplace=True)
        df.columns = clean_cols

        # Save the DataFrame
        new_path = path.replace(".csv", "_clean.csv")
        print(f"\t\t Saving {new_path}")
        df.to_csv(new_path, index=False, encoding="utf-8-sig")

    def parse_yearly_df(self, year):
        """
        Invokes parse_df and saves the DataFrame
        """
        # Define path
        path = f"{self.OUTPUT_PATH}/{self.table_name}/{self.table_code}_1Y_{year}/"
        if not os.path.exists(path):
            raise ValueError(f"{path} does not exist")
        files = os.listdir(path)
        for file in files:
            if "Column-Metadata" in file:
                continue
            elif file.endswith(".csv") and "_clean" not in file:
                print(f"\t\t Cleaning {file}")
                self.parse_df(f"{path}/{file}")

    def parse_files(self):
        """
        This method invokes parse_df on all files in the table directory
        """
        # Print the available files
        tables_directory = f"{self.OUTPUT_PATH}/{self.table_name}"
        folders = os.listdir(tables_directory)
        print("Available files:")
        for folder in folders:
            print(f"\t{folder}")
            new_path = f"{tables_directory}/{folder}"
            files = os.listdir(new_path)
            for file in files:
                print(f"\t\t {file}")
                if "Column-Metadata" in file:
                    continue
                if file.endswith(".csv") and "_clean" not in file:
                    print(f"\t\t Cleaning {file}")
                    self.parse_df(f"{new_path}/{file}")
