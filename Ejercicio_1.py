# Escribe un programa que calcule la edad que cumpliò o debe cumplir este año la persona,
# basado en el año de nacimiento.

# Solicitar el año actual y el año de nacimiento al usuario.

año_actual = int(input("Ingrese el año actual: "))
año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))

# Calcular la edad.
edad = año_actual - año_de_nacimiento

#Mostrar resultado.
print ("¡Este año usted cumpliò o cumplirà", edad, "años!")

# Fin de algoritmo.