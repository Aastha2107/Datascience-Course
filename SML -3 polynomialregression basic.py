# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:58:41 2019

@author: aastha
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv("Position_Salaries.csv")

features = dataset.iloc[:,1:2].values 
labels = dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(features,labels)

lr.predict(6.5)[0]

from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=4)

poly_features = pf.fit_transform(features)

labels = labels.reshape(10,1)

lr2=LinearRegression()
lr2.fit(poly_features,labels)

lr2.predict(pf.fit_transform(6.5))  

lr.score(features,labels)

lr2.score(poly_features,labels)


#decision tree
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(features,labels)

labels_pred=regressor.predict(6.5)
score2=regressor.score(features,labels)

import matplotlib.pyplot as plt

features_grid = np.arange(min(features),max(features),0.1)
features_grid = features_grid.reshape(-1,1)
plt.scatter(features,labels,color='red')


