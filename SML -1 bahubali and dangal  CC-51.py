# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 18:31:44 2019

@author: aastha
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Bahubali2_vs_Dangal.csv")
features=df["Days"].values
features = features.reshape(-1,1)
labels=df.iloc[:,1:].values

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(features,labels)


label_pred=lr.predict(10)
print("collection by movies on 10 day",label_pred)
if(label_pred[0][1]>label_pred[0][0]):
    print("dangal rocks")
else:
    print("bahubali rocks")

plt.vlines(x=0,ymin=0,ymax=100)

