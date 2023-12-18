
#Funcion normal
def suma(nro1,nro2):
    return nro1+nro2

def resta():
    pass

#funcion lambda
sumando=lambda nro1,nro2:nro1*nro2

if __name__=="__main__":
    # print(suma(123,678))
    n1=int(input("Ingrese numero uno: "))
    n2=int(input("Ingrese numero dos: "))
    #print(suma(n1,n2))
    
    #resultado de funcion lambda
    print(f'Funcion lambda{sumando(n1,n2)}')
