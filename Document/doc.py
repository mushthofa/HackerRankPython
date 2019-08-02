#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 01:14:48 2017

@author: mush
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

trfilename = 'trainingdata.txt'

with open(trfilename) as trfile:
    n = int(trfile.readline().strip())
    target = []
    textdata = []
    for i in range(n):
        line = trfile.readline().strip().split(" ")
        target.append(int(line[0]))
        textdata.append(" ".join(line[1:]))

k = int(input().strip())
testdata = []
for i in range(k):
        line =input().strip()
        testdata.append(line)
        
clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', LogisticRegression(C=100, penalty='l1'))])
clf.fit(textdata, target)
test_out = clf.predict(testdata)
for t in test_out:
    print(t)


#scores = cross_val_score(clf, textdata, target, cv=5)   
#print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))     
