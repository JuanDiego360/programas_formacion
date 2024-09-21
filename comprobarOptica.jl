σ=4
ε=8
μ=3
ω=2
ϵₒ=1
c=1/sqrt(μ*ϵₒ)
εᵣ=ε/ϵₒ
Krp=real(ω/c*sqrt(εᵣ+σ/(ϵₒ*ω)*im)) #ingresar expresión (parte real)
println("Krp=",Krp)
k=sqrt(μ*ε*ω^2+μ*σ*ω*im)
println("Krs=",real(k))
Kip=imag(ω/c*sqrt(εᵣ+σ/(ϵₒ*ω)*im)) #ingresar expresión (parte imaginaria)
println("kip=",Kip)
println("Kis=",imag(k))
if (round(real(Krp);digits = 3)==round(real(k);digits = 3))
  println("la componente Kr está bien")
else
  println("la componente Kr está mal")
end
if (round(real(Kip);digits = 3)==round(imag(k);digits = 3))
  println("la componente Ki está bien")
else
  println("la componente Ki está mal")
end