# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 08:54:58 2022

@author: juand
"""

import sympy as sp
import numpy as np
#%%
k=0.7
w=4
sol=0.1
error=1
t= sp.Symbol("t")
y=9*sp.exp(-k*t)*sp.cos(w*t)
dery=sp.diff(y,t)
while (error>0.0000001):
    a=sol
    sol=a-(y.subs(t,a))/dery.subs(t,a)
    error=np.abs((sol-a)/a)
    
print("la solución es:",round(sol,4))

