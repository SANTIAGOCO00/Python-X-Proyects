#MANEJO DE EXCEPCIONES
#   El proceso para manejar los errores se llama depuración

#TIPOS DE ERRORES
#    ERRORES DE SINTAXIS
#       Es un error en el codigo fuente del programa. ERRORES DE COMPILACIÓN (Ej: sangria, parentesis, comas etc...)
#    ERRORES LÓGICOS
#       Errores en la lógica de programazión. Puede dar lugar a operaciones indeseadas que no queremos que ocurran. NO LOS DETECTA EL DEPURADOR (Ej: Confundir simbolos, +,/,- etc...)
#    ERRORES DE EJECUCIÓN
#       Estos errores se detectan en TIEMPO DE EJECUCIÓN, cuando intentamos realizar una operación imposible de llevar a cabo (Ej: Dividir cualquier número por cero)
#___________________________________________________________________________________________________________________________________________________________________________________________

#EXCEPTIONS
#   Los errores de ejecución suceden cuando se detecta un comportamiento anormal, estos errores se les llama EXCEPTIONS
#   Para evitar manejar y evitar el cierre del programa, usaremos el concepto conocido como Exeption Handling
#       EJEMPLOS COMUNES DE EXCEPCIONES
#           Division por cero
#           Accediendo a un archivo que no existe
#           Adición de dos tipos incompatibles
#           Intentando acceder a un índice inexistente
#           Eliminando la tabla del servidor de base de datos desconectado
#   UNA EXCEPCIÓN ES UN METODO CONVENIENTE PARA MANEJAR MENSAJES DE ERROR
#___________________________________________________________________________________________________________________________________________________________________________________________

#EXCPCIONES EN PYTHON
#   Clase Exception: Es la clase base de la cual heredan las excepxiones. Esto significa, que todas las excepciones comunes heredan de esta clase
#   EXEPCIONES COMUNES
#           StandardError - Es la clase base para todas las excepciones incorporadas
#           ArithmeticError - Es la clase base para todos los errores que ocurren durante los calculos numericos
#           FloatingPointError - Se produce cuando un calculo de punto flotante falla
#           ZeroDivisión -Se produce cuando se realiza una división o modulo por cero para todos los tipos númericos
#           EOFError - Se produce cuando no hay entrada desde la función input() y se llega al final del archivo
#           ImportError - Se produce produce cuando una declaración de importación falla
#           KeyboardInterrupt - Cuando el usuario interrumpe la ejecución del programa, generalmente presionando Ctrl+c
#           IndexError - Se produce cuando no se encuentra un indice en una secuancia
#           NameError - Se genera cuandoo un identificador no se encuentra en el espacio de nombre locales o global
#           IOError - Se produce cuando una operación de entrada/salida falla, como print() o open() al abrir un archivo que no existe
#           SyntaxError - Se genera cuando hay un error en la sintaxis de Python
#           IndentationError - Se produce cuando la identación no se especificaa correctamente
#           TypeError - Se genera cuando la función incorporada para un tipo de datos tiene válido de argumentos, pero los argumrntos tienen valoes no validos no especificados
#___________________________________________________________________________________________________________________________________________________________________________________________

#MANEJO DE EXCEPCIONES
#   Para manejar de forma elegante las excepciones Python nos vrinda las siguientes declaraciones
#       Try
#           La operación con error que genere una exepción se coloca dentro de la clausula try. Intentara ejecutar ese feagmento de codigo en particular
#           si se produce excepción, se pasara a la declaración except
#       Except
#           Maneja la excepción, si no se alcanzan las excepciones, las sentencias dentro del bloque try y el control pasa a las siguientes sentencias
""""    SINTAXIS BLOQUE TRY-EXCEPT
                    try:               #Declaraciones que pueden generar el error
                    except Exception1: #Si hay una Excepción1, entonces este bloque se ejecutará.
                    except Exception2: #Si hay una Excepción2, entonces este bloque se ejecutará. """
#__________________________________________________________________________________________________________________________________________________________________________________________

#EJEMPLO1
"""print(name) #Cuando intentamos ejecutarlo arroja el siguiente error: NameError: name 'name' is not defined (Si esto no se maneja detendria el flujo de la aplicación)"""

#Nuevamenete ahora manejando la situación...
try:
    print(name)
except NameError:
    print("Ocurrió algún error, por favor contacte al desarrollador") #Imprime: Ocurrió algún error, por favor contacte al desarrollador (El programa no se detiene)

#Tambien podemos mostrar el error al final del mensaje, añadiendo: as e...
try:
    print(name)
except NameError as e:
    print("Ocurrió algún error, por favor contacte al desarrollador", e) #Imprime: Ocurrió algún error, por favor contacte al desarrollador (El programa no se detiene)

#Intentemos nuevamente ahora definiendo la variable name
name = "PythonX"
try:
    print(name)
except NameError as e:
    print("Some error occured. Please cpntact the developer: ", e) #No se genero ninnguna excepción por lo tando se ejcuto el bloque try y se ignoro el except

#EJEMPLO2:
#   Escribamos un programa para dividir dos números 
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print("La división es: ", num1/num2) #El rpograma funciona bien, pero y si alguien quiere dividir un número por cero sin que se cierre el programa

#Manejemos es posible situación...
try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("La división es: ", num1/num2)
except ZeroDivisionError as e:
    print("Oops, no puedes dividir un número por cero") #l rpogrEama funciona bien, aunque intenten dividir por cero
#_____________________________________________________________________________________________________________________________________________________________________________________________

#ESCENARIO
#   Consideremos el ejemplo anterior
try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("La división es: ", num1/num2)
    print("Gracias por usar la calculadora") #Añadimos esta nueva linea, para cuando termine el codigo sin except
except ZeroDivisionError as e:
    print("Oops, no puedes dividir un número por cero") #El rpogrEama funciona bien, aunque intenten dividir por cero

#   Mejoremos el codigo anterior usando finally(se ejecuta sin importar si el bloque try arroja excepción)

try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("La división es: ", num1/num2)
    print("Gracias por usar la calculadora")
except ZeroDivisionError as e:
    print("Oops, no puedes dividir un número por cero")
finally:
    print("Gracias por usar la calculadora") #El mismo mensaje del bloque try, pero ejecuntandolo aun cuando el codigo tiene excepción
#_____________________________________________________________________________________________________________________________________________________________________________________________

#RAISE
#   Podemos generar excepciones en una instancia dada de manera manual
#   sintaxis: raise Exception("Message") 
#       la excepción es el tipo de excepción Ej: NameError
#       El argumento ("Message") es opcional para un mensaje de salida

#Ejemplo
    try:
        a = int(input("Introduzca un numero positivo: "))
        if a <= 0: #Si el número es menor o igual a cero...
            raise ValueError (str(a),"No es un número positivo") #Mensaje de salida al usuario
    except ValueError as e:
        print(e)