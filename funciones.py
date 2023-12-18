#funciones
def Saludar():
    print("Bienvenido a las funciones sin paramentros")
    
def SaludarName(nombre):
    print(f"Hola {nombre},Como amaneces hoy?")

def Programa(nombre,nota):
    print(f"Hola{nombre}, tienes una nota de {nota}")  
    
def ProgramaDefault(nombre,nota,programa="nuevas tecnologias"):
    print(f"Hola{nombre}, tienes una nota de {nota} en el modulo {programa}") 
    
def operaciones(a,b):
    return (a+b,a*b)         
        
#llamar funcion    
if __name__=="__main__":
    SaludarName("Isa")
    # user = "Diego Sybaja"
    # SaludarName(user)
    # Programa(nota=5.7,noombre="Santiago")
    # Programa("juan",8.9)
    ProgramaDefault("Julian",4.6)
    operaciones(6,7)