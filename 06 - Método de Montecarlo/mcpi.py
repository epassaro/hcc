#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 03:06:42 2018

@author: epassaro

Simplest 'pure' Python Montecarlo approximation of Pi.
 
"""

#%%
import random
from numba import jit

@jit
def mc_pi(n):
    
    x = [ random.uniform(-1, 1) for i in range(n) ]
    y = [ random.uniform(-1, 1) for j in range(n) ]
    
    p = [ (a,b) for a,b in zip(x,y) if a*a + b*b <= 1]
    
    return 4.*len(p)/n

pi_samples = [ mc_pi(100000) for i in range(100) ]
pi_average = sum(pi_samples)/len(pi_samples)

print(pi_average)