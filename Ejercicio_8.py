# Escribe un programa que solicite y muestre por pantalla el nombre, apellido y edad de 5 personas.

# Primero creamos una lista con llaves para almacenar los datos y para indicar la cantidad de veces que se va a repetir la operacion.

personas = 0

while (personas < 5):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
# El programa va a repetir los datos 5 veces porque declaramos en la variable while que sean igual o menor a 5.
# Se muestran los resultados en pantalla ingresados por los usuarios.
    print ("Nombre: ", nombre)
    print ("Apellido: ",apellido)
    print ("Edad: ",edad)
    
    personas+=1
else:
    print ("Las 5 personas fueron ingresadas exitosamente.")

#Fin de algoritmo.