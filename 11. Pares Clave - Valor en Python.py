#PARES CLAVE - VALOR EN PYTHON
#Key-Value. Donde las keys son las palabras y los valores son el significado de estas palabras.

#   TAMBIEN CONOCIDOS COMO DICCIONARIOS:
#   CARACTERISTICAS DE LOS DICCIONARIOS...
#   El diccionario es una colección desordenada y mutable de elementos 
#   Cada elemento de un diccionario tiene un par de clave/valor
#   Se pueden recuperar valores cuando se conoce la clave
#   Cada clave en el diccionario es única, mientras que los valores pueden repetirse

#ESTRUCTURA DE UN DICCIONARIO
#Los valores de un diccionario pueden ser de cualquier tipo, pero las claves deben ser de un tipo de dato inmutable como cadenas, números, o tuplas.
#Cada clave está separada de su valor por un colon (:), los elementos están separados por comas, y todo está encerrado en llaves {}.

#Ejemplo:
#Below is an example of creating an empty dictionary
dict1 = {} #Creamos un diccionario vacio, donde dict1 es la variable
#Dictionary with integrer keys and string values
dict2 = {1:"john", 2:"Sam"} #Creamos un diccionario con llaves integradas y variables de tipo string

#DEFINIENDO UN DICCIONARIO:

#Ejemplo:
#Cursos a los cuales se inscribieron los estudiantes
Students_Enrolled = {"John":"Python", "Sam":"Java", "Nick":["Python","JavaScript"]}
print(Students_Enrolled) #Imprime el diccionario
#______________________________________________________________________________________________________________________________________________________

#MANIPULACIÓN:
#Las claves o Keys son las unicas que pueden identificar los valores en un diccionario
#   Accediendo a los elementos de un diccionario
#   Actualizando un diccionario
#   Eliminando elementos de un diccionario

#ACCEDIENDO A ELEMENTOS:
#Las claves pueden usarse dentro de corchetes [] o con el metodo get()
#Si usamos [] se genera error en caso de que no se encuentre una clave en el diccionario
#Si usamos get() devuelve None si la clave no se encuentra

#Ejemplo:
example = {1:"John", 2:"Nick"}
print(example[1]) #Devuelve e imprime "John"
print(example.get(2)) #Devuelve e imprime "Nick"

#ACTUALIZANDO UN DICCIONARIO:
#Los diccionarios son mutables, eso quiere decir que podemos manipular los valores
#Podemos actualizar el valor o añadir una nueva clave/valor a la colección

#Ejemplo:
example = {1:"John", 2:"Nick"}
example[1] = "Den" #Cambia a John por Den
example[3] = "Sim" #Añade a Sim al diccionario
print(example) #Imprime: {1:"Den", 2:"Nick", 3:"Sim"}

#ELIMINANDO ELEMENTOS:
#Usamos del para eliminar un elemento en particular o todo el diccionario si lo desea

#Ejemplo:
example = {1:"John", 2:"Nick"}
del example[1] #Borramos 1:"John del diccionario"
print(example) #Imprime {2:"Nick"}
#______________________________________________________________________________________________________________________________________________________

#FUNCIONES DEL DICCIONARIO:
#Algunas funciones de Python para manipular el diccionario son...
#   .keys(): Devuelve la lista de claves del diccionario
#   .values(): Devuelve la lista de valores del diccionario
#   .clear(): Elimina todos los elementos de un diccionario, es decir, lo convierte en un diccionario vacio
#   .get(key): Devueleve el valor de la clave especificada. Si la clave no existe devuelve None
#   .items(): Devuelve una lista de pares clave-valor de diccionarios en forma de tupla
#   .update(dic): Agrega los pares clave-valor especificados del diccionario(items) al diccionario

#Ejemplo:
Emp_Data = {101:"Bravo", 102:"Asten", 103:"Kerry"} #Creamos un diccionario lleno
print(Emp_Data.keys()) #Imprime: dict_keys([101, 102, 103])
print(Emp_Data.values()) #IMprime: dict_values(['Bravo', 'Asten', 'Kerry'])
print(Emp_Data.get(101)) #Imprime: Bravo
print(Emp_Data.get(102)) #Imprime: Asten
print(Emp_Data.items()) #Imprime: dict_items([(101, 'Bravo'), (102, 'Asten'), (103, 'Kerry')])
print(Emp_Data.clear()) #Imprime: None ya que borramos el diccionario

Emp_Data = {101:"Bravo", 102:"Asten", 103:"Kerry"}
Emp_Data.update({104:"Curan", 105:"Elly"}) #agrega 104:"Curan", 105:"Elly"
print(Emp_Data) #Imprime el diccionario completo: {101: 'Bravo', 102: 'Asten', 103: 'Kerry', 104: 'Curan', 105: 'Elly'}

#MAS TIPOS DE VALORES:
#Los valores contenidos en el par clave-valor tambien pueden ser del tipo dato lista o tupla

#Ejemplo:
Var_Dict = {"Asia":["India", "UAE", "China"], 101:"Dalmatians"} #La clave Asia contiene multiples valores y vemos tambien que un diccionario puede contener diferente tipos de datos
print(Var_Dict) #Imprime el diccionario: {'Asia': ['India', 'UAE', 'China'], 101: 'Dalmatians'}

#Ejemplo:
#Imagina que tiene 10 valores diferentes almacenados en un entorno de lista
#¿Que pasa pasa si necesitamos agregar o eliminar un valor particular en esta lista?
#   Para esos escenarios usamos: append() o remove()
Var_Dict = {"Asia":["India", "UAE", "China"]} #Diccionario con la clave "Asia" que contiene multiples valores
Var_Dict["Asia"].append("Japan") #Usamos .appened() para agregar el valor "Japan" a la clave "Asia"
print(Var_Dict) #Imprime: {'Asia': ['India', 'UAE', 'China', 'Japan']}
Var_Dict["Asia"].remove("China") #Usamos .remove() para eliminar el valor "China" de la clave "Asia"
print(Var_Dict) #Imprime: {'Asia': ['India', 'UAE', 'Japan']}
#______________________________________________________________________________________________________________________________________________________

#ITERAR SOBRE UN DICCIONARIO:
#Podemos iterar sobre un diccionario con el bucle for. pero hay varias formas de hacerlo teniendo en cuenta clave-valor

#Metodo1: Iterar solo las claves
Emp_Data = {101:"Bravo", 102:"Sten"} #Diccionario
for i in Emp_Data:
    print(i) #Imprime las claves: 101 y 102

#Metodo2: Iterando solo los valores con el metodo .values()
Emp_Data = {101:"Bravo", 102:"Sten"} #Diccionario
for i in Emp_Data. values():
    print(i) #Imprime: Breavo y Sten

#Metodo3: Iterando con claves y valores con el metodo .items()
Emp_Data = {101:"Bravo", 102:"Sten"} #Diccionario
for i in Emp_Data.items():
    print(i) #Imprime: (101, 'Bravo')
             #         (102, 'Sten')