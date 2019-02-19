# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:18:13 2019

@author: aastha
"""

import pandas as pd
df=pd.read_csv("affairs.csv")
feature=df.iloc[:,0:8]
label=df.iloc[:,8]
'''
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[6,7])
feature=ohe.fit(feature)
'''
feature=pd.get_dummies(feature,columns=["occupation"])
feature=pd.get_dummies(feature,columns=["occupation_husb"])

from sklearn.cross_validation import train_test_split
f_train,f_test,l_train,l_test=train_test_split(feature,label, test_size=.25,random_state=0)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(random_state=0)
lr.fit_transform(f_train,l_train)
print(lr.score(f_train,l_train))
labels=(lr.predict(f_test))

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(l_test,labels)

#What percentage of total women actually had an affair?
women_affair=0
a=label.values!=0
for i in a:
    if(i==True):
        women_affair=women_affair+1
        
actual_affair=(women_affair/len(label))*100

print(lr.predict([3,25,3,1,4,16,0,0,0,1,0,0,0,1,0,0,0,0]))


#optimum Level

from sklearn.linear_model import LinearRegression
Rr=LinearRegression()
Rr.fit(f_train,l_train)
lab=Rr.score(f_train,l_train)

import statsmodels.formula.api as sm
import numpy as np
feature = np.append(arr = np.ones((6366,1)).astype(int),values=feature,axis=1)

features_opt=feature[:,[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]]
regressor_OLS=sm.OLS(endog=label,exog=features_opt).fit()
regressor_OLS.summary()


features_opt=feature[:,[0,1, 2, 3, 4, 5, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]]
regressor_OLS=sm.OLS(endog=label,exog=features_opt).fit()
regressor_OLS.summary()

features_opt=feature[:,[0,1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]]
regressor_OLS=sm.OLS(endog=label,exog=features_opt).fit()
regressor_OLS.summary()
features_opt=feature[:,[0,1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]]
regressor_OLS=sm.OLS(endog=label,exog=features_opt).fit()
regressor_OLS.summary()

features_opt=feature[:,[0,1, 2, 3, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]]
regressor_OLS=sm.OLS(endog=label,exog=features_opt).fit()
regressor_OLS.summary()

features_opt=feature[:,[0,1, 2, 3,8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]]
regressor_OLS=sm.OLS(endog=label,exog=features_opt).fit()
regressor_OLS.summary()

features_opt=feature[:,[0,1, 2, 3, 9, 10, 11, 12, 13, 14, 15, 16, 17,18]]
regressor_OLS=sm.OLS(endog=label,exog=features_opt).fit()
regressor_OLS.summary()

features_opt=feature[:,[0,1, 2, 3, 9, 11, 12, 13, 14, 15, 16, 17,18]]
regressor_OLS=sm.OLS(endog=label,exog=features_opt).fit()
regressor_OLS.summary()

