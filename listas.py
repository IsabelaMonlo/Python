# Creación de lista
modulos = ["Lógica","Base de Datos","HTLM5","Nuevas Tecnologias"]

#imprimir una lista
print(modulos)
print("El elemnto inicial de la lista es: ",modulos[0])
print("El último elemnto de la lista es: ",modulos[-1])

#Contar los elementos dentro de la lista
print("Número de elementos en la lista es de ", len(modulos))
print("último elementos en la lista es: ", modulos[len(modulos)-1])

#Agregar elemento al final de la lista
modulos.append('Móviles') 
print (modulos)

#Count devuelve el numero de veces que se repite un elemento
print("El numero de veces que se repite Lógica es: ",modulos.count("Lógica"))   

print("Lista ordenada")   
modulos.sort()
print(modulos)

#Imprimir la posición dentro de la lista
print ("La posición del módulo HTLM5 es :",modulos.index("HTLM5"))

#Este inserta un elemento en la posición que queramos
modulos.insert(2,"web 2")
print(modulos)

#Elimina un elemento de la posición 
modulos.pop(2)
print(modulos)

#Elimina todos los elementos de la lista
# modulos.clear()

#este lo imprime en forma de lista
for indice in modulos:
    print(indice)
