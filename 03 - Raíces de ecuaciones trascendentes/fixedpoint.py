#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:09:29 2018

@author: epassaro


Encontrar las primeras tres raices positivas* de la ecuación tg(x) = 2x,
con un error menor al 1 % usando cualquiera de los métodos presentados.

"""

#%%

import sys
from math import isclose, pi, tan, atan


#%%

if len(sys.argv) != 2:
    
    print("\nUsage: tan-2x.py <integer>\n")
    sys.exit()


#%%

# n = 2 # la n-ésima raíz positiva
n = int(sys.argv[1])

if n > 3:
    print('WARNING: only first three roots can be displayed in graph.')

#%%

f = lambda x: tan(x)
g = lambda theta: 2*atan(pi*2*(n-1)+theta)

#%%

def fixed_point(g, x0, rel_tol=1e-06, abs_tol=0.0, max_iter=1000):
    
    """ Iteración de punto fijo """
    
    x = [x0]
    i = 0
    
    while not isclose(x[i], g(x[i]), rel_tol=rel_tol, abs_tol=abs_tol) and i < max_iter-1:
        
        x.append(g(x[i]))
        i += 1
               
    return x


#%%
    
theta_list = fixed_point(g, 1.)
x_list = [ (i+2*(n-1)*pi)/2 for i in theta_list ]
y_list = [ f(i) for i in x_list ]


#%% Gráfico y salida

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 10, 1000)
Y = np.tan(X)
Y[:-1][np.diff(Y) < 0] = np.nan 

plt.figure(figsize=(8,8))
plt.xlim(0, 8)
plt.ylim(-12, 20)

plt.plot(X, Y, linewidth=1.25, label='$tan(x)$')
plt.plot(X, 2*X, c='r', linewidth=1., label='$2x$')
plt.scatter(x_list, y_list, color='orange', label='$x_i$', zorder=3)
plt.text(6.65, -11, 'root: ' + str(round(x_list[-1], 5)))

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')

plt.grid(linestyle=':')

plt.show()


#%%

print('n =', n, ', x =', x_list[-1], ', iters =', len(x_list))

    
    


