



def run ():
    # pass
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    # print(mi_diccionario)

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])
    
poblacion_paises = {
    'Argentina': 44938712,
    'Brasil': 210147125,
    'Colombia': 50372424
}

#Así podemos acceder a las llaves del diccionario

for pais in poblacion_paises.keys():
    print(pais,' ', poblacion_paises[pais] )


#Así podemos acceder a los valores del diccionario
for pais in poblacion_paises.values():
    print(pais )


#Así podemos acceder tanto a los valores cómo a las llaves del diccionaro
for pais, poblacion in poblacion_paises.items():
    print(pais,' tiene ' , poblacion,' habitantes' )

if __name__ == '__main__':
        run()