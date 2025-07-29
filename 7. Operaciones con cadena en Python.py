#OPERACIONES CON CADENAS EN PYTHON
#________________________________________________________________________________

#Usando la comma (,) para separar cadenas
username = input("Please, enter your name: ")
print("Helllo", username, "welcome to the Python course")

#Usando str.format()
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Hello, {}. You are {} years old.".format(name, age))

#Marcar Placeholders o Marcadores de posición Indices con nombre {nombre} , Indices númerados {0}, o vacios{}
stringOne = ("My name is {fname}, I am {age} years old".format(fname="John", age=36)) #Usando indices con nombre
stringTwo = ("My name is {0}, I am {1} years old".format("John", 36)) #Usando indices numerados
stringThree = ("My name is {}, I am {} years old".format("John", 36)) #Usando indices vacios

#¿Qué son las fStrings?
#Las fStrings son una forma de formatear cadenas en Python que permite incrustar expresiones dentro de cadenas literales utilizando llaves {}.
name = input("Enter your name: ")
print(f"Hello, {name}. Welcome to the Python course!") #Usando fStrings
#Las fStrings son más legibles y eficientes que otros métodos de formateo de cadenas, como el uso de str.format() o el operador %.

#Otro ejempl o de fStrings...
num1 = 5
num2 = 10
print(f"The sum of {num1} and {num2} is {num1 + num2}.") #Usando fStrings
#En este ejemplo, las variables num1 y num2 se incrustan directamente en la cadena utilizando llaves {}.

#CONCEPTO INDICE
#El índice es la posición de un carácter dentro de una cadena. En Python, los índices comienzan en 0.
#Por ejemplo, en la cadena "Python", el índice de 'P' es 0, el índice de 'y' es 1, y así sucesivamente.
#Los índices negativos también son válidos, donde -1 se refiere al último carácter de la cadena, -2 al penúltimo, y así sucesivamente.
#El indice va dentro de los corchetes [] y se coloca después del nombre de la cadena.
appName = "PythonX"
print(appName[0]) #P
print(appName[1]) #y
print(appName[2]) #t
print(appName[3]) #h
print(appName[4]) #o
print(appName[5]) #n
print(appName[6]) #X
#__________________________________________________________________________________________________________________________________________________________________
#CORTE EN PYTHON
#El corte (slicing) en Python permite extraer una subcadena de una cadena original especificando un rango de índices.
#La sintaxis es cadena[inicio:fin], donde 'inicio' es el índice del primer carácter que se desea incluir y 'fin' es el índice del primer carácter que no se desea incluir.

#¿Qué es Slicing?
#El slicing es una técnica en Python que permite extraer una parte de una cadena, lista o tupla utilizando un rango de índices.
# string[start:end:step] donde 'start' es el índice inicial, 'end' es el índice final (no incluido) y 'step' es el paso (opcional).

#Ejemplo de slicing Positivo
appName = "PythonX"
print(appName[:]) #Devuelve toda la cadena
print(appName[::]) #Devuelve toda la cadena

#Ejemplo de slicing con un rango
appName = "PythonX"
print(appName[:4]) #Devuelve "Pyth"
print(appName[2:5]) #Devuelve "tho"
print(appName[3:]) #Devuelve "thonX"
print(appName[::2]) #Devuelve "PtoX"

#slicing Negativo
#El slicing negativo permite acceder a los elementos de una cadena desde el final hacia el principio.
#Por ejemplo, -1 se refiere al último carácter, -2 al penúltimo, y así sucesivamente.
#La sintaxis es cadena[inicio:fin:paso], donde 'inicio' y 'fin' pueden ser negativos.
#Ejemplo de slicing negativo
appName = "PythonX"
print(appName[-1]) #Devuelve "X"
print(appName[-2]) #Devuelve "n"
print(appName[-3]) #Devuelve "o"
print(appName[-4]) #Devuelve "h"
print(appName[-5]) #Devuelve "t"
print(appName[-6]) #Devuelve "y"
print(appName[-7]) #Devuelve "P"
#___________________________________________________________________________________________________________________________________________________________________
#OPERACIONES SIMPLES
#Las operaciones simples en cadenas incluyen la concatenación, repetición y verificación de pertenencia.
#Concatenación: Unir dos o más cadenas utilizando el operador +.
#Repetición: Repetir una cadena un número específico de veces utilizando el operador *.
#Verificación de pertenencia: Comprobar si una subcadena está presente en una cadena utilizando el operador in. 
#Ejemplo de concatenación
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name #Concatenación de cadenas
print(full_name) #Devuelve "John Doe"

#Usando el metodo join()
first_name = "John"
last_name = "Doe"
print(" ".join([first_name, last_name])) #Devuelve "John Doe"

#Ejemplo de repetición de cadenas
str = "Python"
print(str * 3) #Devuelve "PythonPythonPython"
print(str * 2) #Devuelve "PythonPython"

#__________________________________________________________________________________________________________________________________________________________________
#METODOS INTEGRADOS DE CADENAS
#capitalize() - Convierte el primer caraácter en mayúscula y todos los demás caracteres en minuscula.
#cpunt() - Devuelve el número de veces un valor espeficificado aparece en una cadena.
#find() - Busca en la cadena un valor específico y devuelve la posición donde se encontro. Si no se encuentra, devolverá -1.
#index() - Busca en la cadena un valor especificado y devuelve el índice de la posición donde se encontró. Si no se encuentra, lanzará una Excepción (error).
#insalnum() - Devuelve True si todos los caracteres en la cadena son alfanumericos (Letras y Números).
#isalpha() - Devuelve True si todos los caracteres en la cadena están en el alfabeto.
#islower() - Devuelve True si todos los caracteres en la cadena son minúsculas.
#isupper() - Devuelve True si todos los caracteres en la cadena son mayúsculas.
#join() -Une los elementos de una iterable al final de la cadena.
#lower() - Convierte una cadena en minúsculas.
#replace(a,b) - Devuelve una cadena donde un valor especificado es reemplazado po un valor especificado.
#strip() - Devuelve una versión recortada de la cadfena, es decir, elimina los espacios en blanco de ambos extremos.
#upper() - Convierte una cadena en mayúsculas.

#EJEMPLO
str = "PythonX"
print (str.islower())
print (str.upper())
print (str.lower())
print (str.replace("P", "A"))

#METODO len()
#Acepta una cadena como parametro y devuelve la logitud de la cadena. También cuenta todos los espacios en blanco en la cadena.

str = "Love Python"
print(len(str)) #Devuelve 12