import numpy as np
I1=np.matrix([[0,0,0],[0,0,-1],[0,1,0]])
I2=np.matrix([[0,0,1],[0,0,0],[-1,0,0]])
I3=np.matrix([[0,-1,0],[1,0,0],[0,0,0]])
m=[I1,I2,I3]
a=int(input("primera matriz:"))-1
b=int(input("segunda matriz:"))-1
# a=1
# b=2
def multiplicacion(a1,b1,I1,I2,I3,m):
    for i in range(0,3):
        for j in range(0,3):
            if (a1==i and b1==j):
                mr=m[i]*m[j]
    return(mr)

R=multiplicacion(a,b,I1,I2,I3,m)
print("\[ \mathcal{I}^{(",a+1,")}\mathcal{I}^{(",b+1,")}- \mathcal{I}^{(",b+1,")}\mathcal{I}^{(",a+1,")}= \left(\\begin{array}{ccc}")
print("{} & {} & {} \\\\".format(R[0,0],R[0,1],R[0,2])) 
print("{} & {} & {} \\\\".format(R[1,0],R[1,1],R[1,2])) 
print("{} & {} & {}".format(R[2,0],R[2,1],R[2,2]))
print("\end{array} \\right)-")
R=multiplicacion(b,a,I1,I2,I3,m)
print("\left(\\begin{array}{ccc}")
print("{} & {} & {} \\\\".format(R[0,0],R[0,1],R[0,2])) 
print("{} & {} & {} \\\\".format(R[1,0],R[1,1],R[1,2])) 
print("{} & {} & {}".format(R[2,0],R[2,1],R[2,2]))
print("\end{array} \\right)=")
R=multiplicacion(a,b,I1,I2,I3,m)-multiplicacion(b,a,I1,I2,I3,m)
print("\left(\\begin{array}{ccc}")
print("{} & {} & {} \\\\".format(R[0,0],R[0,1],R[0,2])) 
print("{} & {} & {} \\\\".format(R[1,0],R[1,1],R[1,2])) 
print("{} & {} & {}".format(R[2,0],R[2,1],R[2,2]))
print("\end{array} \\right)")

for p in range(0,3):
    if(np.array_equal(R,m[p])):
        print("=\mathcal{I}^{(",p+1,")}","\]")