#8.TODO SOBRE BUCLES
#________________________________________________________________________________________________________________________________________

#Una declaración Loop nos permite ejecutar una declaración o un grupo de declaraciones múltipples veces.
#ITERACIÓN DEFINIDA: En la que el número de repeticiones se espeficica explícitamente de antemano.
#ITERACIÓN INDEFINIDA: En la que el bloque de código se ejecuta hasta que se cumple alguna condición.

#for loop: Generalmente se utilza para iteraciones definidas, es decir, cuando se conoce el número de iteraciones.
#while loop: Generalmente se utiliza para iteración indefinida, es decir, cuando el número de iteraciones es desconocido.
#________________________________________________________________________________________________________________________________________

#LA FUNCIÓN RANGE
#list(range()) es una función incorporada enPython. Se utiliza cuando un usuario necesita realizar una acción un número especifico de veces. Se usa comnmente en el bucle for.
#La función range () toma principalmente tres argumentos...
#start: Es un número entero a partir del cual se debe devolver la secuencia de enteros. El valor predeterminado es 0.
#stop: Es un número entero antes del cual se devuelve  la sencuencia de enteros. El rango de enteros termina en stop -1.
#step (opcional): Es un valor entero que determina el incremento entre cada entero en la secuencia. El valor predeterminado es 1.

#Ejemplo 1:
print(list(range(5))) #Single Argument signifies the end of the range (excluded) [0, 1, 2, 3, 4]
print(list(range(1,5))) #Two arguments signifies start and the end of the range [1, 2, 3, 4]
print(list(range(1,19,2))) #Three argument, if mentioned, signifies the step size [1, 3, 5, 7, 9, 11, 13, 15, 17]

#Ejemplo 2:
#Imprimir todos los números entre 70 y 100 con un tamaño de paso de 5
print(list(range(70,101,5))) # [70, 75, 80, 85, 90, 95, 100]
#_________________________________________________________________________________________________________________________________________

#Bucle for:
#El bucle for se utiliza para iterar sobre una secuencia (que puede ser una lista, un diccionario, una tupla, un conjunto o una cadena).

#Ejemplo 1:
for i in range (5) :
    print(i) #0 1 2 3 4

#Ejemplo 2:
for i in range(5):
    print("PythonX") #PythonX PythonX PythonX PythonX PythonX

#Iterar sobre String:
for i in "PythonX":
    print(i) #P y t h o n X
#_________________________________________________________________________________________________________________________________________

#Bucle While:
#While se utiliza para ejecutar un bloque de intrucciones repetidamente hasta que se cumpla una condición dada.
#Sintaxis: while boolean_expression:
#             statement(s)

#Ejemplo 1:
i = 0
while i < 3:
    print("I love Python")
    i = i + 1 #Incremento de 1
#_________________________________________________________________________________________________________________________________________

# La declaración Break:
#La instrucción break seusa para terminar el bucle o la declaración en la que está presente.

#Ejemplo 1:
str = "GoodMorning"
for i in str: #Iterar sobre la cadena
    if i == "M": 
        break #Cuando se encuentra la letra M, el bucle se detiene.
    print(i) #Good

#Ejemplo 2:
#Imagina un barco transportando pasajeros entre dos puertos. Debido a las restricciones por covid, deben dejar de embarcar pasajeros tan pronto como el 50% de la capacidad del barco este ocupado.

num = input("enter passengers number: ")
Capacidad_del_barco = num * (50.0/100.0) #50% de la capacidad del barco
for i in range (0, n, 10): #Iterando de 10 en 10
    if i > Capacidad_del_barco: #Si el número de pasajeros es mayor a la capacidad del barco el bucle se detiene
        print("capacidad del barco alcanzada") #Imprimiendo la capacidad del barco alcanzada
        break #Deteniendo el bucle
    else: #Si no se ha alcanzado la capacidad del barco, se imprime el numero de pasajeros abordo
        print("pasajeros abordo:" , i) #Imprimiendo el número de pasajeros abordo
#_________________________________________________________________________________________________________________________________________

#Algunos Ejemplos:

#Tabla de multiplicar:
num = int(input("Enter the number for which you wish to generate the multiplication table: "))
for i in range(1,11): #Iterando de 1 a 10
    print(num, "x", i, "=", num*i) #imprimiendo la latbla de multiplicar

#Numeros Pares:
#Un programa que imprima números pares en el rango especificado. Usando el bucle Whle.
num = int(input("Enter the number till where you want to generate even numbers: ")) #Pidiendo al usuario hastq que numero quiere generar los números pares
i = 0 #Inicializando i en 0
while i <= num: #Mientras i sea menor o igual al número escrito por el usuario
    if i % 2 == 0 : #Si i es par
        print(i) #imprimiendo i
    i = i + 1 #incrementando i en 1.