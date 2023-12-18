#nombrar la clase
class Persona:
    #constructor por persona
    def __init__(self,nombre,edad,cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
#instanciar una clase        
#persona=Persona("Juan David",18,2344)
#print(persona.nombre)
    #creando un metodo
    def caminar(self):
        print(f"Hola soy {self.nombre} y estoy caminando")    
persona=Persona("Juan David",18,2344)    
persona.caminar()  