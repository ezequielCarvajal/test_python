import random

def run():
    vidas = 5
    numero_ramdon = random.randint(1,100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    while numero_elegido != numero_ramdon:
        if numero_elegido < numero_ramdon:
            vidas -= 1
            print('El numero es mas grande ' + 'Vidas: '+ str(vidas))
        elif numero_elegido > numero_ramdon:
            vidas -= 1
            print('El numero es más pequeño ' + 'Vidas: '+ str(vidas))
        if vidas <= 0:
            print('Game over!')
            break
        numero_elegido = int(input('Elige otro numero: '))
    if numero_elegido == numero_ramdon:
        print('You win!!')


if __name__ == '__main__':
    run()