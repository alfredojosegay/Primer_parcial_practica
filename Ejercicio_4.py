# Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales, indicando por
# pantalla si el alumno aprobò o debe recursar la materia (se aprueba con 6).

# Solicitar las notas de los parciales al usuario.

nota1 = float(input("Ingrese la primer nota del parcial: "))
nota2 = float(input("Ingrese la segunda nota del parcial: "))
nota3 = float(input("Ingrese la tercer nota del parcial: "))

# Calcular el promedio final.

promedio = (nota1 + nota2 + nota3) / 3

# El programa mostrarà al usuario los resultados, si aprobò o debe recursar la materia.

if promedio >= 6:
    print("Su promedio es: ",promedio, " felicidades, usted aprobò la materia.")
else:
    print("Su promedio es: ",promedio, " Lo siento, usted debe recursar la materia.")

# Fin de algoritmo.