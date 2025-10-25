#!/usr/bin/env python3

import csv 

def immune(filepath, primary_key_column):
    immune_dict = {}
    with open(filepath, 'r', newline = '') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter = '\t')
        for row in reader:
            primary_key = row.pop(primary_key_column)
            immune_dict[primary_key] = row
    return immune_dict
print(immune('immune.txt','Immune_Name'))