# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:13:34 2019

@author: aastha
"""
import pandas as pd
df=pd.read_csv("Automobile.csv")
# so we use fillna to fill the nan values
for i in df:
    df[i]=df[i].fillna(df[i].mode()[0])


#print datatypes
print(df.dtypes)
#print columns only having objectg type data
df_obj=df.select_dtypes(include=['object'])
#find the nan values and fill it with the most occuring values
#to find the colums having nan values 
'''column wise check occur when the axis=[0]
or when axis =[1] rowwise check occur'''
df.isnull().any(axis=0)

from sklearn.preprocessing import Imputer,LabelEncoder
le = LabelEncoder()
for i in df_obj:
    df[i] = le.fit_transform(df[i])
    # le.inverse_transform(df["body_style"])

'''for i in df_obj:
    imp = Imputer(missing_values="NaN", strategy="most_frequent",axis=0)
    imp = imp.fit(df_obj[i])
    df_obj[i] = imp.transform(df_obj[i])
    
    point to ponder:
        imputer onluy works for numeric values
    
'''
from sklearn.preprocessing import OneHotEncoder
ohc=OneHotEncoder()
ohc = OneHotEncoder(categorical_features=[7,6])

df = ohc.fit_transform(df).toarray()

