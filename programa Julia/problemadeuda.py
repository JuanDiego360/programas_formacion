def prestamo(Dp,C,Rp,Dinero):
    nomb=["M","D","Ju","Jo","Calle","Joel"]
    comprobar=True
    for i in nomb:
        for j in range(0,len(nomb)):
            if(Dp==i and Rp==nomb[j]):
                Dinero[nomb.index(Dp)]-=C
                Dinero[nomb.index(Rp)]+=C
                comprobar=False
    if(comprobar):
        Dinero[nomb.index(Dp)]-=C
    return(Dinero)
plata=[50,0,0,0,0,20]
print("iteracion 0")
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 1")
plata=prestamo("M",20,"D",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 2")
plata=prestamo("D",20,"Ju",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 3")
plata=prestamo("Ju",20,"Jo",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 4")
plata=prestamo("Jo",20,"Calle",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 5")
plata=prestamo("Joel",20,"M",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 6")
plata=prestamo("M",20,"D",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 7")
plata=prestamo("D",20,"Ju",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 8")
plata=prestamo("Ju",20,"Jo",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 9")
plata=prestamo("Jo",20,"M",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])
print()
print("iteracion 10")
plata=prestamo("M",20,"Joel",plata)
print("M=",plata[0])
print("D=",plata[1])
print("Ju=",plata[2])
print("Jo=",plata[3])
print("Calle=",plata[4])
print("Joel=",plata[5])