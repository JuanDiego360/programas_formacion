# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:38:03 2022

@author: juand
"""

import numpy as np
import math

#%%

# necesitamos una funcion que pinte (rellene de 1's las posiciones de la matriz)
# array es la array 2D que debemos rellenar de 1's segÃºn la figura de un circulo
def pinta(array,listaCoordenadasX,listaCantidadDeCeldasYAPintar): 

    centerY = int((len(array)-1)/2)

    for x,cantidadCeldasYAPintar in zip(listaCoordenadasX,listaCantidadDeCeldasYAPintar):
        r = range(0,int(cantidadCeldasYAPintar) + 1,1)
        for celda in r:
            #por lo de +- de la solucion
            array[centerY+celda][x] = 100
            array[centerY-celda][x] = 100


def circleMask(rad,radOffset):

    #pasamos el radio a entero
    radAsInt =int(round(float(rad),1))
    #damos un offset al radio para ver bien el circulo en la array bidimensional
    radOffsetAsInt =int(round(float(radOffset),1))
    #obtenemos el centro de la matriz (en X. En Y es igual, pero aqui no lo necesitamos)
    centerX = radAsInt + radOffsetAsInt   

    # En base a lo anterior calculamos el diametro del circulo
    # hacemos el diametro del circulo un numero impar para conseguir simetria
    # con respecto asl centro de la matriz
    d = radAsInt*2+1
    dOffset = radOffsetAsInt*2

    #devuelve matriz de 0's
    mask = np.zeros((d+dOffset,d+dOffset),np.uint8) 

    #En este for calculamos, haciendo un barrido en x el valor que debe tomar y.
    #Todo en base a la formula de un circulo (radAsInt+0.5)**2 = x**2 + y**2 centrado en 0,0
    #El valor de +-y se interpreta como la cantidad de celdas de la matriz que deben ser pintadas para
    #cada valor de x.

    listaCoordenadasX = list()
    listaCantidadDeCeldasAPintar = list()

    #rango para la obtencion de las x para el barrido
    r = range(-(radAsInt),(radAsInt)+1,1)

    for x in r:

        #y = +-math.sqrt((radAsInt+0.5)**2 - x**2 + y**2)
        y = math.sqrt(((radAsInt)**2)-(x**2))
        #correccion del centro en X a nuestro sistema matricial 
        xbis = centerX+x
        listaCoordenadasX.append(xbis)
        listaCantidadDeCeldasAPintar.append(y)

    #poblamos la array 2D para cada valor de xbis con el valor de y obtenido
    pinta(mask,listaCoordenadasX,listaCantidadDeCeldasAPintar)


    return mask

radius = 5
radiusOffset = 1
V=circleMask(radius,radiusOffset)
Vr=np.zeros(np.shape(V))
Ttiempo=np.zeros((np.shape(V)[0],np.shape(V)[1],1))
for i in range(1,2*radius+2):
    for j in range(1,2*radius+2):
        if (V[i,j-1]!=0 and V[i,j+1]!=0 and V[i-1,j]!=0 and V[i+1,j]!=0):
            Vr[i,j]=-90
V=V+Vr