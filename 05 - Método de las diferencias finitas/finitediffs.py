#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:49:57 2018

@author: epassaro
"""

#%%

q, H = 4.0, 1.
x0, yh = 0.0, 1.

N = 20    # Cantidad de nodos equiespaciados

#%%

import numpy as np
from scipy.sparse import diags
from scipy.linalg import solve

h = (H-x0)/N

dp = (2.+h*h*q)*np.ones((1, N)) # diagonal principal
dl = -1.*np.ones((1, N-1))      # diagonal inferior
du = -1.*np.ones((1, N-1))      # diagonal superior
du[:,0] = -2.                   # cambio el primer elemento de du  

A = diags([dp,dl,du], [0, -1, 1], shape=(N,N))
B = np.zeros((1, N))
B[:,-1] = yh

X = solve(A.toarray(), B.transpose())


#%%

import matplotlib.pyplot as plt

x = np.linspace(0., H, N)
y = lambda x: yh*np.cosh(np.sqrt(q)*x)/np.cosh(np.sqrt(q)*H)

plt.figure(figsize=(8, 8))

plt.xlim(x0, H)
plt.ylim(y(0), y(yh))
plt.grid(linestyle=':')

plt.plot(x, y(x), label='Sol. analítica')
plt.plot(x, X, '.', label='Diferencias finitas')

nodestring = 'nodes: ' + str(N)
plt.text(x=0.845, y=0.275, s=nodestring)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
