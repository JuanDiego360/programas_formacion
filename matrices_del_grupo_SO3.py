import numpy as np
import pyperclip as c
I1=np.matrix([[0,0,0],[0,0,-1],[0,1,0]])
I2=np.matrix([[0,0,1],[0,0,0],[-1,0,0]])
I3=np.matrix([[0,-1,0],[1,0,0],[0,0,0]])
m=[I1,I2,I3]
es=[""]*16
a=int(input("primera matriz:"))-1
b=int(input("segunda matriz:"))-1
# a=1-1
# b=2-1
def multiplicacion(a1,b1,I1,I2,I3,m):
    for i in range(0,3):
        for j in range(0,3):
            if (a1==i and b1==j):
                mr=m[i]*m[j]
    return(mr)

R=multiplicacion(a,b,I1,I2,I3,m)
es[0]=("\[\mathcal{I}^{("+str(a+1)+")}\mathcal{I}^{("+str(b+1)+")}- \mathcal{I}^{("+str(b+1)+")}\mathcal{I}^{("+str(a+1)+")}= \left(\\begin{array}{ccc}\n")
es[1]=("{} & {} & {} \\\\ \n".format(R[0,0],R[0,1],R[0,2])) 
es[2]=("{} & {} & {} \\\\ \n".format(R[1,0],R[1,1],R[1,2])) 
es[3]=("{} & {} & {} \n".format(R[2,0],R[2,1],R[2,2]))
es[4]=("\end{array} \\right)- \n")
R=multiplicacion(b,a,I1,I2,I3,m)
es[5]=("\left(\\begin{array}{ccc}\n")
es[6]=("{} & {} & {} \\\\ \n".format(R[0,0],R[0,1],R[0,2])) 
es[7]=("{} & {} & {} \\\\ \n".format(R[1,0],R[1,1],R[1,2])) 
es[8]=("{} & {} & {} \n".format(R[2,0],R[2,1],R[2,2]))
es[9]=("\end{array} \\right)= \n")
R=multiplicacion(a,b,I1,I2,I3,m)-multiplicacion(b,a,I1,I2,I3,m)
es[10]=("\left(\\begin{array}{ccc} \n")
es[11]=("{} & {} & {} \\\\ \n".format(R[0,0],R[0,1],R[0,2])) 
es[12]=("{} & {} & {} \\\\ \n".format(R[1,0],R[1,1],R[1,2])) 
es[13]=("{} & {} & {} \n".format(R[2,0],R[2,1],R[2,2]))
es[14]=("\end{array} \\right) \n")

for p in range(0,3):
    if(np.array_equal(R,m[p])):
        es[15]=("=\mathcal{I}^{("+str(p+1)+")}"+"\]")

    if(np.array_equal(R,-m[p])):
        es[15]=("=-\mathcal{I}^{("+str(p+1)+")}"+"\]")
soluc=str()
for o in range(0,len(es)):
    soluc=soluc+es[o]
c.copy(soluc)