import numpy as np
# a=int(input("primera matriz:"))-1
# b=int(input("segunda matriz:"))-1
# a=1-1
# b=2-1
def multiplicacion(a1,b1):
    I1=np.matrix([[0,1],[1,0]])
    I2=np.matrix([[0,-1j],[1j,0]])
    I3=np.matrix([[1,0],[0,-1]])
    m=[I1,I2,I3]
    for i in range(0,3):
        for j in range(0,3):
            if ((a1-1)==i and (b1-1)==j):
                mr=m[i]*m[j]
    return(mr)

R=multiplicacion(1,2)+multiplicacion(2,3)+multiplicacion(1,3)
print(R)