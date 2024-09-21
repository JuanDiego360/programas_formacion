using DelimitedFiles
function energia(matrix,J)
    tam=size(matrix)[1]
    MdeColum=matrix[1:tam-1,1:end].*matrix[2:end,1:end]
    MdeFila=matrix[1:end,1:tam-1].*matrix[1:end,2:end]
    return(-J*(sum(MdeColum)+sum(MdeFila)))
end
N=20
s=ones((N,N)) #matriz
for i in (1:N)
	for j in (1:N)
		if rand()>0.5
			s[i,j]=-1
        end
    end
end

global suni=copy(s)

J=1
T=1
Kᵦ=1
Np=2 #numero de pasos
β=1/(Kᵦ*T)

Mgra=[sum(s)] #magnetización
global E1=energia(s,J)
for pasos in (1:Np)
    #elejimos una posición al azar dentro de la matriz i:fila, j:columna
    i=rand(1:N)
    j=rand(1:N)
    global s[i,j]*=-1 #cambiamos el el estado del spin
    global E2=energia(s,J) #calculamos la energia despues del giro
    global ΔE=E2-E1 # calculamos la diferencia de energia
    # ΔE<0 Decae la energia a un valor minimo por lo que se acepta
    if ΔE<0
        global E1=E2 #aceptamos el cambio
        push!(Mgra,sum(s)) #la agragamos a la magnetización
        global suni = [suni s] # agregamos al tensor Stiempo
    else
        if rand()<exp(-β*ΔE)
            global E1=E2 #aceptamos el cambio
            push!(Mgra,sum(s)) #la agragamos a la magnetización
            global suni = [suni s] # agregamos al tensor Stiempo
        else #rechazamos el cambio
            global s[i,j]*=-1 #volvemos a camabiar el estado, no hubo cambios
        end
    end
end
print(size(suni))

writedlm("Stiempo_Magnetizacion_negativa_julia.txt",suni)
writedlm("Mgra_Magnetizacion_negativa_julia.txt",Mgra)