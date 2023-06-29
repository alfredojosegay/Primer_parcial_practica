# Escribe un programa que calcule el promedio general de una clase.

suma_total = 0
contador_estudiantes = 0

# Le pedimos al usuario que ingrese las calificaciones de los estudiantes
while True:
    calificacion = input("Ingresa la calificación del estudiante o '1' para salir: ")
    
    # Se rompe el ciclo si el usuario ingresa '1'
    if calificacion == '1':
        break
    
    calificacion = float(calificacion)
    suma_total += calificacion
    
    contador_estudiantes += 1

if contador_estudiantes > 0:
    promedio_general = suma_total / contador_estudiantes
    print("El promedio general de la clase es:", promedio_general)
else:
    print("No se ingresaron calificaciones.")
#Fin de algoritmo.