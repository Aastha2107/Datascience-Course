# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 18:30:42 2019

@author: aastha
"""

import pandas as pd
df=pd.read_csv("Red_Wine.csv")
for i in df:
    if(i=="wine names"):
        df[i]=df[i].fillna(df[i].mode()[0])
    else:
        df[i]=df[i].fillna(df[i].mean())
df.isnull().any(axis=0)
features=df.iloc[:,:-1].values
labels=df.iloc[:,-1].values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
features[:,0]=le.fit_transform(features[:,0])
#now we have to apply onehotencoder 
ohc=OneHotEncoder(categorical_features=[0])
features=ohc.fit_transform(features).toarray()

from sklearn.cross_validation import train_test_split as tts
f_train,f_test,l_train,l_test=tts(features,labels,random_state=0,test_size=.25)
from sklearn.preprocessing import MinMaxScaler
mm=MinMaxScaler()
f_train=mm.fit_transform(f_train)
f_test=mm.transform(f_test)












