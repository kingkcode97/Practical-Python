# -*- coding: utf-8 -*-
# import necessary packages
from datetime import datetime

def convert(s):
    # convert string to datetime
    date = datetime.strptime(str(s), '%Y%m%d')
    return date.date()