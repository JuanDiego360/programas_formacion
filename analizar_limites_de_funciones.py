import numpy as np
def f(x,y):
    return(np.sin(x**2+y**2)/(x**2+y**2)) #se ingresa la función a analizar 

def y(theta,x):
    m=np.tan(theta*np.pi/180)
    return(m*x)
N=2
angulo=[i*N for i in range(0,90//N)]
comparar=[]
for i in range(0,len(angulo)):
    n=1
    deltax=1*10**(-n)
    yv=f(deltax,y(angulo[i],deltax))
    yn=f(deltax/10,y(angulo[i],deltax/10))
    if(yn>yv):
        while((yn/yv-1)>1E-3):
            n+=1
            deltax=1*10**(-n)
            yv=yn
            yn=f(deltax,y(angulo[i],deltax))
    elif(yv>yn):
        while((yv/yn-1)>1E-3):
            n+=1
            deltax=1*10**(-n)
            yv=yn
            yn=f(deltax,y(angulo[i],deltax))
    print(f"cuando theta es {angulo[i]} el límite tiende a: {round(yn,2)}")
    comparar.append(round(yn,2))
print("*"*14)
print("* conclusión *")
print("*"*14)
if(len(set(comparar))==1):
    print(f"el límite si existe :) y es: {comparar[0]}")
else:
    print("el límite no existe :(, porque el límite cambia conforme va cambiando el ángulo")
