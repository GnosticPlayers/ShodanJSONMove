#!/usr/bin/env python3


# Written By GnosticPlayer
# Email: dreammarket@riseup.net

import sys, os, string
import json

downloaded_json = input("Please enter the downloaded Shodan .json: ")

table = []
with open(downloaded_json, 'r') as f:
    for line in f:
        try:
            j = line.split('|')[-1]
            table.append(json.loads(j))
        except ValueError:
            # You probably have bad JSON
            continue


new_file = input("Please enter new file to save ips to: ")


wr2 = open(new_file, 'a')

for row in table:
    wr2.write(row['ip_str'] + "\n")
wr2.close()
print("Operation Complete!")
