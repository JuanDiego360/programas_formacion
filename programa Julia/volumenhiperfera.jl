using Printf
using Distributions
N=convert(Int64,10000)
global dim=convert(Int64,10)
global sumf=0

function generador(d)
    eje=zeros(d)
    for i in (1:d)
        eje[i]=rand(Uniform(-1,1))
    end
    return(eje)
end

@time for i in (1:N)
    sumd=0
    x=generador(dim)
    for j in x
        sumd+=j^2
    end
    if(sumd<=1)
        global sumf+=1
    end
end

I=round(2^dim/N*sumf,digits=3)
varf=sumf/N-sumf/N^2
σ=round(2^dim*sqrt(varf/N);digits=6)
@printf("el hipervolumen de la esfera es V=%f ± %f",I,σ)