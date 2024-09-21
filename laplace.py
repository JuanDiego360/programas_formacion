import numpy as np
import matplotlib.pyplot as plt
#%%

# Set Dimension and delta
lenX = 10 #we set it rectangular
lenY= 5

# Boundary condition
Ttop = 0 #lado derecho
Tbottom = 0 #lado izquierdo
Tleft = 0 #lado de abajo
Tright = 100 #lado de arriba

# Initial guess of interior grid
Tguess = 30

#%%

colorinterpolation = 50
colourMap = plt.cm.jet

# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

#%%

T = np.empty((lenX, lenY))
T.fill(Tguess)
# Set Boundary condition
T[0,1:lenX-1] = Ttop #0    #[fila,columna]
T[lenX-1,:] = Tbottom #0
T[:,lenY-1]= Tright #100
T[:,0] = Tleft #0

target = 1e-2  # Target accuracy

# Iteration (We assume that the iteration is convergence in maxIter = 500)
cont=0
error=1
cont=0
w=0.9
p=1
print("Please wait for a moment")
while error>target:
    # print("matriz antes de pasar por el metodo de gauss")
    # print(T)
    error=0
    for i in range(1, lenX-1, p):
        for j in range(1, lenY-1, p):
            diff=0.25*(T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])-T[i][j]
            T[i][j]=T[i][j]+(w+1)*diff
            
            if (diff>error):
                error=diff
    # print("matriz despues de ser evaluada por el metodo de gauss")
    # print(T)
    # print("error=",error)
    cont+=1

print("Iteration finished")
print(cont)

#%%

plt.title("Contour of Temperature")
plt.contourf(X,Y,T.T, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Show the result in the plot window
plt.show()

print("")

#%%
#---------------------------------------------------------
# ecuación de poisson sin aceleración
a=0.5
e0=8.85418717e-12
lenX = 10 #we set it rectangular
lenY= 10
Te=np.zeros((int(lenX/a),int(lenY/a)))
pho=np.zeros((int(lenX/a),int(lenY/a)))

pho[2,int(lenY/a)-3]=-100
pho[int(lenX/a)-3,2]=100
colorinterpolation = 50
colourMap = plt.cm.jet
# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX,a), np.arange(0, lenY,a))

cont=0
target=1e-2
error=1

while error>target:
    # print("matriz antes de pasar por el metodo de gauss")
    # print(T)
    Tecopy=np.copy(Te)
    for i in range(1, int(lenX/a)-1):
        for j in range(1, int(lenY/a)-1):
            Te[i,j]=0.25*(Te[i+1,j] + Te[i-1,j] + Te[i,j+1] + Te[i,j-1])+a**2/(4*e0)*pho[i,j]
            
    error=np.max(np.abs(Te-Tecopy))
    # print("matriz despues de ser evaluada por el metodo de gauss")
    # print(T)
    # print("error=",error)
    cont+=1

print("Iteration finished")
print(cont)

#%%

plt.title("Contour of Temperature")
plt.contourf(X,Y,Te.T, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

# Show the result in the plot window
plt.show()

print("")

#%%

a=0.5 #pasos
e0=8.85418717e-12 #permitividad electrica del vacio
lenX = 6 #we set it rectangular
lenY= 5
Te=np.zeros((int(lenX/a),int(lenY/a)))
pho=np.zeros((int(lenX/a),int(lenY/a)))
# Te.fill(5)

#ubicación de los potenciales
pho[2,int(lenY/a)-3]=100 
pho[int(lenX/a)-3,2]=100

colorinterpolation = 50
colourMap = plt.cm.jet
# Set meshgrid
X, Y = np.meshgrid(np.arange(0, lenX,a), np.arange(0, lenY,a))

cont=0
target=1e-2
error=1
w=0.9
print("Please wait for a moment")
while error>target:
    error=0
    for i in range(1, int(lenX/a)-1):
        for j in range(1, int(lenY/a)-1):
            diff=0.25*(Te[i+1][j] + Te[i-1][j] + Te[i][j+1] + Te[i][j-1])+a**2/(4*e0)*pho[i,j]-Te[i][j]
            Te[i][j]=Te[i][j]+(w+1)*diff
            
            if (diff>error):error=diff
    cont+=1

print("Iteration finished")
print("el numero de interacciones fueron:",cont)

