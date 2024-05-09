"""This script runs the whole pipeline"""

import argparse
from src.extraction.FileDownloader import FileDownloader
from src.parsing.FileParser import FileParser

parser = argparse.ArgumentParser(
    description="Download and parse USCensus data from a given table"
)

parser.add_argument(
    "table_name",
    type=str,
    choices=[
        "Demographics",
        "Median Income",
        "Education",
        "Poverty",
        "Housing",
        "Foreign Born",
        "Commuting",
    ],
    help="Name of the table to download",
)

parser.add_argument(
    "download_type",
    type=str,
    choices=["all_years", "single_year"],
    default="all_years",
    help="Whether to download all years or a single year",
)

parser.add_argument(
    "--year",
    type=int,
    default=2021,
    help="Year to download. Defaults to 2021",
)


args = parser.parse_args()

if __name__ == "__main__":
    if args.download_type == "all_years":
        downloader = FileDownloader(args.table_name)
        downloader.download_all_years()
        file_parser = FileParser(args.table_name)
        file_parser.parse_files()
    else:
        downloader = FileDownloader(args.table_name, args.year)
        downloader.download_file(args.year)
        file_parser = FileParser(args.table_name)
        file_parser.parse_yearly_df(args.year)
