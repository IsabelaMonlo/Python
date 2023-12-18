cantidadViajerosAdultos_guajira=0
cantidadViajerosNiños_guajira=0
cantidadViajerosAdultos_cañon=0
cantidadViajerosNiños_cañon=0
cantidadViajerosAdultos_llanos=0
cantidadViajerosNiños_llanos=0
totalViajerosadultos=0
totalViajerosniños=0
totalViajerosGuajira=0
totalViajerosCañon=0
totalViajerosLlanos=0
totalDineroGuajira=0
totalDineroLlano=0
totalDineroChicamocha=0
totalDineroDestinos=0

while True:
   print("Bienvenido a nuestra agencia de viajes XYZ")
   print("Por favor Seleccione la acción que desea realizar: ")
   print("1)-Si desea cotizar nuestros viajes")
   print("2)-Si desea obtener toda la información de cotizaciones anteriores")
   print("3)-Si desea salir del programa")
   action = input()
   
   if action == '1':
        print("-----AGENCIA DE VIAJES XYZ-----")
        print("DESTINO_______________VLR PERSONA ADULTO________VLR PERSONA NIÑO")
        print("Guajira                  - 1,450,000             -870,000")
        print("Cañon del Chicamocha     - 1,600,000             -960,000")
        print("Llanos Orientales        - 1,200,000             -720,000")

        nombre = input("Nombre Del Cliente: ")
        cantidadAdultos = int(input("Ingrese la cantidad de personas adultas: "))
        cantidadNiños = int(input("Ingrese la cantidad de niños: "))
        destino = input("nombre del destino: ")
        destino= destino.lower()

        if destino == "Guajira" or destino =="guajira":
            totalAdultos=cantidadAdultos*1450000
            totalNiños=cantidadNiños*870000
            subtotal=totalAdultos+totalNiños
            cantidadViajerosAdultos_guajira +=cantidadAdultos
            cantidadViajerosNiños_guajira +=cantidadNiños
            totalViajerosGuajira += cantidadViajerosAdultos_guajira + cantidadViajerosNiños_guajira
            totalDineroGuajira += subtotal
            #imprimir cotización
            print("-------Cotización viaje a la Guajira-------")
            print("-Nombre del cliente: ", nombre)
            print("-Destino seleccionado: ", destino)
            print("-Numero de personas adultas: ",cantidadAdultos)
            print("-Numero de niños: ",cantidadNiños)
            print("El valor total a pagar es: ",subtotal)
            print("--------------------------------------------")
        elif destino == 'Cañon del Chicamocha'or destino =='cañon del chicamocha':
                totalAdultos=cantidadAdultos*1600000
                totalNiños=cantidadNiños*960000
                subtotal=totalAdultos+totalNiños
                cantidadViajerosAdultos_cañon +=cantidadAdultos
                cantidadViajerosNiños_cañon +=cantidadNiños
                totalViajerosCañon += cantidadViajerosAdultos_cañon + cantidadViajerosNiños_cañon
                totalDineroChicamocha += subtotal
                #imprimir cotización
                print("-------Cotización viaje al Cañon del Chicamocha-------")
                print("-Nombre del cliente: ", nombre)
                print("-Destino seleccionado: ", destino)
                print("-Numero de personas adultas: ",cantidadAdultos)
                print("-Numero de niños: ",cantidadNiños)
                print("El valor total a pagar es: ",subtotal)
                print("--------------------------------------------")
        elif destino== 'Llanos Orientales' or destino =='llanos orientales':
            totalAdultos=cantidadAdultos*1200000
            totalNiños=cantidadNiños*720000
            subtotal=totalAdultos+totalNiños
            cantidadViajerosAdultos_llanos +=cantidadAdultos
            cantidadViajerosNiños_llanos +=cantidadNiños
            totalViajerosLlanos += cantidadViajerosAdultos_llanos + cantidadViajerosNiños_llanos
            totalDineroLlano += subtotal
            #imprimir cotización
            print("-------Cotización viaje a los Llanos orientales-------")
            print("-Nombre del cliente: ", nombre)
            print("-Destino seleccionado: ", destino)
            print("-Numero de personas adultas: ",cantidadAdultos)
            print("-Numero de niños: ",cantidadNiños)
            print("El valor total a pagar es: ",subtotal)
            print("------------------------------------------------------")
        else :
            print("opcion ingresada no valida por mal escrita,ingrese nuevamente.")
            
   elif action == '2':
        #mostrar todas las cotizaciones realizadas anteriormente.
        totalDineroDestinos+= totalDineroChicamocha+totalDineroGuajira+totalDineroLlano
        totalViajerosadultos+= cantidadViajerosAdultos_guajira+cantidadViajerosAdultos_cañon+cantidadViajerosAdultos_llanos
        totalViajerosniños += cantidadViajerosNiños_guajira+cantidadViajerosNiños_cañon+cantidadViajerosNiños_llanos
        
        print("--------------------HISTORIAL DE COTIZACIONES----------------------- ")
        print("Cantidad de personas que viajan para la Guajira:",totalViajerosGuajira)
        print("Cantidad de personas que viajan para Cañón del Chicamocha:",totalViajerosCañon )
        print("Cantidad de personas que viajan para los llanos orientales:",totalViajerosLlanos)
        print("Total de dinero de los viajes para la Guajira:",totalDineroGuajira)
        print("Total de dinero de los viajes para Cañón del Chicamocha:",totalDineroChicamocha )
        print("Total de dinero de los viajes para los llanos orientales:",totalDineroLlano )
        print("Total de personas Adultas:",totalViajerosadultos)
        print("Total de niños:",totalViajerosniños)
        print("Total de dinero de todos los destinos:",totalDineroDestinos)
        
   elif action == '3':
        #salida del sistema
        print("Saliste del programa.")
        break
   else:
        print("Intente nuevamente")