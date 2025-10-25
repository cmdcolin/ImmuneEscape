#!/usr/bin/env python3 
import csv 

def create_dict_of_dict(filepath, primary_key_column):
        nested_dict = {}
        with open(filepath,'r', newline = '') as tsvfile:
            reader = csv.DictReader(tsvfile, delimiter = '\t') 
            for row in reader:
                primary_key = row.pop(primary_key_column)
                nested_dict[primary_key] = row
        return nested_dict   
print (create_dict_of_dict('pathogen.txt','Pathogen_Name'))