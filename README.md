# Curso Básico de Python

# 1. **El arte de la programación**

- El arte de programar es darle instrucciones a la computadora para que resuelva un problema.
- Es una industria que está en un gran desarrollo y un gran auge.
- No se necesitan requisitos, sólo ganas de aprender.

# 2. ¿Por qué aprender Python?

Python no es el único lenguaje que se puede aprender. Sin embargo depende del artefacto que queremos construir para aplicar o adaptar el lenguaje de programación. 

Existen diferentes áreas de la tecnología que se encargan de distintos segmentos.

Python es un lenguaje clave que ayuda mucho para algunas de estás disciplinas.

- Backend
- IA
- IOT
- Data Science
- Frontend
- DevOps
- Videojuegos
- Desarrollo Móvil

## Ventajas

- Fácil
- Elegante
- Buenas practicas

# 3. **El núcleo de un programa: los algoritmos**

Un algoritmo es una serie de pasos para resolver un problema.

- Serie de passo ordenados para resolve run problema
- Finito (No es infinito)
- No ambiguo (Cada paso es particular)

Todas estas características son las que identifican a un algoritmo.

Imagina que quieres perder grasa corporal.

Debo hacer un plan no ¿?

1. Planear
2. Ejecutar
3. Repetimos el proceso

Así hasta que cumplimos nuestro objetivo. Definiendo una serie de pasos especiales.

# 4. Instalación de herramientas en Windows.

Realmente podemos usar cualquier editor para escribir nuestro código, sin embargo el más popular en la industria de la tecnología es Visual Studio Code. Es muy útil porqué ayuda a resaltar las palabras reservadas del lenguaje a detectar errores y es muy liviano al momento de utilizar.

Se recomienda usar Cmder que es un emulador de la consola.

Estas son las herramientas que vamos a usar para el curso 😃.

