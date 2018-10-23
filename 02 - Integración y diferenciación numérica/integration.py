#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:08:27 2018

@author: epassaro
"""

from math import exp, sqrt


def trapz(f, a, b, n=1000):

    """
    Regla del trapecio.

    trapz(f, a, b, n=1000)
    
    f: función a integrar
    a, b: extremos del invervalo
    n: cantidad de subdivisiones del intervalo [a,b]

    """

    h = (b-a)/n
    y_0, y_n = f(a), f(b)
    
    sigma = 0.
    for i in range(n):
        sigma += f(a + h*i)
     
    area = (h/2.)*( y_0 + y_n + 2.*sigma )
    
    return area



def simps(f, a, b, n=1000):

    """
    Regla de Simpson.

    simps(f, a, b, n=1000)
    
    f: función a integrar
    a, b: extremos del invervalo
    n: cantidad de subdivisiones del intervalo [a,b]

    """
    
    if n % 2 != 0:
        return "n must be even!"
    
    h = (b-a)/n
    y_0, y_n = f(a), f(b)
    
    y_odd, y_even = 0., 0.
    for i in range(n):

        if i % 2 == 1:
            y_odd += f(a + h*i)
        
        else:
            y_even += f(a + h*i)
     
    area = (h/3.)*( y_0 + 4.*y_odd +2.*y_even + y_n )
    
    return area


def quadgl4(f):

    """
    Cuadratura de Gauss-Legendre para n=4

    quadgl4(f)
    
    f: función a integrar


    """

    x1, x2 = 0.33981, 0.861136
    w1, w2 = 0.652145, 0.347855
    
    area = w1*f(x1) + w2*f(x2) + w1*f(-x1) + w2*f(-x2)
    

    return area


#######################################################

f = lambda x: x*exp(2*x)

res1 = trapz(f, -1., 1.)
res2 = simps(f, -1., 1.)
res3 = quadgl4(f)

print("\nintegrate -> x*exp(2x) between [-1,1]:\n")
print("     Trapz: {0:.4f}".format(res1))
print("     Simpson: {0:.4f}".format(res2))
print("     4p Gauss-Legendre: {0:.4f}".format(res3))
print()
