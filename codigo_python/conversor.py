menu = """"
Bienvenido al conversor de monedas 💲 😀 💲

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:
"""
opcion = int(input(menu))

if opcion == 1:

    pesos = input("Ingresa el valor en pesos: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos /  valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")

elif opcion == 2:
    pesos = input("Ingresa el valor en pesos Argentinos: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos /  valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")

elif opcion == 3:
    
    pesos = input("Ingresa el valor en pesos Méxicanos: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos /  valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")
else:
    print("Ingresa una opción correcta")




