using SymPy
@vars ρ ϕ z
resul1=integrate(integrate(integrate(ρ,(z,0,ρ)),(ϕ,0,2*π)),(ρ,0,sqrt(2)))
resul2=integrate(integrate(integrate(ρ,(z,0,sqrt(4-ρ^2))),(ϕ,0,2*π)),(ρ,sqrt(2),2))
println(resul1)
println(resul2)
println("el resultado final es:",resul1+resul2)
println("resultado que a mi me dió:",2^(5/2)/3*π+4*π/3*2^(1/2))
println("resultado que me dió en coordenadas esfericas:",8/3*sqrt(2)*π)