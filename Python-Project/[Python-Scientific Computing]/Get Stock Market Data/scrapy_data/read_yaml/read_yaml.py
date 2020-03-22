# -*- coding: utf-8 -*-
# import neccesary packages
import yaml

def read(f):
    with open(f, 'r') as stream:
        try:
            return yaml.safe_load(stream).get('date_get_data')
        except yaml.YAMLError as error:
            print(error)