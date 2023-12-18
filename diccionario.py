
#crear diccionario anidado
agenda = {
    'contacto1':{
       'nombre': 'Andrea',
       'telefono':'3456',
       'direccion':'calle 10'},
    'contacto2':{
       'nombre': 'julian',
       'telefono':'5677',
       'direccion':'calle 5'},
    'contacto3':{
       'nombre': 'johanna',
       'telefono':'8907',
       'direccion':'calle 8'},
    'contacto4':{
       'nombre': 'patricia',
       'telefono':'5673',
       'direccion':'calle 15'},
    'contacto5':{
       'nombre': 'juan',
       'telefono':'1234',
       'direccion':'calle 13'},
    'contacto6':{
       'nombre': 'Andrea',
       'telefono':'3456',
       'direccion':'calle 10'},
    'contacto7':{
       'nombre': 'julian',
       'telefono':'5677',
       'direccion':'calle 5'},
    'contacto8':{
       'nombre': 'johanna',
       'telefono':'8907',
       'direccion':'calle 8'},
    'contacto9':{
       'nombre': 'patricia',
       'telefono':'5673',
       'direccion':'calle 15'},
    'contacto10':{
       'nombre': 'juan',
       'telefono':'1234',
       'direccion':'calle 13'},    
} 
#print(type(agenda))
#imprimientos todos los contactos
print(agenda)

#actualizar un valor
agenda['contacto10','nombre'] = 'luis'
print('valor actualizado es',agenda['contacto10','nombre'])

# Usar el método get() para acceder a un valor
nombre = agenda['contacto9'].get('nombre')
print(f"nombre obtenida usando get : {nombre}")

#obtener las keys
claves = agenda.keys()
print(f"Claves del diccionario: {list(claves)}")

#obtener los items
clave_valor = agenda.items()
print(f"Claves del diccionario: {list(clave_valor)}")

#agregar
agenda["nuevo"]={'nombre':'mario'} #crea una nueva clave y asigna valores al nuevo elemento