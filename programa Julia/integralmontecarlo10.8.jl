using Printf
N=convert(Int64,1e6)
global sumf=0
global sumfxᵢgxᵢ=0
global sumfxᵢgxᵢ2=0
@time for i in (1:N)
    z=rand()
    xᵢ=z^2
    fxᵢ=xᵢ^(-1/2)/(exp(xᵢ)+1)
    gxᵢ=xᵢ^(-1/2)
    f=2/(exp(xᵢ)+1)
    global sumf+=f
    global sumfxᵢgxᵢ+=fxᵢ/gxᵢ
    global sumfxᵢgxᵢ2+=(fxᵢ/gxᵢ)^2
end
I=round(sumf/N;digits=5)
vargxᵢ=1/N*sumfxᵢgxᵢ2-(sumfxᵢgxᵢ/N)^2
σ=round(2*sqrt(vargxᵢ/N);digits=5)
@printf("la integral da como resultado I=%f±%f ",I,σ)