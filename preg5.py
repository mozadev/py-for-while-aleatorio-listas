n= int(input("ingrese el valor de n: "))

suma=0
for i in range(n):
    suma=suma+pow(i+1,i+1)

print("el resultado del algoritno es:" +str(suma))