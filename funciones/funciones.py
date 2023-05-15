# se definen las funciones para que puedan acceder
def sumar(a,b):
    c=a+b
    return c

def resta(a,b):
    c=a-b
    return c

def multiplicar(a,b):
    c=a*b
    return c

def dividir(a,b):
    c=a/b
    return c

def resto(a,b):
    c=a%b
    return c

def elevar(a,b):
    c=a**b
    return c


# con el main llamamos a las funciones definidas
if __name__ == "__main__":

    numero_a = 10
    numero_b = 3

    #Invocaciond de las funciones creadas guardadas en la variable

    s=sumar(numero_a,numero_b)
    r=resta(numero_a,numero_b)
    m=multiplicar(numero_a,numero_b)
    d=dividir(numero_a,numero_b)
    mo=resto(numero_a,numero_b)
    e=elevar(numero_a,numero_b)

    #imprime os resultados
    print('La suma: ', str(s))
    print(f'la resta: {str(r)}')
    print(f'la multi: {str(m)}')
    print(f'la dividir: {str(d)}')
    print(f'la modulo(resto): {str(mo)}')
    print(f'la elevar: {str(e)}')

