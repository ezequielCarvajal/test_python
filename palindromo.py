def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():  # se debe de empezar con una funcion por buena practica.
    palabra = input('write a world ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print(palabra + ' It is a "palindromo"')
    else:
        print(palabra + ' It is No a "palindromo"')


if __name__ == '__main__':
    run()   # entrie point por buena practica.
