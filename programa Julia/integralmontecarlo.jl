using Printf
N=convert(Int64,1e4)
b=2; a=0; h=1 #limites de integración y la altura maxima de la función
A=(b-a)*h
global k=0
for i in (1:N)
    z=rand()
    x=2*z
    y=z
    f=(sin(1/(x*(2-x))))^2
    if (y<f)
        global k+=1
    end
end
I=k*A/N
σ=round(sqrt((I*(A-I))/N); digits=5)
@printf("la integral da como resultado I= %.5f ± %f ",I,σ)