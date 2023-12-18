#Ejercicio While 

respuesta = 1

while respuesta == 1:
    respuesta = int (input ("1. Si \n 2.No\n Escriba el nro para continuar: "))
    while respuesta != 1 and respuesta !=2:
        print("usted digitó mal")
    respuesta = int (input ("1. Si \n 2.No\n Escriba el nro para continuar: "))     
    