

# Lista de comentarios de clientes
comentarios = [
    "  Excelente servicio ",
    "muy MALO el servicio",
    "Rápido y efectivo",
    " podría mejorar ",
    "GENIAL"
]

# Función para procesar y analizar cada comentario
def procesar_comentarios(comentarios):
    for i, comentario in enumerate(comentarios):
        # Eliminar espacios al principio y al final
        comentario = comentario.strip()

        # Convertir todo a minúsculas para un análisis uniforme
        comentario = comentario.lower()

        # Identificar y categorizar comentarios
        if "excelente" in comentario or "genial" in comentario:
            categoria = "POSITIVO"
        elif "malo" in comentario or "mejorar" in comentario:
            categoria = "NEGATIVO"
        else:
            categoria = "NEUTRAL"

        # Formatear el comentario para presentación
        comentario = comentario.capitalize()
        
        # Imprimir el comentario formateado y su categoría
        print(f"Comentario {i+1}: {comentario} (Categoría: {categoria})")

# Llamada a la función con la lista de comentarios
procesar_comentarios(comentarios)