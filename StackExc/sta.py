#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 13:34:42 2017

@author: mush
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
import json


trinfilename = 'testcases/input00.txt'
troufilename = 'testcases/output00.txt'
trainfile = 'training.json'


with open(trainfile) as trin:
    n = int(trin.readline().strip())
    traindata = [];
    targetdata = []
    for i in range(n):
        line = trin.readline().strip()
        json1 = json.loads(line)
        traindata.append(json1['question'] + " " + json1['excerpt'])
        targetdata.append(json1['topic'])
        
with open(trinfilename) as trin:
    n = int(trin.readline().strip())
    testin = [];
    for i in range(n):
        line = trin.readline().strip()
        json1 = json.loads(line)
        testin.append(json1['question'] + " " + json1['excerpt'])


with open(troufilename) as trou:
    testout = []
    for i in range(n):
        class1 = trou.readline().strip()
        testout.append(class1)


    
#k = int(input().strip())
#testin = []
#for i in range(k):
#        line =input().strip()
#        json1 = json.loads(line)
#        testin.append(json1['question'] + " " + json1['excerpt'])

crange = [2**i for i in range(-5, 6, 1)]
for c in crange:
    clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', LogisticRegression(C=c, penalty='l2', solver='sag', max_iter=500))])

    clf.fit(traindata, targetdata)
    testp = clf.predict(testin)
#for t in testp:
#    print(t)
#    
    acc = sum([(testp[i]==testout[i]) for i in range(len(testp))])/len(testp)
    print('c = {:.4f}, Accuracy = {:.2f}'.format(c, 100*acc))
#
#
#scores = cross_val_score(clf, traindata, targetdata, cv=5)   
#print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))     