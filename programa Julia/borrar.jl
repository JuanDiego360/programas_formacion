using DelimitedFiles
using Statistics
n=100:1:200
resul=Array{Int64}(undef,0)
ideal=Array{Int64}(undef,0)
completo=Array{Int64}(undef,length(n),3)
for i in n
    cont=0
    for j in(1:i)
        if(rand((1:6))==6 && rand((1:6))==6)
            cont+=1
        end
    end
    push!(resul,cont)
    push!(ideal,trunc(Int64,i/36))
end
mep=round(mean(resul); digits=3)
met=round(mean(ideal); digits=3)
completo[:,1]=n
completo[:,2]=resul
completo[:,3]=ideal
#println("media practico: ",mep)
#println("media teorico: ",mep)

#plot(n,resul,label=("practico=",mep))
#plot!(n,ideal,label=("teorico=",met))
#xlabel!("lanzamientos")
#ylabel!("doble 6")
#savefig("tirada_de_dados.png")
writedlm("lanzamientos.txt",completo)