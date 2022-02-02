# def imp_mensaje():
#     print('Mensaje especial: ')
#     print('!Estoy aprendiendo a usar funciones¡: ')

# imp_mensaje()
# imp_mensaje()
# imp_mensaje()


def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print('Elegiste la opción ' + str(mensaje))
    print('Adios')


opcion = int(input('Elije una opcion (1,2,3): ') )

if opcion == 1:
    conversacion(opcion)
elif opcion == 2:
    conversacion(opcion)
elif opcion == 3:
    conversacion(opcion)
else:
    print("ingresa una opción correcta")


# def imp_mensaje(mensaje):
#     print(mensaje)

# imp_mensaje()
# imp_mensaje()
# imp_mensaje()