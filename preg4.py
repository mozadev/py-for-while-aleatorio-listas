import random

numerosAleatorios=[]
for i in range(10):
    numerosAleatorios.append(random.randint(1,15))

print(numerosAleatorios)

sumaNumeros=0
for i in range(10):
    sumaNumeros=sumaNumeros+numerosAleatorios[i]

promedioNumeros=sumaNumeros/10

numeroMayor=-999
numeroMenor=999
for i in range(10):
    if(numeroMayor<numerosAleatorios[i]):
        numeroMayor=numerosAleatorios[i]

    if (numeroMenor > numerosAleatorios[i]):
        numeroMenor = numerosAleatorios[i]

print("la suma de los numero es: "+str(sumaNumeros))
print("el promedio de los numero es: "+str(promedioNumeros))
print("El numero mayor  de los numeros es: "+str(numeroMayor))
print("El numero menor de los numeros es: "+str(numeroMenor))



