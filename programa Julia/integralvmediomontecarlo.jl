using Printf
N=convert(Int64,1e4)
b=2; a=0 #limites de integración
global sumf=0; global sumf2=0
for i in (1:N)
    z=rand()
    x=2*z
    f=(sin(1/(x*(2-x))))^2
    global sumf+=f
    global sumf2+=f^2
end
I=(b-a)/N*sumf
varf=sumf2/N-(sumf/N)^2
σ=round((b-a)*sqrt(varf/N); digits=5)
@printf("la integral da como resultado I= %.5f ± %f",I,σ)