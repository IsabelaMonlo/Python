diccionarioPersonas = {}

while True:
    print("Bienvenido al programa de diccionario")
    print("Por favor seleccione la acción que desea realizar:")
    print("1) Agregar persona")
    print("2) Actualizar teléfono")
    print("3) Consultar teléfono")
    print("4) Eliminar persona")
    print("5) Mostrar todos los elementos del diccionario")
    print("6) Salir del programa")
    action = input()

    if action == '1':
        nom = input("Ingrese el nombre a agregar: ")
        tele = input('Ingrese un teléfono: ')
        diccionarioPersonas[nom] = tele
    elif action == '2':
        actualizarvalor = input("Persona a actualizar: ")
        cel = input("Ingrese nuevo teléfono a actualizar: ")
        diccionarioPersonas[actualizarvalor] = cel
        print("Diccionario actualizado: ", diccionarioPersonas)
    elif action == '3':
        print("Diccionario: ", diccionarioPersonas)
        nombreid = input("Persona a consultar: ")
        if nombreid in diccionarioPersonas:
            nombre = diccionarioPersonas[nombreid]
            print("El teléfono consultado es:", nombre)
        else:
            print("Persona no encontrada en el diccionario.")
    elif action == '4':
        print("Diccionario: ", diccionarioPersonas)
        nombreEliminar = input("Ingrese el nombre a eliminar: ")
        if nombreEliminar in diccionarioPersonas:
            diccionarioPersonas.pop(nombreEliminar)
            print("El elemento ha sido eliminado.")
        else:
            print("Persona no encontrada en el diccionario.")
    elif action == '5':
        print("Todos los elementos del diccionario son: ", diccionarioPersonas)
    elif action == '6':
        print("Has salido del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

    
