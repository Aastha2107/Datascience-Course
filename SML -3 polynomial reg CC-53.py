# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:20:24 2019

@author: aastha
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("bluegills.csv")

features = dataset.iloc[:,0].values.reshape(-1,1) 
labels = dataset.iloc[:,1].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(features,labels)
score=lr.score(features,labels)

from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=2)
poly=pf.fit_transform(features)

lr2 = LinearRegression()
lr2.fit(poly,labels)
score1=lr2.score(poly,labels)
lr2.predict(pf.fit_transform(5))[0]


import matplotlib.pyplot as plt

features_grid = np.arange(min(features),max(features),0.1)
features_grid = features_grid.reshape(-1,1)
plt.plot(features,labels,color='red')


