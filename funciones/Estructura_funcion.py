texto_global = 'texto global'

def cambio(texto:str):
    global texto_global
    texto=texto+' Hola' #concatena la palabra ' hola' a la variable texto
    print('La variable texto dentro de la funcion tiene el valor de: ')
    print(texto)
    print(f'texto global en la funcion: {texto_global}')
    
    
if __name__ == '__main__':  # llama la funcion main
    texto='ipp'
    cambio(texto) #se llama a la funcion cambio() pasandole un argumento
    print('la variable texto fuera de la funcion tiene el valor de: ')
    print(texto) #Imprime el valor de la variable texto, que sigue siendo 'ipp'
    print(f'Texto global en el main: {texto_global}') 