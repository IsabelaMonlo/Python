class Estudiante:
    #metodo constructor
    def __init__(self,nombre,edad,carrera,cedula):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.cedula = cedula
    def estudiar(self):
        print(f"Hola soy el estudiante {self.nombre} y estoy estudiando {self.carrera}")
while True:
    nombre=input("Digite el nombre del estudiante: ")
    edad=input("Digite la edad: ")
    carrera=input("digite la carrera: ")
    cedula=input("Digite la cedula: ")            
    #instanciar la clase    
    estudiante=Estudiante(nombre,edad,cedula,carrera)    
    action=int(input("Desea 1.estudiar o 2.salir ?  "))#lower es para convertir cualquier string en minusculas
    if action==1:
        estudiante.estudiar()
    elif action==2:
        print("saliste del programa")
        break    