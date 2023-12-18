estudiante=("linda","Nuevas tecnologias",[4,1.7,4.9])
#imprimir
print(estudiante)
# Cantidad de elementos
print(len(estudiante))

nombre = estudiante[0]
modulo = estudiante[1]
notas = estudiante[2]

print(f"Estudiante {nombre} \nModulo {modulo} \nNotas {notas}")

print("Otra forma de escribir con un for")
for indices in estudiante:
    print(indices)