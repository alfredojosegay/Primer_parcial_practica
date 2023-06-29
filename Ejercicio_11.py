# Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
# a. Si es número es par o impar.
# b. Cuanto es la suma total de todos los números mostrados.
# c. Cuanto es la suma total de todos los números pares mostrados.
# d. Cuanto es la suma total de todos los números impares mostrados.

numero = 1
suma_total = 0
suma_pares = 0
suma_impares = 0

while numero <= 10:
    print(numero)
    
    # El programa verifica si el número es par o impar.
    # Elegì la opcion " \n " para que se muenstre de forma ordenada los numeros pares o impares.
    if numero % 2 == 0:
        print("Es un número par\n")
        suma_pares += numero
    else:
        print("Es un número impar\n")
        suma_impares += numero
    
    suma_total += numero
    numero += 1

print("Suma total:", suma_total)
print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)
#Fin algoritmo.