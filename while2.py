#clave

opcion = 1
intentos_invalidos = 0

while opcion == 1:
    print("Estás dentro del ciclo.")

    # Realizar acciones dentro del ciclo
    print("Realizando acciones dentro del ciclo.")

    # Solicitar al usuario si desea continuar
    print("¿Desea continuar?")
    print("1. Sí")
    print("2. No")
    opcion = int(input("Seleccione una opción: "))

    # Validar la entrada del usuario
    while opcion != 1 and opcion != 2:
        intentos_invalidos += 1
        
        if intentos_invalidos >= 3:
            print("Clave bloqueada por 24 horas.")
            opcion = 2  # Establecer la opción a 2 para salir del bucle
            break
        
        print("APRENDA A ESCRIBIR ES 1 O 2.")
        opcion = int(input("Seleccione una opción: "))

print("Has salido del ciclo.")