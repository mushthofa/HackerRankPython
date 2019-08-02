#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 22:41:43 2017

@author: mush
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score 
from sklearn import preprocessing
import numpy as np


        
[n, k] = map(int, input().strip().split(" "))

        
traindata = np.zeros(n*k).reshape(n, k)
traintarget = np.zeros(n)

for i in range(n):
    line = input().strip().split(" ")
    traintarget[i] = int(line[1])
    for j in range(k):
        ff = line[j+2].split(":")
        traindata[i, j] = float(ff[1])


m = int(input().strip())
testdata = np.zeros(m*k).reshape(m, k)
testid = []
for i in range(m):
    line = input().strip().split(" ")
    testid.append(line[0])
    for j in range(k):
        ff = line[j+1].split(":")
        testdata[i, j] = float(ff[1])

testfilename = 'output00.txt'
with open(testfilename) as trou:
    testout = []
    for i in range(m):
        class1 = trou.readline().strip().split(" ")
        testout.append(int(class1[1]))
        
# Preprocessing
scaler = preprocessing.StandardScaler().fit(traindata)
traindata = scaler.transform(traindata)
testdata = scaler.transform(testdata)


for par in range(0,8):
    clf = SVC(C=2**par, kernel='poly')
    scores = cross_val_score(clf, traindata, traintarget, cv=5)
    print("par = {:d}".format(par))
    print("CV accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))     
    
    clf.fit(traindata, traintarget)
    testp = clf.predict(testdata)
    testp = [int(t) for t in testp]
    acc = sum(testp[i] == testout[i] for i in range(len(testp)))
    posp = sum(testp[i] == 1 for i in range(len(testp)))
    negp = sum(testp[i] == -1 for i in range(len(testp)))
    print("Test accuracy: {:.2f}({:d}-{:d})".format(acc/len(testp)*100, posp, negp))
    
#for (i, t) in enumerate(testid):
#    print("{} {:+d}".format(t, int(testp[i])))
