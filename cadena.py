mensaje = "Bienvenido... Al curso de Python"

# metodo len, imprime el tamaño de la longitud del string contando los espacios
#print("El texto original ", mensaje)
#print("El tamaño del texto es de ", len(mensaje))

# Strip,quitos los espacios al inicio y al final del mensaje y en este caso primero va la variable y despúes el método
sinEspacios = mensaje.strip()

#print("El tamaño del texto sin espacios ", sinEspacios)
#print("El tamaño del texto sin espacios es de ", len(sinEspacios))

# UPPER es mayúsculas sostenidas 
#print("Texto en MAYÚSCULAS")
#print(sinEspacios.upper())

# LOWER es para minúsculas sostenidas
# #print("Texto en MINÚSCULAS")
# print(sinEspacios.lower())

# #TITLE es para imprimir la inicial de cada palabra en mayúscula
# print("Texto en Titulo")
# print(sinEspacios.title())

# #CAPITALIZE es para colocar la primera inicial de la palabra en mayúscula
# print("Texto con la primera inicial en mayúscula")
# print(sinEspacios.capitalize())

#SPLIT sirve para colocar los espacios
parrafo = sinEspacios.split("...")
print(parrafo[0])
print(parrafo[1])
