# Del punto anterior, y considerando que durante 12 meses el empleado trabajò las mismas cantidades de horas,
# escribre un programa que calcule el descuento anual a realizarse, considerando:
# a. Si el sueldo anual es mayor a $2.000.000, el descuento es el %5.
# b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
# c. Si el sueldo anual es menor a $1.000.000, debe aplicarse el descuento del %1.
# d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual a desconectarse
# y las horas trabajadas en todo el año.

# Solicitar al usuario que ingrese la cantidad de horas trabajadas y su sueldo bruto anual.

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en el año: "))
sueldo_bruto_anual = float(input("Ingrese su sueldo anual: "))

if sueldo_bruto_anual > 2000000:
    descuento = sueldo_bruto_anual * 0.05

elif sueldo_bruto_anual >= 1000000 and sueldo_bruto_anual <= 2000000:
    descuento = sueldo_bruto_anual * 0.03

else:
    sueldo_bruto_anual < 1000000
    descuento = sueldo_bruto_anual * 0.01

# El programa realiza los càlculos una vez que el usuario ingresò las horas trabajadas.

sueldo_neto_anual = sueldo_bruto_anual - descuento
bonificacion_anual = sueldo_bruto_anual * 120

# Se muestran los resultados en pantalla.

print("El salario anual bruto es de: $",sueldo_bruto_anual)
print("El monto anual de bonificaciones es de: $",bonificacion_anual)
print("El monto anual a descontarse es de: $",descuento)
print("Las horas trabajadas en el año son: ",horas_trabajadas)
print("El sueldo anual neto es de: ",sueldo_neto_anual)

#Fin de algoritmo