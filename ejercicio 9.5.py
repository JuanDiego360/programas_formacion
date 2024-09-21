import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
#%%

h=1E-5 #discretización del tiempo
tf=0.025
ti=0
L=1
xi=0
nx=50 #numero de pasos en el espacio
nt=(tf-ti)/h # numero de pasos en el tiempo
a=(L-xi)/nx # discretización en el espacio step
x=np.arange(xi,L,a)
t=np.arange(ti,tf,h)
#parametros de phi
C=1
d=0.1
sigma=0.3
v=100
phi=np.zeros((len(t),len(x)))
for i in range(0,nx):
    phi[0,i]=C*(x[i]*(L-x[i]))/L**2*np.exp(-(x[i]-d)**2/(2*sigma**2))
#%%
phih=np.zeros((len(t),len(x)))
for i in range(1,len(t)):
    for j in range(1,len(x)-1):
        phih[i,j]=phih[i-1,j]+h*phi[i-1,j] #phi[t,x]
        phi[i,j]=phi[i-1,j]+h*v**2/a**2*(phih[i-1,j+1]+phih[i-1,j-1]-2*phih[i-1,j])

#%%
# acelerar simulación
tam=int(len(phih[:,0])*(0.1))
alth=np.zeros((tam,len(x)))
for i in range(0,tam):
    alth[i]=phih[i*int(len(phih)/tam)]
#%%
#simulación
fig3=plt.figure()
ax=fig3.gca()
def puntoapunto(i):
    ax.clear()
    plt.plot(x,alth[i,:])
    plt.title("simulación de la cuerda t={} ms".format(round(t[i*int(len(phih)/tam)]*1000,3)))
    plt.xlabel("longitud de la cuerda (m)")
    plt.ylabel("amplitud de la onda (m)")
    plt.grid()
    plt.ylim(-0.0005,0.0005)
    plt.xlim(0,L)
ani=animation.FuncAnimation(fig3, puntoapunto, range(len(alth)))

plt.show()

# ani.save("Simulacion_de_la_cuerda.mp4", writer="ffmpeg")

#%matplotlib
