# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:20:25 2019

@author: aastha
"""

import pandas as pd
df=pd.read_csv("mushrooms.csv")
features=df.iloc[:,1:]
labels=df.iloc[:,1]


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in features:
    features[i]=le.fit_transform(features[i])
labels=le.fit_transform(labels)
from sklearn.cross_validation import train_test_split as tts
f_train,f_test,l_train,l_test=tts(features,labels,random_state=0,test_size=0.20)

from sklearn.neighbors import KNeighborsClassifier
classifer=KNeighborsClassifier(n_neighbors=5,p=2)
classifer.fit(f_train,l_train)


pred=classifer.predict(f_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(l_test,pred)
score=classifer.score(f_test,l_test)