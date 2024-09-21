using LinearAlgebra
using Plots

#preparar la matriz
L=7
m=Int64((L-1)/2)
P=zeros(L-m+1,L)
condcon=100
for i in (1:(L-m+1))
    for j in (1:L)
        if(j==(m-i+2) || j==(m+i))
            P[i,j]=50
        end
        if(i==(L-m+1))
            P[i,j]=condcon
        end
    end
end
guess=30
for i in (2:L-m)
    for j in (1:L)
        if(j>(m-i+2) && j<(m+i))
            P[i,j]=guess
        end
    end
end

target = 1e-3  # Target accuracy

# Iteration (We assume that the iteration is convergence in maxIter = 500)

error=1
diff=zeros(L-m+1,L)
Pcopy=copy(P)
Puni=copy(P)
println("Por favor espere un momento, calculando solución")
put=0
while error>target
    put=put+1
    Pcopy=copy(P)
    for i in (2:L-m)
        for j in (2:L)
            if(j>(m-i+2) && j<(m+i))
                    P[i,j]=0.25*(P[i+1,j] + P[i-1,j] + P[i,j+1] + P[i,j-1])
            end
        end
    end
                    
    for i in (1:L-m)
        for j in (1:L)
            if(j>(m-i) && j<(m+i))
                diff[i,j]=abs(Pcopy[i,j]-P[i,j])
            end
        end
    end
    
    # percentage=cont/19*100
    # print("Completado:{} %".format(round(percentage,2)), end='\r')
    error=maximum(diff)
    Puni=[Puni P]
end
Ttiempo=reshape(Puni,L-m+1,L,:)
println("Solución calculada")
println("el numero de interacciones fueron:",put)
