# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 18:35:50 2019

@author: aastha
"""
import os
file=open("Auto_mpg.txt")
A=[]
B=[]
for i in file:
    A.append(i.split())
for i in A:
    B.append(" ".join(i[8:]))
import pandas as pd
df=pd.DataFrame(A)

df.drop(df.columns[8:], axis=1, inplace=True)

for i in df:
    pd.to_numeric(df[i])
df['8']=B
df.columns=[ "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ]


import pandas as pd
import numpy as np
df1=pd.read_csv("Auto_mpg.txt",sep='\s+',header=None)
df1.columns=[ "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ]
'''to check the ? value
 df1['horsepower'].loc[df1["horsepower"]=='?'].index
'''
df1=df1.replace(to_replace='?',value=np.nan)
df1["horsepower"]=df1["horsepower"].fillna(df1["horsepower"].median()).astype(np.float64)
#Display the Car Name with highest miles per gallon value
df1["car name"][df1["mpg"].loc[df1["mpg"]==[df1["mpg"].max()]].index]

features=df1.iloc[:,1:]             
labels=df1.iloc[:,0]
#from sklearn.preprocessing import LabelEncoder,OneHotEncoder
#le=LabelEncoder()
#for i in df1:
 #   df1[i]=df1[i].astype("category").cat.codes

    feautures=pd.get_dummies(features)
    labels=pd.get_dummies(labels)
    
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(feautures,labels)
score=regressor.score(feautures,labels)

from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor(n_estimators=300,random_state=0)
rfr.fit(feautures,labels)
                  
                    
    
                    
 
