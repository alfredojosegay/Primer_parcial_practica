# Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no
# hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas.
suma_total = 0
contador_estudiantes = 0

while True:
    calificacion = input("Ingresa la calificación del estudiante o '1' para salir: ")
    
    # Se rompe el ciclo si el usuario ingresa '1'.
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
