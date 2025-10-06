#!/usr/bin/python3
import os
import json
import csv
from datetime import *

# Generate filename with current date/time
time1 = datetime.now()
# filepath = time1.strftime('Daily_reports_%Y-%m-%d_%H%M.csv')
filepath= 'daily_report.csv'

# Load JSON commands
jsonfile = 'my_json.json'
with open(jsonfile) as jf:
    my_dict = json.load(jf)

# Detect OS flavour
os_flavour = os.popen(my_dict['os_flavour']).read().strip().lower()

if os_flavour in ['ubuntu', 'rhel' ]:
    print("Operating system is Ubuntu or RHEL. Collecting information, please wait...")

    hostname = os.popen(my_dict['hostname']).read().strip()
    ip_address = os.popen(my_dict['ip_address']).read().strip()
    df_details = os.popen(my_dict['df_details']).read().strip()

    header_csv = my_dict['headers_pars']
    data_csv = [hostname, ip_address, df_details]

    with open(filepath, 'a', newline='') as file1:
        csvwriter = csv.writer(file1)
        csvwriter.writerow(header_csv)
        csvwriter.writerow(data_csv)

    print(f"✅ File created successfully: {filepath}")
else:
    print(f"⚠️ Other operating system detected: {os_flavour}")
