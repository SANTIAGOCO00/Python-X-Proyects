#Importar modulos con import y from se añade de manera opcional para seleccionar solo una parte del codigo a importar (secciones de codigo ya esscritos para usar)
#_________________________________________________________________________________________________________________________________________________________________
#Algunas funciones matematicas del modulo math son: ceil(), floor(), sqrt(), pow(), sin(), cos(), tan(), log(), log10(), pi, e, etc.
#ceil(): devuelve el entero mayor o igual al numero
#floor(): devuelve el entero menor o igual al numero
#fabs(): devuelve el valor absoluto de un numero
#factorial(): devuelve el factorial de un numero
#fmod(): devuelve el resto de la division de dos numeros
#log2(): devuelve el logaritmo en base 2 de un numero
#log10(): devuelve el logaritmo en base 10 de un numero
#pow(): devuelve el resultado de elevar un numero a otro
#sqrt(): devuelve la raiz cuadrada de un numero
#trunc(): devuelve la parte entera de un numero
#math.pi: devuelve el valor de pi
#math.e: devuelve el valor de e
#math.inf: devuelve el valor de infinito
#math.nan: devuelve el valor de NaN (Not a Number)
#math.degrees(): convierte radianes a grados
#math.radians(): convierte grados a radianes
#math.factorial(): devuelve el factorial de un numero
#math.gcd(): devuelve el maximo comun divisor de dos numeros
#math.lcm(): devuelve el minimo comun multiplo de dos numeros
#math.isclose(): devuelve True si dos numeros son cercanos entre si
#math.isfinite(): devuelve True si un numero es finito
#math.isinf(): devuelve True si un numero es infinito
#math.isnan(): devuelve True si un numero es NaN (Not a Number)
#math.isqrt(): devuelve la raiz cuadrada entera de un numero
#math.perm(): devuelve el numero de permutaciones de n elementos tomados de r en r
#math.comb(): devuelve el numero de combinaciones de n elementos tomados de r en r
#math.dist(): devuelve la distancia entre dos puntos en un espacio n-dimensional    
#math.hypot(): devuelve la hipotenusa de un triangulo rectangulo
#math.prod(): devuelve el producto de los elementos de un iterable
#math.sum(): devuelve la suma de los elementos de un iterable
#math.copysign(): devuelve un numero con el signo de otro numero
#math.fsum(): devuelve la suma de los elementos de un iterable con mayor precision
#math.remainder(): devuelve el resto de la division de dos numeros
#math.trunc(): devuelve la parte entera de un numero
#math.degrees(): convierte radianes a grados
#math.radians(): convierte grados a radianes
#math.atan2(): devuelve el arco tangente de dos numeros
#math.atan(): devuelve el arco tangente de un numero
#math.acos(): devuelve el arco coseno de un numero
#math.asin(): devuelve el arco seno de un numero
#math.acosh(): devuelve el arco coseno hiperbólico de un numero
#etc...

#Ejemplo de uso de la libreria math
import math
print(math.sqrt(4)) #Salida: 2.0  
print(math.fabs(-5)) #Salida: 5.0 
print(math.floor(4.6)) #Salida: 4
print(math.pow(2,2)) #Salida: 4
print(math.trunc(7.999)) #Salida: 7
print(math.factorial(5)) #Salida: 120
 
 #Ejemplo 2
number = 12
print(math.factorial(number)) #Salida: 479001600
#__________________________________________________________________________________________________________________________________________________________________

#trigonometria en python: sin(), cos(), tan(), degrees(), radians(), etc...
#math.degrees() convierte radianes a grados
#math.radians() convierte grados a radianes
#math.sin() devuelve el seno de un angulo en radianes
#math.cos() devuelve el coseno de un angulo en radianes
#math.tan() devuelve la tangente de un angulo en radianes

import math
print(math.sin(0)) #Salida: 0.0
print(math.sin(3)) #Salida: 1.0
print(math.tan(3)) #Salida: -0.1425465430742778
print(math.cos(3)) #Salida: -0.9899924966004454

#___________________________________________________________________________________________________________________________________________________________________
#Constantes matematicas en python: pi, tau, e, inf, nan, etc...

import math
#math.pi devuelve el valor de pi
print(math.pi) #Salida: 3.141592653589793
#math.tau devuelve el valor de tau
print(math.tau) #Salida: 6.283185307179586
#math.e devuelve el valor de e
print(math.e) #Salida: 2.718281828459045
#math.inf devuelve el valor de infinito
print("Positive Infinity", math.inf) #Salida: infinito positivo
print("Negative Infinity", -math.inf) #Salida: infinito negativo

#Ejemplo 3
import math
radius = int(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print("The area of the circle is: ", area) #Salida: 78.53981633974483

#___________________________________________________________________________________________________________________________________________________________________
#Modulo random de Python: seed(), randrange(x,y,step),  randint(x,y), random(), choice(sequence), shuffle(sequence), sample(), etc...
#seed(): establece la semilla para el generador de numeros aleatorios
#randrange(x,y,step): devuelve un numero aleatorio entre x e y con un paso de step
#randint(x,y): devuelve un numero entero aleatorio entre x e y
#random(): devuelve un numero aleatorio entre 0 y 1
#choice(sequence): devuelve un elemento aleatorio de una secuencia
#shuffle(sequence): mezcla una secuencia
#sample(sequence, k): devuelve una lista de k elementos aleatorios de una secuencia

import random
print(random.random())
print(random.randint(1,100)) #Salida: 1-100
print(random.randrange(1,10)) #Salida: 1-10
print(random.randrange(1,10,2)) #Salida: 1-10 con paso de 2

#Ejemplo randrange: Genera un número aleatorio entre 1 y 10 con un paso de 3
print(random.randrange(1, 10, 3)) #Salida: 1-10 con paso de 3
print(random.randrange(1, 10, 3)) #Salida: 1-10 con paso de 3
print(random.randrange(1, 10, 3)) #Salida: 1-10 con paso de 3

#EJEMPLO 4: juego de adivinar el numero
import random
GenerateNumber = random.randrange(1,10) #Genera un numero aleatorio entre 1 y 10
UserGuess = int(input("Guess the number between 1 and 10: ")) #Pide al usuario que adivine el numero
if UserGuess == GenerateNumber: #Si el numero adivinado es igual al numero generado
    print("You guessed it right!") #Salida: Adivinaste el numero
elif UserGuess < GenerateNumber: #Si el numero adivinado es menor que el numero generado
    print("Your guess is too low!") #Salida: Tu adivinanza es muy baja
elif UserGuess > GenerateNumber: #Si el numero adivinado es mayor que el numero generado
    print("Your guess is too high!") #Salida: Tu adivinanza es muy alta