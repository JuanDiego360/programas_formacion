# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:48:17 2022

@author: juand
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#%%

#preparar la matriz
L=71
# di=(L-1)/2
m=int((L-1)/2)
P=np.zeros((L-m+1,L))
Ttiempo=np.zeros(((L-m+1,L,1)))
condcon=100
# llenar la matriz condiciones de frontera
for i in range(0,L-m+1):
    for j in range(0,L):
        if(j==(m-i) or j==(m+i)):
            P[i,j]=50
            Ttiempo[i,j,0]=P[i,j]
        if(i==(L-m)):
            P[i,j]=condcon
            Ttiempo[i,j,0]=P[i,j]
# llenar matriz adentro de la placa
guess=30
for i in range(1,L-m):
    for j in range(0,L):
        if(j>(m-i) and j<(m+i)):
            P[i,j]=guess
            Ttiempo[i,j,0]=P[i,j]
#%%
target = 1e-3  # Target accuracy

# Iteration (We assume that the iteration is convergence in maxIter = 500)
cont=0
error=1
diff=np.zeros((L-m+1,L))
print("Please wait for a moment")
P = np.expand_dims(P, axis=2)
while error>target:
    Pcopy=np.copy(P)
    for i in range(1,L-m):
        for j in range(0,L):
            if(j>(m-i) and j<(m+i)):
                    P[i,j]=0.25*(P[i+1][j] + P[i-1][j] + P[i][j+1] + P[i][j-1])
                    
    for i in range(1,L-m):
        for j in range(0,L):
            if(j>(m-i) and j<(m+i)):
                diff[i,j]=np.abs(Pcopy[i,j]-P[i,j])
    
    error=np.max(diff)
    cont+=1
    Ttiempo = np.append(Ttiempo,P, axis=2)
print("Iteration finished")
print("el numero de interacciones fueron:",cont)

#%%
colorinterpolation = 100
colourMap = plt.cm.jet

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, L-m+1), np.arange(0, L))
#%%
# acelerar simulación
tam=int((cont+1)*1/3)
Ttimpoac=np.zeros(((L-m+1,L,tam)))
for i in range(0,tam):
    Ttimpoac[:,:,i]=Ttiempo[:,:,i*int((cont+1)/tam)]
#%%
#simulación
fig3=plt.figure()
ax=fig3.gca()
def puntoapunto(i):
    ax.clear()
    plt.title("placa triangular")
    plt.contourf(Y,X,Ttimpoac[:,:,i].T, colorinterpolation, cmap=colourMap)
ani=animation.FuncAnimation(fig3, puntoapunto, range(tam))
# ani.save("Gradiente_de_laplaca_triangular.mp4", writer="ffmpeg")
plt.show()