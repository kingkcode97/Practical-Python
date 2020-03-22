# -*- coding: utf-8 -*-
# import neccessary packages
import pandas as pd
from datetime import date
from datetime import timedelta
from date_process import date_preprocess
from read_yaml import read_yaml
from webscraper import webscraper

def main():
    # reading file yaml
    file = 'config.yaml'
    yaml_source = read_yaml.read(file)

    # assignment date need to scrapy data and today
    date_scrapy = date_preprocess.convert(yaml_source)
    today = date.today()
    
    dict_data = {
                'Date': [],
                'Currency' : [],
                'Purchase_Price': [],
                'Transfer_Price': [],
                'Price': []
            }

    # while loop from date_scrapy to today
    while date_scrapy <= today:
        list_info = webscraper.parse(date_scrapy)[:]
        for key, value in zip(dict_data.keys(), list_info):
            dict_data[key].extend(value)
            
        # add date_scrapy 1 day
        date_scrapy += timedelta(days=1)
        
    # assignment dataframe
    dataframe = pd.DataFrame(dict_data)
    
    # save dataframe to csv format
    dataframe.to_csv('stock_in_24h_com_vn.csv')
    print('[Completed]')

if __name__ == '__main__':
    main()