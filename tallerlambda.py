#definicion de funciones lambda
subtotal= lambda precio,cantidad : precio * cantidad
calcDescuento = lambda variable1,descuento :(variable1*descuento/100)
calciva =lambda variable1,iva: variable1*(iva/100)
neto=lambda variable1,variabledes,variableiva:(variable1+variableiva)-variabledes
print('---------Taller---------')
producto=input("Ingrese el nombre del producto: ")
precio=float(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese la cantidad del producto: "))
descuento=float(input("Ingrese el descuento: "))
iva=float(input("ingrese el iva: "))
variable1=subtotal(precio,cantidad)
variabledes=calcDescuento(variable1,descuento)
variableiva=calciva(variable1,iva)
print(f'El subtotal es: {round (subtotal(precio,cantidad))}')
print(f'El descuento seria del : {round (calcDescuento(variable1,descuento))}')
print(f'El iva por la cantidad de productos es : {round(calciva(variable1,iva))}')
print(f'El neto a pagar es: {round(neto(variable1,variabledes,variableiva))}')

