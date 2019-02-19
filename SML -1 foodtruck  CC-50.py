# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:44:24 2019

@author: aastha
"""

import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("Foodtruck.csv")
#check the null value
dataset.isnull().any(axis=0)
features=dataset["Population"].values
labels=dataset["Profit"].values

#to change the dimension it should not be !d array
features = features.reshape(-1,1)
labels=labels.reshape(-1,1)
from sklearn.cross_validation import train_test_split as tts 
f_train,f_test,l_train,l_test=tts(features,labels,random_state=0,test_size=.20)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(f_train,l_train)


label_pred=lr.predict(f_test)

Score=lr.score(f_test,l_test)



plt.scatter(f_train,l_train,color='cyan')
plt.plot(f_train,lr.predict(f_train),color='red')
plt.title("Population and Profit (trained data)")
plt.xlabel("Population")
plt.ylabel("Profit")
plt.show()

plt.scatter(f_test,l_test,color='cyan')
plt.plot(f_train,lr.predict(f_train),color='red')
plt.title("Population and Profit (test data)")
plt.xlabel("Population")
plt.ylabel("Profit")
plt.show()



'''
Based on the above trained results, what will be your estimated profit, 
if you set up your outlet in Jaipur? (Current population in Jaipur is 3.073 million)


'''
jaipur_profit=lr.predict(3.073)