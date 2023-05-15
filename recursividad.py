# la recursividad es una funcion que se llama a si misma

# ejemplo de fibonacci
def fibonacciSolo(num):  # esta es la funcion de un solo paso en fibonacci
    a0=0
    a1=1
    if num==0:
        return a0
    elif num ==1:
        return a1
    else:
        for i in range(2,num):
            fib=a0+a1
            a0=a1
            a1=fib
        return fib
    
def fibonacciRecursividad(num): # cuando llega al ultimo return calcula 2 veces al entrar al metodo, desglosa
    x=0
    if num <= 1:
        return num
    else:
        
        print(f'Imprime la cantidad de metodos: fibonacciRecursividad({num}-1): {fibonacciRecursividad(num-1)} y el fibonacciRecursividad({num}-2): {fibonacciRecursividad(num-2)}')
        return fibonacciRecursividad(num-1) + fibonacciRecursividad(num-2)
    
def factorial(num):
    b=0
    if num<=1:
        return 1
    else: 
        
        print(f'Imprime la funcion {num}*factorial({num}-1): {factorial(num-1)}')
        return num*factorial(num-1)
    
if __name__=='__main__':
    valor_fibonacci=5 # este valor es del ejemplo
    
    result_fibonacci=fibonacciRecursividad(valor_fibonacci)
    print('Valor de Fibonacci recursiva: ',str(result_fibonacci))
    
    #numero factorial
    valor_factorial=5
    result_factorial=factorial(valor_factorial)
    print('Resultado del factorial: ', str(result_factorial))