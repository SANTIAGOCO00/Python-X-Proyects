#Listas en Phyton
#Las listas son untipo de variable que nos permite almacenar multiples valores de varios tipos de datos en una sola variable.
#Una lista en Python puede ser creada solocando la secuencia dentro de los corchetes []. Los elementos dentro de la secuencia deben estar separados por comas

#Ejemplo:
#Below is an example of creating an empty list
list1 = [] #List1 es núestra variable
#list with values of same data type
list2 = [1,4,6,3,9] #List2 es la variable en este ejemplo de lista con el mismo tipo de elementos
#List with values of different data types
list3 = ["John",23,56.0,True] #List3 es la variable en este ejemplo de lista con diferentes tipos de elementos

#Ejemplo2:
#Queremos hacer seguimineto a de los cursos en los que esta inscrito un estudiante. Aqui podemos usar el concepto de lista.
coursesEnrolled = ["Python","Java","React"]
print(coursesEnrolled)
#______________________________________________________________________________________________________________________________________________________

#MANIPULACIÓN DE LISTAS
#Manipularemos la lista usando lo siguiente:
#   Accediendo a los elementos de una lista.
#   Actualizando una lista.
#   Eliminando elementos de una lista.

#ACCEDIENDO A ELEMENTOS DE UNA LISTA:
#Dado que la lista es un tipo de dato secuencial, podemos acceder a los elementos de una lista usando indices. Los indices inicias desde 0

#Ejemplo:
names = ["john","Sam","Barry","Lin"] #EL número 0 del indice sera "John" y sucesivamente...
print(names) #Imprime la lista completa
print(names[0]) #Imprime "john"
print(names[3]) #Imprime "Lin"

#SEGMENTACIÓN DE LISTAS:
#Ejemplo:
names = ["John","Sam","Barry","Lin"]
print(names) #Imprime la lista completa
print(names[0:3]) #Imprime "John", "Sam" y "Barry"
print(names[2:]) #Imprime "Barry" y "Lin"

#ACTUALIZANDO LISTAS:
#Las listas son mutables, podemos actualizar el valor con el tiempo usando el operador =

#Ejemplo:
marks = [56,76,69,71,39] #marks es la variable que contiene las notas
print(marks) #imprime la lista completa
marks[4] = 43 #Actualizamos la nota 39 por 43
print(marks) #imprime la lista completa

#ELIMINANDO ELEMENTOS DE UNA LISTA:
#Si conocemos el número de indice del elemento que deseamos eliminar de la lista, podemos hacerlo con la declaración del.

#Ejemplo:
names = ["John","Sam","Barry","Lin"] 
print(names) #Imprime la lista completa
del names[1] #Eliminamos el elemento en el indice 1 que es "Sam"
print(names) #Imprime la lista sin "Sam"

#Tambien podemos eliminar la lista completa usando la declaración del.
#Ejemplo:
names = ["John","Sam","Barry","Lin"] 
del names #Eliminamos la lsita completa

#Ejemplo:
#Stan estaba creando una lista de paises Europeos y accidentalmente agregó a Peru a esta lista. ¿Puedes eliminarlo?
Europe_Countries = ["France","Peru","Spain","Germany"]
print(Europe_Countries) #Imprime la lista completa con un error "Peru"
del Europe_Countries[1] #Eliminamos el elemento "Peru" de la lista
print(Europe_Countries) #Imprime la lista sin "Peru"
#______________________________________________________________________________________________________________________________________________________

#OPERACIONES BASICAS EN LISTAS:
#Algunas de las operaciones que podemos relizar son:
#   Concatenación
#   Repetición
#   Membresía

#CONCATENACIÓN y REPETICIÓN DE LISTAS
#Agregar dos listas es concatenación de listas y multiplicaruna lista es reetición de listas. Podemos usar + y * respectivamente.

#Ejemplo:
list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2) #Concatenamos las listas, aparece la lista 1 y luego la lista 2
print(list1 * 3) #Multiplicamos la lista por 3, aparece 3 veces la lista

#Ejemplo:
print(["PythonX"*2]) #Imprime [PythonXPythonX]

#MEMBRESÍA:
#El operador de pertenencia in() se usa para probar la pertenencia de un elemento en una lista.

