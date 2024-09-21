nt=4/3
ni=2.5
θi=28.07248694*pi/180
if ((ni*sin(θi)/nt)<1)
    θt=asin((ni*sin(θi))/nt)
else
    θt=pi/2
end
Γp=(nt*cos(θi)-ni*cos(θt))/(nt*cos(θi)+ni*cos(θt))
Γ⊥=(ni*cos(θi)-nt*cos(θt))/(ni*cos(θi)+nt*cos(θt))
τp=(2*ni*cos(θi))/(nt*cos(θi)+ni*cos(θt))
τ⊥=(2*ni*cos(θi))/(ni*cos(θi)+nt*cos(θt))
R=round(Γp^2; digits=2)
T=round((nt*cos(θt))/(ni*cos(θi))*τp^2, digits=2)
println("τ⊥=",τ⊥)
println("τp=",τp)
println("Γ⊥=",Γ⊥)
println("Γp=",Γp)
println("R=",R)
println("T=",T)