[https://python.org/](https://python.org/)

[https://cmder.net/](https://cmder.net/)

[https://code.visualstudio.com/](https://code.visualstudio.com/)

# 5. Instalación de herramientas en Mac

Esta es una lectura para aprender a instalar las herramientas en el entorno de Mac

# 6. Instalación de herramientas en Ubuntu

Esta es una lectura para aprender a instalar las herramientas en Ubuntu

# 7. Tu mejor herramienta: La consola

Comandos esenciales para usar en la consola:

En la consola podemos hacer las mismas cosas que en la interfaz gráfica.

`cd`  para entrar a un directorio

`cd ..` para devolverme

ej:

`cd Desktop`

Saber los archivos que están en un directorio

`ls`

Archivos en lista y ocultos`ls -la`

Crear un directorio `mkdir`

Eliminar un directorio `rmdi`

Crear un archivo `touch`

# 8. Explorando Python: Operadores aritmeticos

`2**2`

`2**5`

`5 + 5  * 2` Pendas

`2**(1/2)`

```sql
import math
round(math.sqrt(9))
```

# ¿Qué es una variable?

Una variable es un símbolo constituyente de un predicado, formula o algoritmo que se designa dentro y fuera del ámbito matemático para tomar diferentes valores.

Es cómo una caja en donde se pueden guardar objetos. Se pueden guardar cosas, esta variable o caja tienen nombres llamados identificadores.

En python es posible asignar variables con el simbolo de `=`

## Reglas para escribir de forma correcta las variables

- Una variable es una “caja” o lugar en donde puedo guardar objetos: números texto, etc.
- El identificador de mi variable no puede comenzar con un número y debe estar en minúsculas. Las palabras dentro del mismo se separan con guion bajo. (Snakecase).
- También es posible leer el PEP que define una serie de reglas para escribir el código de una forma legible y organizada.

# Los primitivos: tipos de datos sencillos

- Números enteros
- Números de punto o coma flotante
- Texto ( Cadenas de caracteres )
- Booleanos puede ser verdadero o falso

```python
nombre = "Cristian Camilo Correa Barrera"
nombre * 4 

salario = 90000.213
edad = 37

estudiante = True
etudiante = False
```

# 11. Convertir un dato a un tipo diferente

```python
numero1 = input("Escribe un número: ")
numero2 = input("Escribe un número: ")
numero1 + numero2 
# nos concatena 
numero1 = int(numero1)
numero2 = int(numero2)
str(numero1)
int(4.5)

```

# 12. Operadores lógicos y de comparación

```python
is_student = True
work = False
is_student and work
False
is_student or work
not is_student
not work

>>> numero1 = 5
>>> numero2 = 5
>>> numero1 == numero2
>>> numero1 >= numero2
>>> numero1 > numero2
>>> numero1 <= numero2
True
```

# 13. **Tu primer programa: conversor de monedas**

Vamos a crear un programa que consiste en realizar conversión de pesos colombianos a Dolares.

La persona debe ingresar el valor en pesos y debe devolver el valor en dolares.

 

```python
pesos = input("Ingresa el valor en pesos: ")
pesos = float(pesos)

valor_dolar = 3875

dolares = pesos /  valor_dolar

dolares = round(dolares,2)

dolares = str(dolares)

print("Tienes $" + dolares + "dólares")
```

# 14. **Construyendo el camino de un programa con condicionales**

Los operadores condicionales nos permiten definir el comportamiento con nuevos caminos y reglas para una variable.

El termino `pass` me ayuda a dejar en blanco el segmento dentro de cada parte del if.

```python
edad = int(input("Escribe tu edad"))

if edad > 17:
    # pass
    print("Es mayor a 17")
else:
    # pass
    print("No es mayor de 17")
```

# 15. **Varios países en mi conversor de monedas**

Vamos a cambiar nuestro programa de conversión de monedas para agregar más opciones 😀 de países y tasas de cambio.

```python
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
```

# 16. **Aprendiendo a no repetir código con funciones.**

```python
def imp_mensaje():
    print('Mensaje especial: ')
    print('!Estoy aprendiendo a usar funciones¡: ')

imp_mensaje()
imp_mensaje()
imp_mensaje()
```

# 17. **Modularizando nuestro conversor de monedas**

Vamos a poner en practica el diseño de funciones.

Con la palabra reservada `return` podemos guardar el resultado de una función en una nueva variable.

```python
def sum(a,b):
    print('Se suman dos numeros')
    resultado =  a + b
    return resultado

sumatoria = sum(1,4)
print(sumatoria)
```

Mejoras al programa  mediante una función es posible abstraer el código que se repite mucho.

```python
def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantos pesos ' + tipo_pesos +' Tienes?: ')
    pesos = float(pesos)
    dolares = pesos /  valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dólares")

    

menu = """"
Bienvenido al conversor de monedas 💲 😀 💲

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print("Ingresa una opción correcta")
```

# 18. **Trabajando con texto: cadenas de caracteres**

Las variables de tipo string tienen bastantes métodos que nos ayuda a cambiar el comportamiento de la variable. Son funciones Built in y hacen parte del lenguaje de programación en sí.

```python
nombre = input('¿Cual es tu nombre')
nombre.upper()
nombre.lower()
nombre.capitalize()
nombre.strip()
nombre.replace('o','a')
nombre.len()
nombre[0]
nombre[1]
nombre[2]

for c in nombre:
	print(c)
```

# 18. **Trabajando con texto: slices**

Slices o rebanadas

Slice se puede usar para truncar el contenido de una variable.

```python
nombre = 'cristian camilo correa barrera'
nombre[0:1]
nombre[:3]
nombre[1:7]
#también es posible agregar otro criterio para indicar la canitdad de saltos, de a 1 de a 2 ...

nombre[1:7:2]
nombre[1:7:3]

#así podemos hacer el reverse de una cadena
#que vaya del inicio al final pero en reversa
nombre[::-1]

```

# 20. **Proyecto: palíndromo**

Vamos a crear un programa para que nos diga si una palabra es un palíndromo, es decir que se lee igual al derecho y al revés.

Es importante tener una función `run()` al inicio del código

```python
def run():
    pass
```

Punto de entrada del programa

```python
if __name__ == '_main_':
    run()
```

Una vez python encuentra esta linea de código, comienza a ejecutar todo lo que está debajo.

Es una buena practica dejar dos espacios o saltos de línea después de cada función.

```python
def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_ivertida = palabra[::-1]
    if palabra == palabra_ivertida:
        return True
    else:
        return False

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()
```

# 21. **Aprendiendo bucles**

Imaginemos que tenemos un programa que debe ejecutar varios pasos. No es viable ejecutarlo de forma manual. Entonces aquí es donde se hace uso de las estructuras de ciclos *for y while* para los casos en los que queremos repetir los pasos las veces que queramos.

```python
for n in range(1000):
    print(2**n)

contador = 0
print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)  )

contador = 1
print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)  )
```

# 22. El ciclo while

Es una estructura de control que nos ayuda a crear un bucle para un bloque de código.

```python
def run():
    CONS_LIMIT = 1000000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < CONS_LIMIT:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2)  )
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()
```

# 23. **Explorando un bucle diferente: el ciclo for**

Es otro tipo de estructura de bucle para crear de forma recursiva series o sucesiones

 

```python
#Esto crea los n primeros números
for n in range(1,1001):
    print(n)
```

Así se puede pasar un range a una lista

```python
a = list(range(1,1000))
print(a)
```

# 24. **Recorriendo un string con for**

Las variables de tipo string, funcionan como arreglos y es posible recorrerlos mediante ciclos.

```python
nombre = input('Escribr tu no nombre: ')
    for l in nombre:
        print(l)
```

# 25. **Interrumpiendo ciclos con break y continue**

Algunas veces queremos interrumpir el código o tener excepciones 

```python
for contador in range(1000):
        if contador %2 != 0:
            continue
        print(contador)
```

Otro ejemplo con la palabra brak es 

```python
for i in range(100000):
        print(i)
        if i == 5678:
            break
```

# 26. ****Proyecto: prueba de primalidad****

Vamos a crear un programa para crear una serie o sucesión de números primos.

Entonces cuando un residuo es diferente de cero, se piensa que no es primo.

```sql
# sample cases
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
def is_prime(number):
    counter = 0 
    for i in range(1, number + 1):
            if (i == 1 or i == number) and number > 1:
                continue
            if number % i != 0 :
                return True
            else:
                return False
            
    if counter == 0:
        return True
    else: 
        False
        

def run():
    number = input("Please, enter a number: ")
    numbers = number.split(',')
    
    for n in numbers:
        # print(n)
        if is_prime(int(n)):
            print( n +  ' Is prime')
        else:
            print( n  + ' Is not a prime number')

if __name__ == '__main__':
    run()
```

# 27. ****Proyecto: videojuego****

En esta clase vamos a crear un video juego que adivinará que pensará en número aleatorio y luego debo probar con diferentes números hasta encontrar el número correcto.

```sql
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
```

# 28. ****Almacenar varios valores en una variable: listas****

Una variable es cómo una caja para guardar cosas, sin embargo es posible guardar muchas cosas u objetos en estructuras de datos llamados listas. Una estructura de datos son estructuras que nos ayudan a guardar datos de diferentes tipos.

```python
# Esto es un número
numero = 4

# Esto es una lista
numeros = [1, 2, 3, 4]

#¿Cómo accedo a los elementos de una lista?

numeros[0]
numeros[1]
numeros[2]

#Las listas (en python) también pueden contener diferentes tipos de datos

lista_con_diferentes_datos = ['Hola', 1, 2, True, False]

#¿Cómo agrego objetos a una lista?

lista_con_diferentes_datos.append('Soy un nuevo string :3')

# ¿Cómo elimino objetos de una lista? 
# En la función pop se escribe el indice o la posición de lo que queremos eliminar
lista_con_diferentes_datos.pop(0)

#Como mostrar acceder a una lista mediante un ciclo

for e in lista_con_diferentes_datos:
		print(e)

#también podemos hacer reverse a los alementos de la lista  (⓿_⓿)

lista_con_diferentes_datos[::-1]
```

# 29. ****Entendiendo cómo funcionan las tuplas****

Algunas operaciones entre las listas podría sumar

```python
numeros1 = [1,2,3,4]
>>> numeros2 = [5,6,7,8] 
>>> numeros1 + numeros2
[1, 2, 3, 4, 5, 6, 7, 8]

numeros1 * 5

```

Las tuplas son un tipo de objeto estático, no es posible hacerles apend

 

Los *strings* (cadenas de caracteres) al igual que las tuplas, también son considerados por python como **inmutables**.

La única manera de modificar el contenido de una variable de tipo string, es reasignando completamente su valor. No es posible realizar cambios individuales en un índice particular.

```python
mi_tupla = (1,2,3,4,5)
mi_tupla.append(6)

# Sin embargo puedo recorrerlo y realizar diferentes operaciones con este tipo de dato
for t in mi_tupla:
	print(t)
```

# 30. ****¿Qué son los diccionarios?****

Los diccionarios son otro tipo de estructura de datos, las estructuras de datos en general son muy importantes para aprender.

```python
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
```

# 31. ****Proyecto: generador de contraseñas****

Este proyecto consiste en generar contraseñas aleatorias para poder poner en practica el uso de listas y ciclos.

```python
import random

def generate_pass():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    char_set = MAYUS + MINUS + NUMS + CHARS

    password = []

    for i in range(15):
        random_char  = random.choice(char_set)
        password.append(random_char)

    password_str =  ''.join(password)
    return password_str

def run():
    password = generate_pass()

    print('Your new password is: ' + password)

if __name__ == '__main__':
    run()
```

# 32. ****Sigue aprendiendo****

En este punto ya sabemos lo elemental y básico de python, para poder entender un poco cómo funcionan las principales estructuras de datos.