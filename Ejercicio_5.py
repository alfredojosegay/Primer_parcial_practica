# Escribe un programa que calcule el sueldo de un empleado basàndose en la cantidad de horas y muestre por pantalla
# el resultado, considerando lo siguiente:
# a. Si trabajò mas de 120hs al mes, la hora tiene un valor de $1500.
# b. Si trabajò entre 80 y 120hs por mes, la hora tiene un valor de $1300.
# c. Si trabajò menos de 80hs por mes, la hora tiene un valor de $1100.

# Solicitar al usuario la cantidad de horas trabajadas en el mes.

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))

if horas_trabajadas > 120:
    valor_hora = 1500

elif horas_trabajadas >= 80 and horas_trabajadas <= 120:
    valor_hora = 1300

else:
    horas_trabajadas < 80
    valor_hora = 1100

# Se hace el càlculo de las horas trabajadas ingresadas por el usuario.

sueldo = horas_trabajadas * valor_hora

# Por ùltimo se muestra el resultado total del sueldo del usuario.

print("El sueldo del empelado es: $", sueldo)

#Fin de algoritmo.