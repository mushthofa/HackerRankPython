#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 00:26:27 2017

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


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    gpa = [float(x) for x in input().strip().split(" ")]
    corbest = 0
    ibest = -1
    for j in range(5):
        apt = [float(x) for x in input().strip().split(" ")]
        c = corr(gpa, apt)
        if(c>corbest):
            corbest = c
            ibest = j
    print(ibest+1)