using Plots
NTl = 1000
NPb = 0               # Number of lead atoms
τ = 3.053*60        # Half life of thallium in seconds
h = 1.0               # Size of time-step in seconds
tmax = 1000           # Total time
μ=log(2)/τ
p=2^(-h/τ)*μ*tmax
tpoints =1:h:tmax
Tlpoints = ones(tmax)*NTl
Pbpoints = zeros(tmax)
@time for j in (1:NTl)
    global p0=-log(1-rand())
    if p0<p
        t=trunc(Int64,p0/μ)
        if(t<NTl && t>1)
            Tlpoints[t:end].-=1
            Pbpoints[t:end].+=1
        end
    end
end
plot(tpoints,Tlpoints,label="Tl")
plot!(tpoints,Pbpoints,label="Pb")