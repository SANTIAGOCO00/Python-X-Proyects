#CONJUNTOS, SET O COLECCIONES
#Los set() o conjuntos se usan para agrupar y almacenar multiples elementos
#   CARACTERISTICAS:
#   Los conjuntos son colecciones desordenadas. Así, no hay un índice adjunto a ningún elemento en un conjunto de Python
#   Los elementos del conjunto son únicos. Esto significa que no se permiten elementos duplicados
#   Un conjunto en sí puede ser modificado, pero los elementos contenidos en el conjunto deben ser de un tipo inmutable

#NOTA: Los sets() al igual que los dicionarios usan () la diferencia es que el diccionario contiene elementos clave-valor

#Ejemplo:
Example = set() #Creamos un conjunto vacio
print(type(Example)) #Imprimimios: class "set" /Ya que con type() averiguamos la clase de example que es set()

#   Los conjuntos no pueden tner listas ni diccionarios en ellos, ya que son inmutables
Example = {1,2,3} #Creamos un diccionario con int
Example1 = {6, 8.9, "James"} #Creamos un diccioanrio con int, float point, str
print(Example) #Imprimimos: {1, 2, 3}
print(Example1) #Imprimimos: {8.9, 'James', 6}
#______________________________________________________________________________________________________________________________________________________

#ACCEDIENDO A ELEMENTOS
#   Los conjuntos no tiene un orden definido, por lo tanto no podemos usar números como indices. 
#   Pero podemos acceder a los elementos uno por uno recorriendolos.

