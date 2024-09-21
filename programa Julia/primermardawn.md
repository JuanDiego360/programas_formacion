# Comparación de Julia y Python

## Python

~~~python
import numpy as np
import matplotlib.pyplot as plt
import time

h=1.0
τPbBi=3.3*60
τTlPb=2.2*60
τBiTl=46*60
τBiPb=46*60
def probabilidad(τ,h):
    p=1-2**(-h/τ)
    return(p)
pBiPb=probabilidad(τBiPb,h)
pBiTl=probabilidad(τBiTl,h)
pTlPb=probabilidad(τTlPb,h)
pPbBi=probabilidad(τPbBi,h)
tmax=20000

NT213Bi=10000
NT209Tl=0
NT209Pb=0
NT209Bi=0
tpuntos=np.linspace(0,tmax,NT213Bi)
Bi213puntos=[]
Pbpuntos=[]
Tlpuntos=[]
Bi209puntos=[]
a=time.time()
for t in tpuntos:
    Bi213puntos.append(NT213Bi)
    Tlpuntos.append(NT209Tl)
    Pbpuntos.append(NT209Pb)
    Bi209puntos.append(NT209Bi)
    decaimiento1=0
    decaimiento2=0
    decaimiento3=0
    decaimiento4=0
    numetl=0
    for i in range(0,NT209Pb):
        if np.random.random()<pPbBi:
            decaimiento1+=1
    for i in range(0,NT209Tl):
        if np.random.random()<pTlPb:
            decaimiento2+=1
    for i in range(0,NT213Bi):
        if np.random.random()<pBiPb:
            decaimiento3+=1
            if np.random.random()<0.9791:
                decaimiento4+=1
            else:
                numetl+=1
    NT213Bi-=decaimiento3
    NT209Pb+=decaimiento4-decaimiento1+decaimiento2
    NT209Tl+=numetl-decaimiento2
    NT209Bi+=decaimiento1
b=time.time()
print("tiempo de ejecución",round(b-a,5))
~~~
tiempo de ejecución de python: 22.61275 seconds
## Julia

~~~julia
using Plots

# cosntantes
h=1.0
τPbBi=3.3*60
τTlPb=2.2*60
τBiTl=46*60
τBiPb=46*60
function probabilidad(τ,h)
    p=1-2^(-h/τ)
    return(p)
end
pBiPb=probabilidad(τBiPb,h)
pBiTl=probabilidad(τBiTl,h)
pTlPb=probabilidad(τTlPb,h)
pPbBi=probabilidad(τPbBi,h)
tmax=20000

NT213Bi=10000
NT209Tl=0
NT209Pb=0
NT209Bi=0
tpuntos=0.0:h:tmax
Bi213puntos=Array{Int64}(undef,0)
Pbpuntos=Array{Int64}(undef,0)
Tlpuntos=Array{Int64}(undef,0)
Bi209puntos=Array{Int64}(undef,0)
@time for t in tpuntos
    push!(Bi213puntos,NT213Bi)
    push!(Tlpuntos,NT209Tl)
    push!(Pbpuntos,NT209Pb)
    push!(Bi209puntos,NT209Bi)
    decaimica1=0
    decaimica2=0
    decaimica3=0
    decaimica4=0
    numetl=0
    for i in (0:NT209Pb)
        if rand()<pPbBi
            decaimica1+=1
        end
    end
    
    for i in (0:NT209Tl)
        if rand()<pTlPb
            decaimica2+=1
        end
    end
    
    for i in (0:NT213Bi)
        if rand()<pBiPb
            decaimica3+=1
            if rand()<0.9791
                decaimica4+=1
            else
                numetl+=1
            end
        end
    end
    NT213Bi-=decaimica3
    NT209Tl+=numetl-decaimica2
    NT209Pb+=decaimica4+decaimica2-decaimica1
    NT209Bi+=decaimica1
end
~~~
tiempo de ejecución de Julia: 6.696168 seconds

# En conclusión es mucho mejor Julia!
![se tenia que decir](https://www.eltiempo.com/files/article_main/uploads/2019/04/12/5cb0ebe1c61aa.jpeg)