#!/usr/bin/env python3
# coding: utf-8

import json
import csv
import re
import logging
import pathlib
import sys
import getpass

API_KEY = os.environ['API_KEY']

print("API_Key  :  ", API_KEY)

#####################################################################################
#################### comment all below

# # Setup logging
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s.%(msecs)03dZ splunk_rest_upload_lookups: %(levelname)s: %(message)s',
#                     datefmt='%Y-%m-%dT%H:%M:%S')

# # Read data from CSV file
# dir = pathlib.Path().cwd()
# print(dir)
# lookup_file = "{}{}".format(dir,"/csv/test_csv.csv")
# lookup_content = []
# lookup_name = pathlib.Path(lookup_file).name

# #lookup_file = "C:\\Sundar\\testcsv.csv"
# #lookup_content = []
# #lookup_name = pathlib.Path(lookup_file).name

# try:
#     with open(lookup_file, encoding='utf-8', errors='ignore', newline='') as f:
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#             lookup_content.append(row)
# except  Exception as e:
#     logging.error("Error reading {} : {}".format(lookup_file, e))
#     exit(1)

# print("")
# contents = json.dumps(lookup_content)
# print(lookup_name)
# print("********************** contents ********************** ")
# print(lookup_content)
# print(" ")
# print("********************** contents ********************** ")
# print(json.dumps(lookup_content))
