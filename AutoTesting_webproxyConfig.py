# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:15:29 2021

@author: Darren.Lin
"""


import requests
import pandas as pd
import os,sys,readline
from bs4 import BeautifulSoup
requests.packages.urllib3.disable_warnings()


df = pd.read_excel(r'C:\Users\darren.lin\Desktop\市场域名绑定申请(代理碼) (新SLB對應表)0220.xlsx',sheet_name='test') 
Domain_lists=df['IP'].tolist()

for i in Domain_lists:
    try:
        protocol='https://'
        url=protocol+i
        html = requests.get(url)
        html.encoding = 'utf8'
        soup = BeautifulSoup(html.text,"html.parser")
        script=soup.find("script")
        z=script.string
        log= open('C:/Users/darren.lin/Desktop/log.txt',"a")
        print(i,html.status_code,z[60:70].split('\'')[1],file=log)
        print(i,html.status_code,z[60:70].split('\'')[1])
        log.close()
    except :
        log= open('C:/Users/darren.lin/Desktop/log.txt',"a")
        print(i+'無法連線',file=log)
        print(url+'無法連線')
        log.close()



 






