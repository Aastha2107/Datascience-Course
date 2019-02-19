# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:32:45 2018

@author: aastha
"""

'''
Scrap the data from State/Territory and National Share (%) columns for top 6 states
 basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.
'''
import urllib
wiki ="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
page = urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup


soup = BeautifulSoup(page)
all_tables=soup.findAll('table')
right_table=soup.find('table', class_="wikitable")

A=[]
B=[]

for row in right_table.find_all("tr"):
    cells = row.findAll('td')
    if (len(cells)==7):
        A.append(cells[1].find(text=True))
        B.append(cells[4].find(text=True))
        

           # C.append(cells[0].find(text=True))
A.remove(A[-1])
B.remove(B[-1])
import pandas as pd
df=pd.DataFrame()
df['state']=A
df['national share']=B

print(df)
df.to_csv("data2.csv")




#now we have scrap the data now we need to plot the pie  graph

df=pd.read_csv("data2.csv")

de=df.sort_values(by='national share', ascending=[False])
de=de.head(6)

import matplotlib.pyplot as plyt
#plyt.rcdefaults()
label=['rajasthan','Madhya pradesh','maharashtra','uttar pradesh','jammu','gujarat']
colors=['r','g','b','c','m','c']
explode=[0.2,0,0,0,0,0]
plyt.pie(de['national share'],labels= label ,explode=explode,colors=colors, autopct="%2.2f%%")
plyt.title("National Share")
plyt.axis('equals')

