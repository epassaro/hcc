#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:15:47 2018

@author: epassaro
"""

#%%

def euler(f, h, x0, y0, xf):
    
    x = [x0]
    y = [y0]
    i = 0
    
    while x[i] <= xf:
        
        x[i] = x[i] + h       
        y[i] = y[i] + h*f(x[i], y[i])
        
        x.append(x[i])
        y.append(y[i])
        
        i += 1
    
    return x,y


#%%
    
def heun(f, h, x0, y0, xf):
    
    x = [x0]
    y = [y0]
    i = 0
    
    while x[i] <= xf:
        
        x_prev = x[i]
        y_prev = y[i]       
        y_next = y[i] + h*f(x[i], y[i])
        
        x[i] = x[i] + h
        y[i] = y[i] + h/2.*(f(x_prev, y_prev)+f(x[i], y_next))
               
        x.append(x[i])
        y.append(y[i])
        
        i += 1
    
    return x,y


#%%

def rk4(f, h, x0, y0, xf):
    
    x = [x0]
    y = [y0]
    i = 0
    
    while x[i] <= xf:

        k1 = f(x[i], y[i])
        k2 = f(x[i] +0.5*h, y[i] +0.5*h*k1)
        k3 = f(x[i] +0.5*h, y[i] +0.5*h*k2)
        k4 = f(x[i] +h, y[i] +h*k3)
        
        x[i] = x[i] + h
        y[i] = y[i] + h/6.*(k1 +2.*k2 +2.*k3 +k4)
        
        x.append(x[i])
        y.append(y[i])

        i += 1

    return x,y

    
#%%
    
f = lambda x, y: 1.0 -x +4.0*y

x_eu, y_eu = euler(f, 0.05, 0., 1., 1.)
x_hn, y_hn = heun(f, 0.05, 0., 1., 1.)
x_rk, y_rk = rk4(f, 0.05, 0., 1., 1.)


#%%

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = lambda x: 0.25*x -3/16 + 19/16*np.exp(4.*x)

fig, ax = plt.subplots(figsize=(10,8))

ax.plot(x, y(x), label='Sol. analítica')
ax.scatter(x_eu, y_eu, c='orange', s=4, label='Euler')
ax.scatter(x_hn, y_hn, c='magenta', s=4, label='Heun')
ax.scatter(x_rk, y_rk, c='green', s=4, label='Runge-Kutta')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

plt.show()