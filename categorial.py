# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 23:04:35 2019

@author: aastha
"""

import pandas as pd
df=pd.read_csv("Loan.csv")
labels=df.iloc[:,-1].values
features=df.iloc[:,:-1].values

#to check the null value in any column so there is no null no need to check the nan and mssing values treatment 
df.isnull().any(axis=0)
from sklearn.cross_validation import train_test_split as tts
f_train,f_test,L_train,L_test=tts(features,labels,random_state=0,test_size=.20)

df_obj=df.select_dtypes(include=['object']).copy()
from sklearn.preprocessing import LabelEncoder,OneHotEncoder 
le = LabelEncoder()
for i in range(1,6):
    features[:,i] = le.fit_transform(features[:,i])

la=LabelEncoder()
features[:,-1]=la.fit_transform(features[:,-1])
ohc = OneHotEncoder(categorical_features=[-1])
features = ohc.fit_transform(features).toarray()



#Categorial Data with pandas as well as sklearn
import pandas as pd

df = pd.read_csv("Data.csv")

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values
#with sklearn
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder

imp = Imputer()
features[:,1:] = imp.fit_transform(features[:,1:])

le = LabelEncoder()
features[:,0] = le.fit_transform(features[:,0])
labels = le.fit_transform(labels)

ohe = OneHotEncoder(categorical_features=[0])
features = ohe.fit_transform(features).toarray()


#with Pandas
df = df.fillna(df.mean())

for i in df.select_dtypes(include=[object]):
    df[i] = df[i].astype('category').cat.codes
    
features = df.drop("Purchased", axis=1)
labels = df["Purchased"]

features = pd.get_dummies(features,columns=["Country"])

