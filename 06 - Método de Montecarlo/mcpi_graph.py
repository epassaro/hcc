#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 03:29:43 2018

@author: epassaro
"""

#%%
import random
import matplotlib.pyplot as plt  

n = 10000

x = [ random.uniform(-1, 1) for i in range(n) ]
y = [ random.uniform(-1, 1) for j in range(n) ]

p = [ (a,b) for a,b in zip(x,y) if a*a + b*b <= 1]

plt.figure(figsize=(5,5))
plt.scatter(x, y, s=2)
plt.scatter(*zip(*p), s=2, c='red', label=(4.*len(p)/n))
plt.legend(loc='upper left')

plt.show()