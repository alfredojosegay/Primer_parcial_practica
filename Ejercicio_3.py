# Escribe un programa que calcule la equivalencia a pesos de dòlares ingresados por pantalla. El programa debe
# preguntar el tipo de cambio a convertir (es decir, cuanto cotiza el dòlar).

# Solicitar al usuario el precio actual de dòlar.

precio = float(input("Ingrese el precio actual del dòlar: $"))

# Solicitar al usuario el tipo de cambio.

tipo_cambio = float(input("Ingrese el tipo de cambio: $"))

# Calcular la equivalencia en pesos.

equivalencia_pesos =  precio * tipo_cambio

# Mostrar el resultado por pantalla.

print("La cantidad ingresada en dòlares equivale a: $", equivalencia_pesos)

# Fin de algoritmo.