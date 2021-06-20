precioXkilo=float(input("ingrese el precio por kilo de las manzanas: "))
pesoKilos=float(input("ingrese el peso en kg. de las manzanas: "))

montoApagarSinDescuento=precioXkilo*pesoKilos
if 0<=pesoKilos<=2:
    descuento=0*montoApagarSinDescuento
if 2.01<=pesoKilos<=5:
    descuento=0.1*montoApagarSinDescuento
if 5.01<=pesoKilos<=10:
    descuento=0.15*montoApagarSinDescuento
if 10.01<=pesoKilos:
    descuento=0.2*montoApagarSinDescuento

montoApagarConDescuento=montoApagarSinDescuento-descuento
print("el monto a pagar es igual : "+str(montoApagarConDescuento))



