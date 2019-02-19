# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:16:13 2019

@author: aastha
"""

import pandas as pd
df=pd.read_csv("Cars.csv")
features=df.iloc[:,0].values
labels=df.iloc[:,1:].values
df.dtypes

obj_df = df.select_dtypes(include=['object']).copy()
li=list(df["Mileage"].isnull())
a=df["Mileage"].mean()
for i in range(len(li)):
    if(li[i]==True):
        labels["Mileage"][i]=a
        
from sklearn.cross_validation import train_test_split as tts
f_train,f_test,l_train,l_test = tts(features,labels, random_state=0, test_size=0.25)

