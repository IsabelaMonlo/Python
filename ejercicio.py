print("-----Ejercicio-----")
producto = input("Nombre producto: ")
cantidad = int(input("Ingrese la cantidad: "))
precio =  float(input("Ingrese el precio: "))
Porcentajeiva = float(input("igrese el iva: "))

subtotal = ( cantidad * precio)

if (cantidad >1 and cantidad <=10 ): 
    Iva=subtotal* (Porcentajeiva/100)
    neto = subtotal + Iva 
    print("el subtotal de la cuenta es de ",subtotal," y el neto con el iva es de ",neto," y no tiene descuento.")
elif (cantidad >11 and cantidad <=20 ): 
    Iva=subtotal* (Porcentajeiva/100)
    descuento=subtotal * 7 /100
    neto = (subtotal + Iva ) - descuento
    print("el subtotal de la cuenta es de ",subtotal," y el neto con el iva y el descuento es de ",neto)  
elif (cantidad >21 and cantidad<=30 ): 
    Iva=subtotal* (Porcentajeiva/100)
    descuento=subtotal * 13 /100
    neto = (subtotal + Iva ) - descuento
    print("el subtotal de la cuenta es de ",subtotal," y el neto con el iva y el descuento es de ",neto) 
elif (cantidad >31 and cantidad <40 ): 
    Iva=subtotal* (Porcentajeiva/100)
    descuento=subtotal * 20 /100
    neto = (subtotal + Iva ) - descuento
    print("el subtotal de la cuenta es de ",subtotal," y el neto con el iva y el descuento es de ",neto)
elif(cantidad > 40):
    Iva=subtotal* (Porcentajeiva/100)
    descuento=subtotal * 35 /100
    neto = (subtotal + Iva ) - descuento
    print("el subtotal de la cuenta es de ",subtotal," y el neto con el iva y el descuento es de ",neto)
else:
    print("error")       
                     
                  