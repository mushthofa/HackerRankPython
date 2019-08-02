#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 22:42:43 2017

@author: mush
"""

import numpy as np
from sklearn import linear_model

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
regr = linear_model.LinearRegression()
regr.fit(train_x, train_y)
test_y = regr.predict(testmat)
for i in range(t):
    print("{:.2f}".format(test_y[i]))
    
