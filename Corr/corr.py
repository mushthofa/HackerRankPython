#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 22:22:07 2017

@author: mush
"""

from math import sqrt

def mean(a):
    return sum(a)/len(a)

def corr(a, b):
    nom = 0
    dena = 0
    denb = 0
    ma = mean(a)
    mb = mean(b)
    for i in range(len(a)):
        nom += (a[i]-ma)*(b[i]-mb)
    for i in range(len(a)):
        dena += (a[i]-ma)*(a[i]-ma)
    for i in range(len(b)):
        denb += (b[i]-mb)*(b[i]-mb)
    den = sqrt(dena)*sqrt(denb)
    return nom/den
        

a = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
b = [10, 25,  17,  11,  13,  17,  20,  13,  9,   15]
print("{:.3f}".format(corr(a,b)))