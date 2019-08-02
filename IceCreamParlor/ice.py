#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:06:51 2017

@author: mush
"""
import sys

def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m

def binsearch(a, t):
    idx = sorted(range(len(a)),key=lambda x:a[x])
    asort = [a[i] for i in idx]
    ii = binary_search(asort, t)
    if(ii<0):
        return -1
    else:
        return idx[ii]


def trip(a, m):
    if(m%2==0):
        idx = []
        for [i, q] in enumerate(a):
            if(q==m/2):
                idx.append(i)
        if(len(idx)>=2):
            return idx
    for [i, q] in enumerate(a):
        j = binsearch(a, m-q)
        if(j>=0 and j!=i):
            return [i,j]
    return [-1, -1]

q = int(input().strip())
for ii in range(q):
    m = int(input().strip())
    k = int(input().strip())
    a = [int(n) for n in input().strip().split(" ")]
    [i, j] = trip(a, m)
    [i, j] = sorted([i, j])
    print("{} {}".format(i+1,j+1))
