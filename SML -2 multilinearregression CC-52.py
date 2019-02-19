# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:46:00 2019

@author: aastha
"""

import pandas as pd
df=pd.read_csv("iq_size.csv")
features=df.iloc[:,1:].values
labels=df.iloc[:,0].values.reshape(-1,1)
from sklearn.cross_validation import train_test_split as tts
f_train,f_test,l_train,l_test=tts(features,labels,random_state=0,test_size=.20)

from sklearn.preprocessing import StandardScaler 
sc=StandardScaler()
f_train=sc.fit_transform(f_train)
f_test=sc.transform(f_test)
l_test=sc.fit_transform(l_test)
l_train=sc.transform(l_train)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(f_train,l_train)

pred=regressor.predict([90,70,150])
score=regressor.score(f_train,l_train)

#backward elimination 
import statsmodels.formula.api as sm
import numpy as np
#add an extea colomuns as the first columns become constsnt
features=np.append(arr=np.ones((38,1)).astype(int),values = features,axis=1)
features_opt=features[:,[0,1,2,3]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()

features_opt=features[:,[0,1,2]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()


features_opt=features[:,[1,2]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()

features_opt=features[:,[1]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()

regressor.fit(features_opt,labels)
score1=regressor.score(features_opt,labels)

