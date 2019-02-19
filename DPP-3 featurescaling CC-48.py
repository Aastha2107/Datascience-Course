# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:54:18 2019

@author: aastha
"""
'''


Notice it's missing column names. Give the following column names to it 'Class label', 'Alcohol', 'Malic acid' respectively.
The features Alcohol (percent/volume) and Malic acid (g/l) are measured on different scales. So, that Feature Scaling is important prior to any comparison or combination of these data.
Perform Standardization and Min-Max scaling using sklearn module.

'''

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',
     header=None,
     usecols=[0,1,2]
    )
'''
Notice it's missing column names.
Give the following column names to it 'Class label', 'Alcohol', 'Malic acid' respectively.
'''
df.columns=["Class Label","Alcohol","Malic Acid"]
#check the null values
df.isnull().any(axis=0)
'''
The features Alcohol (percent/volume) and Malic acid (g/l) are measured on different scales. 
So, that Feature Scaling is important prior to any comparison or combination of these data.
'''
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
df["Malic Acid"]=sc.fit_transform(df["Malic Acid"])
df["Alcohol"]=sc.fit_transform(df["Alcohol"])
from sklearn.preprocessing import MinMaxScaler
m=MinMaxScaler()
df["Alcohol"]=m.fit_transform(df["Alcohol"])






