import random


def adivina_numero(number,random_number):
    if number < random_number:
        print("Ingresa un número más grande ")
    if number > random_number:
        print("Ingresa un número más pequeño ")


def run():
    random_number = random.randint(1,100)
    print('El número aleatorio es: ' + str(random_number) )
    number = int(input('Elige un número entre el 1 y el 100: '))
    
    contador = 0
    while random_number != number:
        adivina_numero(number,random_number)
        number = int(input('Elige Otro número: '))
        contador += 1
    print('¡Ganaste! te tomó ' +str(contador+1) + ' Pasos ¿Puedes hacerlo mejor?' )


if __name__ == '__main__':
    run()