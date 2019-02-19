# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:52:50 2019

@author: aastha
"""

import pandas as pd
df=pd.read_csv("Loan.csv")
labels=df.iloc[:,-1].values
features=df.iloc[:,:-1].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
for i in range(0,6):
    features[:,i]=le.fit_transform(features[:,i])
la=LabelEncoder()    
features[:,11]=la.fit_transform(features[:,11])
#onehotencoder
'''before that we need to perform labelencoding in the columns of the dataframe'''

ohe = OneHotEncoder(categorical_features=[11])
features = ohe.fit_transform(features).toarray()

#labelencoding of the label
lc=LabelEncoder()
labels[:,0]=lc.fit_transform(labels[:,0])
from sklearn.cross_validation import train_test_split as tts
f_train,f_test,l_train,l_test=tts(features,labels,random_state=0,test_size=.20)

'''*****************************Now With Pandas***************************************'''
feature=df.drop("Target",axis=1)
for i in feature.select_dtypes(include=[object]):
    feature[i] = feature[i].astype('category').cat.codes

feature = pd.get_dummies(feature,columns=["Property_Area"])

label=df["Target"]
label=label.astype('category').cat.codes
label=pd.get_dummies(label)
    