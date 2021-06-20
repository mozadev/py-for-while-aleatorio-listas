
kilometrosRecorridos=int(input("ingrese la cantidad de kilometros recorridos: "))

if(kilometrosRecorridos<=100):
    montoPagar=300

if(100<kilometrosRecorridos<=500):
    montoPagar=300+(kilometrosRecorridos-100)*(15)
if(kilometrosRecorridos>500):
    montoPagar=300+400*15+(kilometrosRecorridos-500)*10

montoSinImpuesto=montoPagar/1.18

print("el monto a pagar por el vehiculo sin impuesto: "+ str(montoSinImpuesto))
print("el monto a pagar por el vehiculo sin impuesto: "+ str(montoPagar))
