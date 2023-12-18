#Lista de obras de arte, donde cada obra es un diccionario
obras_de_arte = [
    {"titulo": "La noche estrellada", "artista": "Vincent van Gogh", "año": 1889},
    {"titulo": "La persistencia de la memoria", "artista": "Salvador Dalí", "año": 1931},
    {"titulo": "Mona Lisa", "artista": "Leonardo da Vinci", "año": 1503},
    {"titulo": "Los jugadores de cartas", "artista": "Paul Cézanne", "año": 1892}
]

#Función para mostrar todas las obras
ver_obras = lambda obras: [print(f"Título: {obra['titulo']}, Artista: {obra['artista']}, Año: {obra['año']}") for obra in obras]

#Función para agregar una nueva obra
agregar_obra = lambda obras, titulo, artista, año: obras.append({"titulo": titulo, "artista": artista, "año": año})

#Función para buscar obras por artista utilizando una función lambda
buscar_obras_por_artista = lambda obras, artista: list(filter(lambda obra: obra['artista'] == artista, obras))

#Función para eliminar una obra por título utilizando una función lambda
eliminar_obra = lambda obras, titulo: obras.remove(next((obra for obra in obras if obra['titulo'] == titulo), None))

#Función principal
def main():
    while True:
        print("\n-Galería de Arte-")
        print("1.Ver todas las obras")
        print("2.Agregar una nueva obra")
        print("3.Buscar obras por artista")
        print("4.Eliminar obra por título")
        print("5.Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ver_obras(obras_de_arte)
        elif opcion == "2":
            titulo = input("Ingrese el título de la obra: ")
            artista = input("Ingrese el nombre del artista: ")
            año = input("Ingrese el año de creación: ")
            agregar_obra(obras_de_arte, titulo, artista, año)
            print(f"Se ha agregado la obra '{titulo}' de {artista}.")
        elif opcion == "3":
            artista = input("Ingrese el nombre del artista a buscar: ")
            obras_encontradas = buscar_obras_por_artista(obras_de_arte, artista)
            if obras_encontradas:
                ver_obras(obras_encontradas)
            else:
                print(f"No se encontraron obras de {artista}.")
        elif opcion == "4":
            titulo = input("Ingrese el título de la obra a eliminar: ")
            eliminar_obra(obras_de_arte, titulo)
            print(f"La obra '{titulo}' ha sido eliminada de la galería.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
