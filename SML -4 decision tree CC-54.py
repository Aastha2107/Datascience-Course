# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:35:02 2019

@author: aastha
"""

import pandas as pd
df=pd.read_csv("pastHires.csv")
features=df.iloc[:,:-1].values
labels=df.iloc[:,-1].values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
features[:,1]=le.fit_transform(features[:,1])
features[:,4]=le.fit_transform(features[:,4])
features[:,5]=le.fit_transform(features[:,5])
#perform onehotencoding on it 
features[:,3]=le.fit_transform(features[:,3])

labels=le.fit_transform(labels)
'''
ohe=OneHotEncoder(categorical_features=[3])
features=ohe.fit_transform(features).toarray()
'''

from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(features,labels)

score=regressor.score(features,labels)

from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor(n_estimators=300,random_state=0)
rfr.fit(features,labels)
pred=regressor.predict([10,1,4,0,1,0]).reshape(1,-1)
pred1=regressor.predict([10,0,4,1,0,1]).reshape(1,-1)
score1=rfr.score(features,labels)
