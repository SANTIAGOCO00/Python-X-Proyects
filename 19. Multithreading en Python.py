#MULTITHREADING / MULTITAREA
#   En terminos de programación se le conoce como: Subprocesos múltiples

#   PROCESOS E HILOS
#       PROCESOS
#           Es el programa en ejecución. Cuando se inicia una aplicación, el sitema operativo crea un proceso
#           En pocas palabras, es una instancia de un programa que se esta ejecutando
#       HILOS / THREAD
#           Es una entidad dentro de un proceso que puede ser programado para ejecutarse
#           Es la unidad de procesamiento más pequeña que puede realizar un sistema operativo
#           En pocas palabras, un hilo es una secuancia de intrucciones dentro de un programa que puede ejecutarse de manera independiante de otro código

#               Cada proceso en la computadora es manejada por un proceso
#               Y a su vez cada proceso es manejado por algo llamado Hilo
#               Un hilo ejecuta diversas tareas dentro de la computadora, de la siguiente manera...
#                   TAREA >>> PROCESO >>> HILO (Así es es como se vería el desglose)

#Ejemplo:
""" Este código define dos clases (Example y ExampleTwo),
    cada una con un método run() que imprime un mensaje cinco veces en la consola. 
    Luego, se crean instancias de ambas clases y se llama a sus métodos run(), ejecutando así las iteraciones y las impresiones correspondientes.
"""
# Definimos una clase llamada Example
class Example:  
    def run(self):  # Método de la clase que se ejecutará cuando se llame a 'run'
        for i in range(5):  # Iteramos 5 veces (valores de i: 0, 1, 2, 3, 4)
            print("Hola por Example")  # Mostramos un mensaje en la consola

# Definimos otra clase llamada ExampleTwo
class ExampleTwo:  
    def run(self):  # Método de la clase que se ejecutará cuando se llame a 'run'
        for i in range(5):  # Iteramos 5 veces
            print("Hola por ExampleTwo")  # Mostramos un mensaje en la consola

# Creamos una instancia de la clase Example
example = Example()  

# Creamos una instancia de la clase ExampleTwo
exampleTwo = ExampleTwo()  

# Llamamos al método 'run' de la instancia 'example'
example.run()  # Esto imprimirá "Hola por Example" cinco veces

# Llamamos al método 'run' de la instancia 'exampleTwo'
exampleTwo.run()  # Esto imprimirá "Hola por ExampleTwo" cinco veces
""" Como vimos, Python ejecuta de manera secuencial por lo tanto imprime exampleTwo una vez finalizado de imprimir example,
    Esto no es lo ideal. Para ello debemos usar Multithreading"""
#___________________________________________________________________________________________________________________________________________________________________________________________

#MULTITHREADING EN PYTHON
#   Python proporciona los siguientes módulos para implementar hilos es Python.
#       MODULO thread (Obsoleto desde Python3)

#       MODULO threading
#           Proporciona una amplia gama de funciones, para gestionar aplicaciones multihilo / multithreading
#           FUNCIONES
#               activeCount()   Devuelve el conteo de objetos Thread que aún estan vivos
#               currentThread() Devuelve el objeto actual de la clase Thread
#               enumerate()     Devuelve la lista de todos los objetos Thread activos
#               isDaemon()      Devuelve True si el hilo es un demoino
#               isAlive()       Devuelve True si el hilo sigue activo

#           CLASE Thread
#               Es la clave principal, define la plantilla y operaciones de un hilo en Python
#               Para una aplicación con multiples hilos, es declarar una clase que herede de la clase Thread y sobreescriba su metodo run()
#               Normalmente , todo el programa es ejecutado por un hilo principal

#               METODOS DE LA CLASE Thread
#               run()   Denota actividad de un hilo y puede ser sobrescrito por una clase que extiende la clase Thread
#               start() Inicia la actividad de un hilo. Debe ser llamado solo una vez para cada hilo, de lo contrario lanzará un error en tiempo de ejecución
#               join()  Bloquea la ejecución de otro código hasta que el hilo en el que se llamó al método join() se 
#____________________________________________________________________________________________________________________________________________________________________________________________

#IMPLEMENTANDO MULTITHREADING EN PYTHON
##Ejemplo:
""" Como vimos en el codigo anterior, Python ejecuta de manera secuencial por lo tanto imprime exampleTwo una vez finalizado de imprimir example,
    Esto no es lo ideal. Para ello debemos usar Multithreading"""

#Ahora agamoslo mejor: Para implementar threading, necesitamos las siguientes 3 cosas;
#       Importar módulo threading
#       Heredar de la clase thread y sobreescribir el método run()
#       Inicie la ejecución de los hilos utilizando el metodo start()

from threading import *  # Importamos el módulo threading para manejar hilos

