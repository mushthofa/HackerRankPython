#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 23:35:02 2017

@author: mush
"""

import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

[k, n] = map(int, input().strip().split(" "))
trainmat = []
for i in range(n):
    rowtrain =[float(a) for a in  input().strip().split(" ")]
    trainmat.append(rowtrain)

t = int(input().strip())
testmat = []
for i in range(t):
    rowtest = [float(a) for a in  input().strip().split(" ")]
    testmat.append(rowtest)

trainmat = np.array(trainmat)
train_x = trainmat[:, :k]
train_y = trainmat[:, k]

poly = PolynomialFeatures(3)
train_x = poly.fit_transform(train_x)

regr = linear_model.LinearRegression()
regr.fit(train_x, train_y)

testmat = poly.fit_transform(testmat)
test_y = regr.predict(testmat)
for i in range(t):
    print("{:.2f}".format(test_y[i]))
    