#Ejemplo:
Enrolled_List = ["John","Sam","Barry","Lin"]
print("John" in Enrolled_List) #Imprime True porque "John" es parte de la lista
print("Axel" in Enrolled_List) #Imprime False porque "Axel" no es parte de la lista
print("Sam"not in Enrolled_List) #Imprime False porque "Sam" es parte de la lista
print("Axel"not in Enrolled_List) #Imprime True porque "Axel" no es parte de la lista

#Ejemplo:
#Stan estaba creando una lista de paises y elimino algunos paises que fueron agregados por error. Escribe un codigo que verifique si el pais eliminado sigue siendo parte de la lista o no

#Lista original de paises
Countries = ["France","Peru","Spain","Germany"]
del(Countries[1]) #Eliminamos el elemento "Peru" de la lista
if("Peru" in Countries): #verificamos si "Peru" es parte de la lista
    print("Peru sigue siendo parte de la lista") 
else:
    print("Peru no es parte de la lista")
#______________________________________________________________________________________________________________________________________________________

#ITERANDO SOBRE UNA LISTA:
#Podemos usar for para iterar sobre una lista.

#Ejemplo:
fruits = ["Apple","Mango","Cherry","Banana"]
for i in fruits: #Iteramos sobre la lista de frutas
    print(i) #Imprimimos cada elemento de la lista

#Ejemplo:
#Ahora digamos que queremos verificar si un elemento en particular esta en la lista o no. Queremos buscar "Mango"
fruits = ["Apple","Mango","Cherry","Banana"]
for i in fruits: #Iteramos sobre la lista de frutas
    if i == "Mango": #Si el elemnto es igual a "Mango"
        print("Mango esta en la lista")
        break #Salimos del bucle
else:
    print("Mango no esta en la lista")

#Ejemplo:
#Escribe un codigo que imprima todos los países de la lista a continuación que no tengan la subcadena "Land" en su nombre.
Countries = ["Ireland","Finland","France","Iceland","Poland","Spain"]
for country in Countries: #Iteramos sobre la lista de países
    if "land" not in country: #Si "land" no esta en el nombre del país
        print("Los paises que no cuentan con land son:",country) #Imprimme paises que no tengan "land"
#______________________________________________________________________________________________________________________________________________________

#ALGUNAS FUNCIONES INTEGRADAS:
#   len(list) - Devuelve la longitud de la lista
#   min(list) - Devuelve los elementos de la lista con el valor mínimo
#   max(list) - Devuelve los elementos de la lista con el valor maximo

#Ejemplo:
numbers = [23,56,78,13,98,33]
print(len(numbers)) #Imprime 6, que es la logitud de la lista
print(min(numbers)) #Imprime 13, que es el valor minimo de la lista
print(max(numbers)) #Imprime 98, Que es el valor maximo de la lista

#METODOS DE LISTA:
#Se puede acceder a algunos metodos incorporados para trabajar con listas utilizando list.method()
#   .append(element): - Añade el elemento especificado a la lista
#   .inser(Indice, Elemento): - Inserta un elemento en el indice especificado
#   .pop(): - Elimina y devuelve el ultimo elemento de la lista
#   .remove(Element): - Elimina el elemento especificado de la lista
#   .reverse(): - Invierte el orden de los elementos en la lista
#   .index(Element): Devuelve el índice del rpimer elemento coincidiente
#   .count(Element): Devuelve el conteo de cuántas veces un elemnto aparece en la lista

#Ejemplo:
names = ["John","Sam","Barry","Lin"]
print(names)
names.append("Axel") #Añade el elemento especificado a la lista
print(names)

#Ejemplo:
names = ["John","Sam","Barry","Lin"]
names.insert(1,"Ron") #Inserta el elemento en el indice especificado
print(names)

#Ejemplo:
names = ["John","Sam","Barry","Lin"]
names.remove("Barry") #Elimina el elemento especificado de la lista
print(names)

#Ejemplo:
age =[18,67,35,23,18,22]
print(age.count(18)) #Devuelve el conteo de cuántas veces un elemento aparece en la lista
#______________________________________________________________________________________________________________________________________________________

#LISTAS INTELIGENTES:
#Ejemplo: Ejecutar bucle en unrango dado, si el número es par, luego lo agregamos a la lista que hemos creado con el nombre even.
even = []
for x in range(1,11):
    if x % 2 == 0:
        even.append(x)
print(even)

