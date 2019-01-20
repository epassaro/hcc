#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 03:06:42 2018

@author: epassaro

Simplest 'pure' Python Montecarlo approximation of Pi.
 
"""

#%%
import numpy as np
from numba import njit, prange

@njit
def mc_pi(n):
    
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)    
    
    r = x*x + y*y
    
    return 4.*r[ r <= 1 ].size/n

@njit
def parallel_mc_pi(n,m):
    
    pi_sum = 0.0
    for i in prange(m):
        pi_sum += mc_pi(n)
    
    return pi_sum/m

print('pi ≃ %.5f' % parallel_mc_pi(100000,100))