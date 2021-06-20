

while True:
 notaExamen=int(input("ingrese la calificacion del examen escrito (0-100): "))
 if 0<=notaExamen<=100:
     break

while True:
    notaLecciones=int(input("ingrese la calificacion de lecciones (0-10): "))
    if 0<=notaLecciones<=10:
        break

while True:
    notaTareas=int(input("ingrese la calificacion de tareas (0-10): "))
    if 0 <= notaTareas <= 10:
        break

while True:
    notaLaboratorio=int(input("ingrese la calificacion del examen laboratorio (0-10): "))
    if 0 <= notaLaboratorio <= 10:
        break


calificacionFinal=notaExamen*0.6+notaExamen*0.2+notaTareas*0.15+notaLaboratorio*0.05


if 0<=calificacionFinal<=20:
    print("la calificacion final es: " + str(calificacionFinal))

else:
    print("la calificacion final debe estar entre 0 -20, vuelva ingresar las notas")




