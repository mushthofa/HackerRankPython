#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 22:11:27 2017

@author: mush
"""

import sys

red = []
green = []
blue = []
for line in sys.stdin:
    pixels = line.strip().split(" ")
    r = []
    g = []
    b = []
    for p in pixels:
        p = p.strip().split(",")
        [r1, g1, b1] = map(int, p)
        r.append(r1)
        g.append(g1)
        b.append(b1)
    red.append(r)
    blue.append(b)
    green.append(g)

bw = red
thd = 3*80
thu = 3*(255-80)
cd = 0
cn = 0
for i in range(len(red)):
    for j in range(len(red[1])):
        bw[i][j] += blue[i][j] + green[i][j]
        if(bw[i][j] >= thu):
            cd = cd + 1
        if(bw[i][j] <= thd):
            cn = cn + 1

if(cd > cn):
    print("day")
else:
    print("night")



        