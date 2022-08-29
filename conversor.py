# pesos = input('Tengo en moneda tica: ')
# pesos = float(pesos)
# valor_dolar = 620
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print('Tienes $' + dolares + ' dolares')

# menu = """
# Bienvenid@ al conversor de monedas:
# 1 - Pesos colombianos
# 2 - Pesos argentinos
# 3 - Pesos mexicanos
# Elige una option: 
# """
# option = input(menu)

# if option == '1':
#     pesos = int(input('Cuantos pesos colombianos tienes? '))
#     valor_dolar = 4417
# elif option == '2':
#     pesos = int(input('Cuantos pesos argentinos tienes? '))
#     valor_dolar = 138
# elif option == '3':
#     pesos = int(input('Cuantos pesos mexicanos tienes? '))
#     valor_dolar = 20
# else:
#     print('Ingresa una option correcta')

# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print('Tienes $ ' + dolares + ' dolares')

################## Whit funtions

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opción correcta por favor')
