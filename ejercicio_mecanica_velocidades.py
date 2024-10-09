#! usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
"""
author: Juan Diego Florez Vera

el siguiente código resuelve el siguiente ejercicio:

1. Dos piedras se arrojan verticalmente hacia arriba desde el suelo, una tiene tres veces la velocidad inicial de la otra. 
a) Si la piedra más rápida tarda 10 seg en regresar al suelo, ¿cuánto tiempo le tomará regresar a la piedra más lenta? 
b) Si la piedra más lenta alcanza una altura máxima de H, ¿a qué altura (en términos de H) llegará la piedra más rápida? Suponga caida libre
"""
g=9.8 #m/s^2
tf=10 #seg lo que tarda en llegar al suelo
vo1=g*tf/6 #m/s
vo2=3*vo1 #m/s
t1=np.linspace(0,2*vo1/g,100) #seg
t2=np.linspace(0,tf,100) #seg

# definir funcion de la posición para cualquier piedra
def hf(t,g,v):
    return(v*t-g*t**2/2)

h1=hf(t1,g,vo1) #piedra mas lenta
h2=hf(t2,g,vo2) #piedra mas rapida
hmax=max(h2)+10
fig, ax = plt.subplots()
ax.set_xlim(0, tf)
ax.set_ylim(0, hmax)

print(f"la velocidad inicial de la piedra 1 es {round(vo1,3)} m/s")
print(f"la velocidad inicial de la piedra 2 es {round(vo2,3)} m/s")
print(f"a) la piedra mas lenta le tomará regresar a tierra {round(2*vo1/g,3)} segundos.")
print(f"b) la piedra más rapida llegará a una altura de {hf(tf/2,g,vo2)/hf(vo1/g,g,vo1)} H")

# Crear las líneas para cada array
line1, = ax.plot([], [], lw=2,label="piedra 1")
line2, = ax.plot([], [], lw=2,label="piedra 2")


def animate(i):
        line1.set_data(t1[:i+1],h1[:i+1])
        line2.set_data(t2[:i+1],h2[:i+1])
        return line1,line2

# Crear la animación
ani = animation.FuncAnimation(fig, animate, frames=len(t1), interval=1)
plt.grid()
plt.title("movimiento de las dos piedras")
plt.xlabel("tiempo (seg)")
plt.ylabel("altura (m)")
plt.legend()
plt.show()
