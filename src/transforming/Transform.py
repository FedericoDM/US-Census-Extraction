"""This script further cleans the data from the US Census API"""

import os
import pandas as pd


class Transform:
    def __init__(self, table_name):
        self.table_name = table_name
