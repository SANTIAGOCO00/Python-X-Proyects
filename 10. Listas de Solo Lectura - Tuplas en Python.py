#LISTAS DE SOLO LECTURA: TUPLAS
#A diferencias de las listas las Tuplas son inmutables, es decir, los valores de las Tuplas no se pueden cambiar
#Nos ayudan a almacenar una lista de valores que son inmutables, solo los podemos optener y leer
#Las tuplas en Python pueden ser creadas dentro de los parentesis() y dentro de la secuencia deben estar separados por comas ,
#Pueden contener difrenrentes tipos de elementos (int, float, string, etc...)

#Ejemplo:
#Below is an example of creating an empty Tuple
tuple1 = () #Tuple1, Tuple2 y Tuple3 son núestras variables 
tuple2 = (1,4,6,3,9) #Tuple with values of same data type
tuple3 = ("John", 23, 56.0, True) #Tuple with values of different data types

#Ejemplo:
#Almacene los años de nacimiento de los empleados en un departamento en particular.
employees = (1984, 1995, 1998, 1976)
print(employees)
#______________________________________________________________________________________________________________________________________________________

#MANIPULACIÓN DE TUPLAS:
#Manipularemos las Tuplas usando lo siguinte...
#   Accediendo a los elemtos de una Tupla
#   Segmentación de tuplas
#   Actualizar una tupla (Esto no es posible)
#   Eliminar elementos de una tupla

#ACCEDEINDO A ELEMENTOS Y SEGMENTACIÓN DE TUPLAS:
#Al igual que las listas, podemos usar el índice para acceder a elementos de una Tupla y realizar segmentación de Tuplas.
#El indice inicia desde 0

#Ejemplo:
languages = ("Python", "Java", "Ruby", "Lisp")
print(languages)
#ACCEDIENDO A ELEMENTOS...
print(languages[0])
print(languages[2])
#PERFORMING SLICING...
print(languages[1:4])

#ACTUALIZACIÓN DE TUPLAS:
#Las tuplas son inmutables, por lo tanto sus valores no se pueden cambiar

#Ejemplo:
""" tuple1 = (1,2,3,4,5)
    tuple1[3] = 5
    print(tuple1) """ #Por lo tanto tendremos: Type Error: "Tuple" object does not support item assignement

#ELIMINAR ELEMENTOS DE UNA TUPLA:
#Dado que las tuplas son inmutables, podemos usar "del" para eliminar la tupla completa
tuple1 = (12, 56, 98)
print(tuple1)
del tuple1
#______________________________________________________________________________________________________________________________________________________

#OPERACIONES BASICAS CON TUPLAS:
#El resultado de estas operaciones es siempre una nueva tupla ya que no podemos manipular la existente. Podemos realizar las siguinte operaciones:
#   Concantenación
#   Repetición
#   Membresia

#CONCANTENACIÓN Y REPETICIÓN DE TUPLAS:
#Sumar dos tuplas es concatenación de tuplas y multiplicar una tupla es repetición

#Ejemplo:
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(tuple1+tuple2) #CONCATENACIÓN
print(tuple1*3) #REPETICIÓN

#MEMBRESIA:
#Los operadores de pertenencia como: in / not in podemos usarlos con tuplas

#Ejemplo:
names = ("Sam", "Mike", "Kane", "Nick")
print("Sam" in names) #True, ya que "Sam" esta en names
print("Sam" not in names) #False, ya que "Sam" esta en names
print("Samuel" in names) #False, ya que "Samuel" no esta en names
print("Samuel" not in names) #True, ya que "Samuel" no esta en names

#ITERANDO:
#Podemos iterar con el bucle for sobre las tuplas

#Ejemplo:
#Iterar a través de cada ciudad en la siguiente tupla
ciudades = ("London", "Tokyo", "New York")
for ciudad in ciudades:
    print(ciudad) #Imprime la ciudad en la tupla ciudades
#______________________________________________________________________________________________________________________________________________________

#FUNCIONES CON TUPLAS:
#Algunas funciones integradas que incluye Python para las tuplas son:
#   len(tuple) - Devuelve la longitud de las tuplas
#   min(tuple) - Devuelve los elemntos de las tuplas con el valor mínimo
#   max(tuple) - Devuelve los elementos de las tuplas con el valor máximo

#Ejemplo:
numbers = (3, 56, 78, 13, 98, 33)
print(len(numbers)) #Devuelve 5
print(min(numbers)) #Devuelve 3
print(max(numbers)) #Devuelve 98

#METODOS CON TUPLAS:
#   index(elements): Devuelve el índice del primer elemento coincidiente
#   coutn(elements): Devuelve el conteo de cuántas veces un elemento aparece en la tupla

#Ejemplo:
example = (23, 45, 23, 67, 89, 1)
print(example.index(23)) #Devuelve 0, el índice del primer elemento coincidiente
print(example.count(67)) #Devuelve 1, el conteo de cuántas veces un elemento aparece en la tupla
#______________________________________________________________________________________________________________________________________________________

#¿Por qué Tuple?
#Porque usamos tuplas para tipos de datos heterogéneos (different) y listas para tipos de datos homogéneos (similar)
#Dado que son inmutables iterar en una tupla es más rapido que en una lista. Aumenta el rendimiento
#Si tienes datos que no cambian, implementarlos como tupla garantiza que permanezcan protegidos
