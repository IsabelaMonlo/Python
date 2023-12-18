#Lista que contiene diccionarios con Tuplas
obras_de_arte = [
    {"titulo": "La noche estrellada", "artista": "Vincent van Gogh", "año": 1889},
    {"titulo": "La persistencia de la memoria", "artista": "Salvador Dalí", "año": 1931},
    {"titulo": "Mona Lisa", "artista": "Leonardo da Vinci", "año": 1503},
    {"titulo": "Los jugadores de cartas", "artista": "Paul Cézanne", "año": 1892}
]

#Función para ver todas la galeria
def ver_obras():
    for obra in obras_de_arte:
        print(f"Título: {obra['titulo']}, Artista: {obra['artista']}, Año: {obra['año']}")

#Función para agregar una nueva obra a la galería
#Método append se utiliza para agregar un elemnto al final de la lista
def agregar_obra(titulo, artista, año):
    nueva_obra = {"titulo": titulo, "artista": artista, "año": año}
    obras_de_arte.append(nueva_obra)
    print(f"Se ha agregado la obra '{titulo}' de {artista}.")

#Función para buscar obras de un artista específico
def buscar_obras_por_artista(artista):
    obras_encontradas = []
    for obra in obras_de_arte:
        if obra['artista'] == artista:
            obras_encontradas.append(obra)
    
    if len(obras_encontradas) == 0:
        print(f"No se encontraron obras de {artista}.")
    else:
        print(f"Obras de {artista}:")
        for obra in obras_encontradas:
            print(f"Título: {obra['titulo']}, Año: {obra['año']}")

#Funcion Eliminar obra
def eliminar_obra(titulo):
    obra_encontrada = None
    
    # Buscamos la obra por título
    for obra in obras_de_arte:
        if obra['titulo'] == titulo:
            obra_encontrada = obra
            break
    
    if obra_encontrada:
        # Si se encuentra la obra, la eliminamos de la lista
        obras_de_arte.remove(obra_encontrada)
        print(f"La obra '{titulo}' ha sido eliminada de la galería.")
    else:
        print(f"No se encontró la obra '{titulo}' en la galería.")
          

# Función principal
def main():
    while True:
        print("\nGalería de Arte")
        print("1. Ver todas las obras")
        print("2. Agregar una nueva obra")
        print("3. Buscar obras por artista")
        print("4. Eliminar obra")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ver_obras()
        elif opcion == "2":
            titulo = input("Ingrese el título de la obra: ")
            artista = input("Ingrese el nombre del artista: ")
            año = input("Ingrese el año de creación: ")
            agregar_obra(titulo, artista, año)
        elif opcion == "3":
            artista = input("Ingrese el nombre del artista a buscar: ")
            buscar_obras_por_artista(artista)
        elif opcion == "4":
            artista = input("Ingrese el titulo de la obra a eliminar: ")
            eliminar_obra(titulo)
        elif opcion == "5":
            print("Bye")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