# Definimos una clase llamada Example que hereda de Thread para poder ejecutarse en un hilo
class Example(Thread):  
    def run(self):  # Este método se ejecutará al iniciar el hilo
        for i in range(400):  # Iteramos 400(Aumentar bucle para ver la diferencia con el codigo anterior) veces (valores de i: 0, 1, 2, 3, 4, etc..)
            print("Hola por Example")  # Mostramos un mensaje en la consola

# Definimos otra clase llamada ExampleTwo que también hereda de Thread
class ExampleTwo(Thread):  
    def run(self):  # Este método se ejecutará al iniciar el hilo
        for i in range(400):  # Iteramos 400(Aumentar bucle para ver la diferencia con el codigo anterior) veces (valores de i: 0, 1, 2, 3, 4, etc..)
            print("Hola por ExampleTwo")  # Mostramos un mensaje en la consola

# Creamos instancias de las clases Example y ExampleTwo
example = Example()  
exampleTwo = ExampleTwo()  

# Iniciamos los hilos llamando al método start()
example.start()  # Esto ejecutará el método run() en un hilo separado
exampleTwo.start()  # Esto ejecutará el método run() en un hilo separado
"AHORA PARECEN ESTAR TRABAJANDO DE MANERA SIMULTANEA, PERO EN REALIDAD ESTAN TRABAJANDO CONCURRENTEMENTE: NO ES LO IDEAL..."
#____________________________________________________________________________________________________________________________________________________________________________________________


#Para lograrlo de manera correcta debemos: EJECUTAR >>> ESPERAR >>> EJECUTAR
#   Esto podemos lograrlo usando el módulo Time en Python
#   Podemos usar el método sleep() Que acepta tiempo en segundos como parámetros y hace que el código se duerma(wait) durante ese tiempo

"""AHORA NUEVAMENTE..."""

from threading import *  # Importamos el módulo threading para manejar hilos
from time import sleep  # Importamos sleep para controlar el flujo de ejecución

# Definimos una clase llamada Example que hereda de Thread
class Example(Thread):  
    def run(self):  # Método que se ejecutará al iniciar el hilo
        for i in range(400):  # Iteramos 400 veces para visualizar la concurrencia
            print("Hola por Example")  # Imprimimos un mensaje en la consola
            sleep(1)  # Pausamos por 1 segundo en cada iteración

# Definimos otra clase llamada ExampleTwo que también hereda de Thread
class ExampleTwo(Thread):  
    def run(self):  # Método que se ejecutará al iniciar el hilo
        for i in range(400):  # Iteramos 400 veces como en la primera clase
            print("Hola por ExampleTwo")  # Imprimimos un mensaje en la consola
            sleep(1)  # Pausamos por 1 segundo en cada iteración

# Creamos instancias de las clases Example y ExampleTwo
example = Example()  
exampleTwo = ExampleTwo()  

# Iniciamos los hilos llamando al método start()
example.start()  # Se inicia el primer hilo
sleep(0.1)  # Pequeña pausa para observar cómo se intercalan los mensajes
exampleTwo.start()  # Se inicia el segundo hilo
""" - Uso de Thread: Permite la ejecución paralela de código.
    - Incorporación de sleep(1) dentro del bucle: Hace que cada hilo espere un segundo entre iteraciones, ayudando a visualizar mejor la ejecución concurrente.
    - Pequeña pausa (sleep(0.1)) entre la inicialización de los hilos: Esto escalona la ejecución y ayuda a ver cómo se intercalan las impresiones.
"""
#____________________________________________________________________________________________________________________________________________________________________________________________

#PROBLEMA CON EL HILO PRINCIPAL
#   En la sección anterior creamos dos hilos que eran responsables de la ejecicón de las dos logicas de ambas clases
#   En el ultimo codigo el hilo principal no tenia nada que hacer . Su trabajo era solo crear dos hilos que manejaron el resto del codigo
#   Necesitamos decirle al hilo principal que espere hasta que los otros dos hilos terminen su parte. Para ello usamos join()

"""AHORA VEAMOS EL SIGUIENTE JEMPLO"""
from threading import *  # Importamos el módulo threading para manejar hilos
from time import sleep  # Importamos sleep para controlar el flujo de ejecución

# Definimos una clase llamada Example que hereda de Thread
class Example(Thread):  
    def run(self):  # Método que se ejecutará al iniciar el hilo
        for i in range(400):  # Iteramos 400 veces para visualizar la concurrencia
            print("Hola por Example")  # Imprimimos un mensaje en la consola
            sleep(1)  # Pausamos por 1 segundo en cada iteración

