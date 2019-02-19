# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:05:58 2018

@author: aastha
"""
'''import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number of their cars and explode the largest car maker


'''
import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame()
df=pd.read_csv("Automobile.csv ")
car=df['make'].value_counts()
car=car.head(10)
label=["toyota","nissan","mazda","honda","mitsubishi","subaru","volkswagen","peugot","volvo","dodge"]

plt.pie(car.head(5),labels=car.index[:5],explode=(0.2,0,0,0,0),autopct="%2.2f%%")
plt.axis('equal')
plt.savefig('demo.jpg')
plt.show()

#using numpy
#grnfromtxt is used to read a csv file 
import numpy as np
from numpy import genfromtxt
my_data = genfromtxt('Automobile.csv', delimiter=',',dtype="str", skip_header=True)
new_array=my_data.T
from collections import Counter
b=Counter(new_array[2]).most_common(10)
c=[]
for i in b:
    c.append(i[1])
label=["toyota","nissan","mazda","honda","mitsubishi","subaru","volkswagen","peugot","volvo","dodge"]
plt.pie(c,labels=label,explode=(0.5,0,0,0,0,0,0,0,0,0),autopct="%2.2f%%")
plt.axis('equal')

d=my_data[:,1]
for i in range(len(d)):
    if d[i] == '':
        d[i] = np.nan
        
print(d)        

d = d.astype(np.float64)
         


