#FUNCIONES EN PYTHON
#   Concepto más fundamental e importante de Python
#   Componentes basicos de un programa


#REUSABILIDAD
#   Reutilizar un codigo en particular en lugar de escribir uno nuevo
#   Promueven la idea de "Write Once, Execute Anytime"

#Ejemplo Sencillo:
Number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
Number_3 = Number_1+number_2
print("Adition is: ", Number_3)
#Mas adelante veremos como reutilizar este codigo usando funciones...
#___________________________________________________________________________________________________________________________________________________________________________________________

#SINTAXIS DE FUNCIÓN
#   A continuación se muestra la estructura (syntax) de una función en Python.
"""def function_name (parameter1, parameter2): Def se usa para definir una función, asignamos nombre a la función similar a una variable. La palabra def, es seguida por el nombre de las funciones en paréntesis ().
    //block of code                            Los parentesis los usamos para asignar los parametros, es decir, el medio por el cual pasamos valores a una función y finalizamos con (:).
    return statements"""

#LLAMANDO UNA FUNCIÓN
#   Una función es un bloque de codigo que ejecuta una tarea, pero no lo hara a menos que el bloque de codigo la llame.
#   Para llamaruna función escribimos el nombre de la función con los parámetros adecuados.
#Acontinuación, se muestra la sintaxis para llamar una función...
""" function_name()
    #OR
    function_name(parameter1,paremeter2) """
#__________________________________________________________________________________________________________________________________________________________________________________________

#DEFINIEDO UNA FUNCIÓN
#   Vamos a crear una función que diga "HEllo!"
def Say_Hello(): #Definimos y creamos la función Say_Hello():
    print("Hello") #Print "Hello" es el bloque de codigo para la función.
Say_Hello() #Imprime "Hello" cada vez que se llame la función.

#TIEMPOS PARA PARAMETROS
#   Crea una función que diga "Hola" con el nombre del usuario.
def Say_Hello(name): #Necesitamos pasar un valor, que es name, que contendra el valor pasado. 
    print("Hello", name) #Usamos este parametro en el cuerpo de la función para personalizar la salida.
Say_Hello("John") #LLamamos la función que esta vez espera espera un valor, por lo tanto debemos pasar el nombre del usuario cuando se llame la función
#No cumplir con esto puede resultar en error ...

#AÑADIR
#   Crea una función simple que sume dos números
def add_Numbers(num1, num2): #Definimos y creamos la función add_Numbers.
    num3=num1+num2 #Operamos dentro del bloque de la función.
    return num3 #Retorna el num3.
print(add_Numbers(5,6)) #Imprimimos y llamamos la función que operara num1 y num2 que agregemos.
#_________________________________________________________________________________________________________________________________________________________________________________________

#ARGUMENTOS Y PARAMETROS
#   ARGUMENTO: Valor enviado a la función
#   PARAMETRO: Variable listada en el parentesis de la función
def add_number(a,b): #a y b son los parametros
    return a+b
add_number(2,3) #2 y 3 son los argumentos

#Ejemplo:
def Say_Hello(name):
    print("Hello", name)
Say_Hello("Santiago")
#   Estos valores pueden venir del usuario o de algunos calculos de procesamiento.

#ARGUMENTOS PREDETERMINADOS
# Podemos proporcionar un valor predeterminado asignado (=)
def Say_Hello(name="User"):
    print("Hello", name)
Say_Hello()
#Así, si no se pasa un argumento, considerará el valor predeterminado del argumento. Si se pasa el argumento, entonces se considera valor pasado
#De esta manera no arroja Error al no tener argumentos nuevos

#Ejemplo:
#   Una aplicación de pasarela de pago, debe mostrar si la transacción fue aceptada o rechazada.
#   El requisito es mantener predeterminado como "Rejected"(Rechazada) para que cualquier problema menor pueda ser resaltado
def Payment_Status(status="Rejected"):
    print("Payment_Status: ", status)
Payment_Status()
#_____________________________________________________________________________________________________________________________________________________________________________________________

#LAMBDA EN PYTHON
#   lambda
#   Son un atajo para escribir la funciones
#   No tienen nombre por ello se les dicef funciones anonimas
#   Estan restringidas solo a una expresion
#   Puede tomar cualquier numero de argumentos pero solo contienen una unica expresión. Una expresión es un fragmento de codigo que puede o no devolver un 
#   lambda no usa return
""" lambda arguments : expression """ #Estructura de lambda
#Ejemplo:
#   Definamos una función que sume dos números utilizando la palabra clave def
def Add_Numbers(num1, num2):
    return num1 + num2
#AHORA CON lambda
lambda num1, num2: num1 + num2 #Quitamos def y agregamos lambda, retiramos parentesis y no usamos return

#LLAMAR A LA FUNCIÓN LAMBDA
#   Al no tener nombre asignamos una variable a lambda para llamarla
add_number = lambda num1, num2: num1 + num2 #Asignamos una varible que es add_number a lambda. Asignamos parametros : Asignamos argumentos
print(add_number(5,6)) #Imprimimos y llamamos la función que operara num1 y num2 que agregemos