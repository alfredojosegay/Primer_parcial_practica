# Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto
# (bruto + bonif), considerando:
# a. Si trabajò mas de 120hs, la bonificaciòn es de %18.
# b. Si trabajò entre 80hs y 120hs, la bonificaciòn es de %15.
# c. Si trabajò menos de 80 hs, la bonificaciòn es de %13.

# Solicitar al usuario las horas trabajadas.
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

if horas_trabajadas > 120:
    valor_hora = 1500
    bonificacion = valor_hora * 0.18

elif horas_trabajadas > 80 and horas_trabajadas <= 120:
    valor_hora = 1300
    bonificacion = valor_hora * 0.15

else:
    horas_trabajadas < 80
    valor_hora = 1100
    bonificacion = valor_hora * 0.13

# Se calcula el sueldo, monto a bonificar y sueldo neto dependiendo de las horas trabajadas ingresadas por el usuario.

sueldo_bruto = valor_hora * horas_trabajadas
bonificacion = sueldo_bruto * bonificacion
sueldo_neto = sueldo_bruto + bonificacion

# Se muestra por pantalla los resultados de los calculos.

print("Su sueldo bruto es: $",sueldo_bruto)
print("El monto a bonificar es: $",bonificacion)
print("Su sueldo neto es: $",sueldo_neto)

# Fin de algoritmo.