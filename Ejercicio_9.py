# Escribe un programa que solicite y muestre por pantalla el nombre, apellido y edad de una cantidad de personas
# ingresadas por el usuario.

contador_personas = 0
# En este caso, el programa pregunta cuantas personas quiere registrar.
contador_personas = int(input("Ingrese la cantidad de personas que desea registrar: ",))

while (contador_personas >=1):
   
    nombre = input ("Ingrese el nombre: ")
    apellido = input ("Ingrese el apellido: ")
    edad = input("Ingrese la edad: ")
    print("Nombre: ", (nombre),", Apellido: ", (apellido), ", Edad: ",(edad))
    # En esta parte declaramos el incremento o decremento, para que no se forme un bucle infinito.
    contador_personas=contador_personas-1
    # Se muestran los datos en una linea de cada usuario.   
else:
    print("¡Los datos ingresados fueron cargados con èxito!")
# Fin de algoritmo.