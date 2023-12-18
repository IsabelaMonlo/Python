n1=int(input('ingrese primer numero: '))
n2=int(input('ingrese segundo numero: '))
funcion=lambda n1,n2: n1 if n1 > n2  else n2
print(f'el mayor es: {funcion(n1,n2)}')