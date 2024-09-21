using Symbolics
@variables x
global sol=0.2
global error=1
f=x*exp(x)-1
drf=Symbolics.derivative(f, x)
while(error>0.01)
    ant=sol
    global sol=sol-substitute(f, Dict([x =>sol]))/(substitute(drf, Dict([x => sol])))
    global error=abs(ant-sol)/sol
end
print("la solucion es:",sol)