#Ejemplo:
#Conjunto con días de la semana
days ={"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(days) #Imprimimos: {'Monday2', 'Friday', 'Thursday', 'Saturday', 'Wednesday', 'Sunday', 'Tuesday'} al azar ya que no tienen orden
for day  in days: #Asignamos una nueva variable day para days con usando for
    print(day) #Imprimimos day y el orden es al azar
#______________________________________________________________________________________________________________________________________________________

#REALIZANDO OPERACIONES ESPECIFICAS DE LOS CONJUNTOS
#   Unión de Conjuntos
#   Intersección de Conjuntos
#   Diferencia de Conuntos

#UNION DE CONJUNTOS
#   Supongamos que tenemos dos conjuntos, Conjunto A y Conjunto B
#   La union de dos conjuntos A y B es el conjunto de elementos que están en A, en B, o en ambos A y B
#   La union de dos conjuntos produce un nuevo conjunto que contiene todos los elementos de ambos conjuntos
#   Lo realizamos con los operadores .union() o con |

#Ejemplo:
Conjunto_A = {1,2,3,4,5} #Creamos un conjunto
Conjunto_B = {4,5,6,7,8} #Creamos un segundo conjunto
print(Conjunto_A|Conjunto_B) #imprimimos usando el operador | : {1, 2, 3, 4, 5, 6, 7, 8}
print(Conjunto_A.union(Conjunto_B)) #Imprimimos usando el operador .union() : {1, 2, 3, 4, 5, 6, 7, 8}

#INTERSECCIÓN DE CONJUNTOS
#   la intersección de dos conjuntos A y B, se denota A ∩ B.
#   Es el conjunto que contiene todos los elementode A que tambien pertenecen a B
#   La intersección de A y B es un conjunto de elemntos que son comunes a ambos conjuntos
#   Realizamos la intersección con los operadores .intersection() o &

#Ejemplo:
Conjunto_A = {1,2,3,4,5} #Creamos un conjunto
Conjunto_B = {4,5,6,7,8} #Creamos un segundo conjunto
print(Conjunto_A&Conjunto_B) #Imprimimos usando el operador & : {4, 5}
print(Conjunto_A.intersection(Conjunto_B)) #Imprimimos usando el operador .intersection() : {4, 5}

#DIFERENCIA DE CONJUNTOS
#   Diferencia de conjuntos crea un nuevo conjunto que contiene solo los elementos del primer conjunto y ninguno del segundo conjunto
#   La diferencia el conjunto de lementos que esta en un conjunto y no en el otro
#   Realizamos la diferenci con los operadores .difference() o - :

#Ejemplo:
Conjunto_A = {1,2,3,4,5} #Creamos un conjunto
Conjunto_B = {4,5,6,7,8} #Creamos un segundo conjunto
print("Conjunto_A - Conjunto_B: ", Conjunto_A-Conjunto_B) #Imprimimos usando el operador - : {1, 2, 3}
print("Conjunto_B - Conjunto_A: ", Conjunto_B-Conjunto_A) #Imrpimimos usando el operador - : {8, 6, 7}
print("Conjunto_A - Conjunto_B: ", Conjunto_A.difference(Conjunto_B)) #Imprimimos usando el operador .difference() : {1, 2, 3}
print("Conjunto_B - Conjunto_A: ", Conjunto_B.difference(Conjunto_A)) #Imrpimimos usando el operador .difference() : {8, 6, 7}
#______________________________________________________________________________________________________________________________________________________

#FUNCIONES INTEGRADAS
#   len() Devuelve la longitud (número de elementos del conjunto)
#   max() Devuelve el elemento más grande del conjunto
#   min() Devuelve el elemento más pequeño del conjunto
#   sorted() Devuelve una nueva lista ordenada de los elementos en el conjuto. No ordena el conjunto en sí mismo
#   sum() Devuelve la suma de todos los elementos del conjunto

#Ejemlplo:
example = {23,22,34,36,24,41}
print(len(example)) #Imprime: 6
print(max(example)) #Imprime: 41
print(min(example)) #Imprime: 22
print(sorted(example)) #Imprime: [22, 23, 24, 34, 36, 41]
print(sum(example)) #Imprime: 180
#______________________________________________________________________________________________________________________________________________________

#METODOS EN CONJUNTOS
#Algunos metodos importantes de set()
#   .add() Añade un elemento al conjunto
#   .intersection() Devuelve la intersección de dos conjuntos como un nuevo conjunto
#   .clear() Elimina todos los elementos del conjunto
#   .copy()  Devuelve una copia del conjunto
#   .difference() Devuelve la diferencia de dos o más conjuntos como un nuevo conjunto
#   .discart() Elimina un elemento del conjunto si es un miembro
#   .isdisjoint() Devuelve True si dos conjuntos tienen una intersección nula
#   .issubset() Devuelve True si otro conjunto contiene este conjunto
#   .issuperset() Devuelve True si este conjunto contiene otro conjunto
#   .pop() Elimina y devuelve un elemento arbitrario del conjunto
#   .remove() Elimina un elemento del conjunto
#   .union() Devuelve la union de conjuntos en un nuevo conjunto
#   .update() Actualiza el conjunto con la unión de sí mismo y otros

#Ejemplo:
#Creamos un conjunto con las edades de los emepleados
age = {23,22,34,36,24,41}
print(age.add(56)) #Añade 56 al conjunto e imprime None ya que esta Agregado: None
print(age.remove(22)) #Elimina 22 del conjunto e imprime None ya que esta eliminado: None
print(age.pop()) #Elimina y devuelve un elemento arbitrario del conjunto: 34
print(age) #Imprimir el conjunto: {36, 23, 24, 41, 56}

#Ejemplo:
A = {1,2,3}
B = {1,2,3,4,5}
C = {100,101,102}
print(A.issubset(B)) #Imprime: True, ya que otro conjunto contiene este conjunto
print(B.issuperset(A)) #Imprime: True, ya que este conjunto contiene otro conjunto
print(A.isdisjoint(B)) #Imprime: False, ya que ambos conjuntos cuentan con intersección
print(A.isdisjoint(C)) #Imprime: True, ya que ambos conjuntos tienen una intersección nula

#Ejemplo:
Brics_Nations = {"B", "R", "I", "C", "S"}
Brics_Nations.discard("Z") #Elimina el elemento "Z" pero no afecta ya que "Z" no es parte del conjuto
print(Brics_Nations) #Imprime el conjunto: {'B', 'R', 'C', 'I', 'S'} en desorden ya que los conjuntos tienen orden

#Ejemplo:
""" Brics_Nations = {"B", "R", "I", "C", "S"}
    Brics_Nations.remove("Z") #Elimina el elemento "Z" pero nos arrojara un error ya que "Z" no es parte del conjuto
    print(Brics_Nations)  #Syntax Error """