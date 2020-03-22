# -*- coding: utf-8 -*-
# import necessary packages
from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep

# remove \t \n \r
def clean(txt):
    if txt:
        return " ".join("".join(txt).split()).strip()
    return None

def parse(date):
    """
    Grab stock data from 24h.com.vn page

    Args:
        url (str): link to page
        date (datetime): date scraped

    Returns:
        dict: Scraped data
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    for entries in range(5):
        try:
            url = "https://www.24h.com.vn/ty-gia-ngoai-te-ttcb-c426.html?d=%s" % (str(date))
            # query the website
            response = requests.get(url, headers=headers, verify=False)

            if response.status_code!=200:
                raise ValueError("Invalid Response Received From Webserver")

            # import url page need to scrapy
            print("Parsing %s" % (url))

            # adding random delay
            sleep(randint(1,3))

            # parse the html
            content = BeautifulSoup(response.content, 'html.parser')

            # find table
            table = content.findAll('table')

            # initialize list element
            list_data = [[], [], [], [], []]
            
            # access columns in tabular data
            for tr in table[1].findAll('tr'):
                # access rows in tabular data
                for i, td in enumerate(tr.find_all('td')):
                    list_data[i+1].append(clean(td.text))
                    
                list_data[0].append(date)
                
            return list_data
        except Exception as e:
            print("Failed to process the request, Exception: %s"%(e))