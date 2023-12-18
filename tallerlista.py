listaPersonas = []

while True:
    print("Bienvenido al programa de lista de personas")
    print("Por favor seleccione la acción que desea realizar:")
    print("1) Agregar persona")
    print("2) Actualizar teléfono")
    print("3) Consultar teléfono")
    print("4) Eliminar persona")
    print("5) Mostrar todas las personas")
    print("6) Salir del programa")
    action = input()

    if action == '1':
        nom = input("Ingrese el nombre a agregar: ")
        tele = input('Ingrese un teléfono: ')
        persona = (nom, tele)
        listaPersonas.append(persona)
    elif action == '2':
        actualizarvalor = input("Persona a actualizar: ")
        cel = input("Ingrese nuevo teléfono a actualizar: ")
        for i, persona in enumerate(listaPersonas):
            if persona[0] == actualizarvalor:
                listaPersonas[i] = (persona[0], cel)
                print("Lista actualizada: ", listaPersonas)
                break
        else:
            print("Persona no encontrada en la lista.")
    elif action == '3':
        print("Lista de personas:")
        for persona in listaPersonas:
            print("Nombre:", persona[0], "Teléfono:", persona[1])
        nombreid = input("Ingrese el nombre a consultar: ")
        for persona in listaPersonas:
            if persona[0] == nombreid:
                print("El teléfono consultado es:", persona[1])
                break
        else:
            print("Persona no encontrada en la lista.")
    elif action == '4':
        print("Lista de personas:")
        for persona in listaPersonas:
            print("Nombre:", persona[0], "Teléfono:", persona[1])
        nombreEliminar = input("Ingrese el nombre a eliminar: ")
        for persona in listaPersonas:
            if persona[0] == nombreEliminar:
                listaPersonas.remove(persona)
                print("La persona ha sido eliminada.")
                break
        else:
            print("Persona no encontrada en la lista.")
    elif action == '5':
        print("Lista de todas las personas:")
        for persona in listaPersonas:
            print("Nombre:", persona[0], "Teléfono:", persona[1])
    elif action == '6':
        print("Has salido del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