# Definimos otra clase llamada ExampleTwo que también hereda de Thread
class ExampleTwo(Thread):  
    def run(self):  # Método que se ejecutará al iniciar el hilo
        for i in range(400):  # Iteramos 400 veces como en la primera clase
            print("Hola por ExampleTwo")  # Imprimimos un mensaje en la consola
            sleep(1)  # Pausamos por 1 segundo en cada iteración

# Creamos instancias de las clases Example y ExampleTwo
example = Example()  
exampleTwo = ExampleTwo()  

# Iniciamos los hilos llamando al método start()
example.start()  # Se inicia el primer hilo
sleep(0.1)  # Pequeña pausa para observar cómo se intercalan los mensajes
exampleTwo.start()  # Se inicia el segundo hilo

# Esperamos que los hilos terminen su ejecución antes de continuar con el hilo principal
example.join()  # El hilo principal espera a que termine 'example'
exampleTwo.join()  # El hilo principal espera a que termine 'exampleTwo'

# Una vez que ambos hilos terminan, el hilo principal imprime el mensaje final
print("Fin del programa")  # Indicamos el fin de la ejecución

""" - Sin join(): El hilo principal iniciaría los hilos y terminaría inmediatamente sin esperar su ejecución.
    - Con join(): Forzamos al hilo principal a esperar hasta que los hilos example y exampleTwo completen sus tareas antes de continuar.
Este enfoque garantiza que el programa solo imprimirá "Fin del programa" cuando ambos hilos hayan terminado su ejecución, lo que es clave en procesos concurrentes.
"""
#____________________________________________________________________________________________________________________________________________________________________________________________

#PROBLEMAS
#   A menudo se le denomina programación concurrente a multithrading
#   Crear apps que soporten esta funcionalidad es muy valioso actualmente
#   Pero la programación concurrente es un poco complicada
#   Normalme encontraremos dos problemas comunes: Interbloqueos y Condiciones de carrera
#       INTERBLOQUEOS
#           Donde un conjunto de procesos estan bloqueados porque cada proceso esta retneiendo un recurso y esperando otro recurso adquirido por algun otro proceso
#           Ocurre cuando diferente hilos o procesos intentan adquirir los recursos compartidos del sistema(forks) al mismo tiempo
#           Como resultado ninguno de los procesos tiene oportunidad de ejecutarse ya que estan esperando a otro recurso que esta siendo retenido por otro proceso
#       CONDICIONES DE CARRERA
#           Es la situación indeseable que ocurre cuando un dispositivo o un sistema intenta realizar dos o mas operaciones al mismo tiempo
#           Pero estas deberan hacerse en la secuencia decuada para hacerse de la manera correcta
#____________________________________________________________________________________________________________________________________________________________________________________________

from threading import *  # Importamos el módulo threading para manejar hilos
import threading  # Importamos threading explícitamente (aunque ya lo hicimos antes)
from time import sleep  # Importamos sleep para controlar el flujo de ejecución

# Creamos un objeto Lock para gestionar la sincronización entre hilos
Lock = threading.Lock()

# Definimos una clase Example que usa el bloqueo (Lock) para sincronizar el acceso
class Example(Thread):
    def run(self):  # Método que se ejecutará en el hilo
        for i in range(3):  # Iteramos 3 veces
            Lock.acquire()  # Adquirimos el bloqueo
            print("Lock Acquired")  # Indicamos que el bloqueo ha sido adquirido
            print("Hello from Example")  # Mensaje de Example
            sleep(1)  # Simulamos una tarea con pausa de 1 segundo
            Lock.release()  # Liberamos el bloqueo, permitiendo que otro hilo lo tome

# Definimos otra clase ExampleTwo que también usa el bloqueo
class ExampleTwo(Thread):
    def run(self):  # Método que se ejecutará en el hilo
        for i in range(3):  # Iteramos 3 veces
            Lock.acquire()  # Adquirimos el bloqueo
            print("Lock Acquired")  # Indicamos que el bloqueo ha sido adquirido
            print("Hello from ExampleTwo")  # Mensaje de ExampleTwo
            sleep(1)  # Simulamos una tarea con pausa de 1 segundo
            Lock.release()  # Liberamos el bloqueo

# Creamos instancias de las clases
example = Example()
exampleTwo = ExampleTwo()

# Iniciamos los hilos
example.start()
sleep(0.1)  # Pequeña pausa para observar la intercalación de hilos
exampleTwo.start()

"""- Corrección en los comentarios: realse() no es un método válido en Lock, el correcto es release().
    - Uso de Lock.acquire() y Lock.release():
    - Evita condiciones de carrera: Solo un hilo accede al recurso compartido a la vez.
    - Controla el acceso: Mantiene un orden predecible en la ejecución de los mensajes.
    - Breve pausa (sleep(0.1)) antes de iniciar el segundo hilo: Permite observar la ejecución sincronizada.
"""