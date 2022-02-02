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