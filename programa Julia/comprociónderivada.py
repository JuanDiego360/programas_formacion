import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,np.pi,10)
y=np.sin(x)
dydxp=np.cos(x)
dydx=[]
xn=[]
for i in range(0,len(x)-1):
    dydx.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    xn.append((x[i+1]+x[i])/2)
plt.plot(x,dydxp,label="fpt(x)")
plt.plot(xn,dydx,label="fps(x)")
plt.legend()
plt.grid()
plt.show()