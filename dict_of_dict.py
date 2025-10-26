#!/usr/bin/env python3 

def create_dict_of_dict(filename, top_key):
    result = {}
    
    with open(filename, 'r') as file_read:
        lines = file_read.read().strip().split('\n')
        header = lines[0].split('\t')
        id_col = header[0]
        for line in lines[1:]:
            #isolate the lines into a list separated by the tabs
            parts = line.strip().split('\t')
            #combine the header line with the components into a dictionary
            data = dict(zip(header,parts))
            #set top level keys
            key = data[id_col].strip()
            #build the final dictionary
            result[key] = {
                'Action': data['Action'].split(','),
                'Damage': [int(x) for x in data['Damage'].split(',')],
                'Health': [int(data['Health'])],
                'Image': data['Image'],
                'Name': [data['Name']] }
    return result