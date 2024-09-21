import numpy as np
import matplotlib.pyplot as plt
#%%
#preparar la matriz
L=19
m=int((L-1)/2)
P=np.empty((L,L))
condcon=100
# llenar la matriz condiciones de frontera
for i in range(0,L):
    for j in range(0,L):
        if(j==(m-i) or j==(m+i)):
            P[i,j]=condcon
        if(i>m):
            if(j==(i-m) or j==(L-1-i+m)):
                P[i,j]=50       

# llenar matriz adentro de la placa
guess=30
for i in range(1,L-1):
    for j in range(0,L):
        if(i<=m):
            if(j>(m-i) and j<(m+i)):
                P[i,j]=guess
        if(i>m):
            if(j>(i-m) and j<(L-1-i+m)):
                P[i,j]=guess    

#%%
target = 1e-3  # Target accuracy

# Iteration (We assume that the iteration is convergence in maxIter = 500)
cont=0
error=1
diff=np.zeros((L,L))
print("Please wait for a moment")
while error>target:
    Pcopy=np.copy(P)
    for i in range(1,L-1):
        for j in range(0,L):
            if(i<=m):
                if(j>(m-i) and j<(m+i)):
                    P[i,j]=0.25*(P[i+1][j] + P[i-1][j] + P[i][j+1] + P[i][j-1])
            if(i>m):
                if(j>(i-m) and j<(L-1-i+m)):
                    P[i,j]=0.25*(P[i+1][j] + P[i-1][j] + P[i][j+1] + P[i][j-1])  
            
    for i in range(1,L-1):
        for j in range(0,L):
            if(i<=m):
                if(j>(m-i) and j<(m+i)):
                    diff[i,j]=np.abs(Pcopy[i,j]-P[i,j])
            if(i>m):
                if(j>(i-m) and j<(L-1-i+m)):
                    diff[i,j]=np.abs(Pcopy[i,j]-P[i,j])
    
    
    error=np.max(diff)
    cont+=1

print("Iteration finished")
print("el numero de interacciones fueron:",cont)

#%%

colorinterpolation = 200
colourMap = plt.cm.jet

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, L), np.arange(0, L))

# Configure the contour
plt.title("Contour of Temperature")
plt.contourf(X, Y, P, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Show the result in the plot window
plt.show()

print("")