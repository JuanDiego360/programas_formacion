using Plots
L=101
global x=convert(Int32,(L+1)/2)
global y=convert(Int32,(L+1)/2)
vecx=[x]
vecy=[y]
for i in (1:2000)
    global a=x
    global b=y

    varbool=true
    while(varbool)
        global x=a
        global y=b
        varale=rand(1:4)
        if varale==1
            y+=1
        end
        if varale==2
            y-=1
        end
        if varale==3
            x+=1
        end
        if varale==4
            x-=1
        end
        if(x==1 || x==L || y==1 || y==L)
            varbool=true
        else
            varbool=false
        end
    end
    push!(vecx,x)
    push!(vecy,y)
end

anim = @animate for i in (1:length(vecx))
    plot([vecx[i]],[vecy[i]],seriestype=:scatter)
    ylims!(0,L)
    xlims!(0,L)
    title!("movimiento Brownian")
end
gif(anim, "anim_fps60.gif", fps = 60)
