#PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
#   En programación, existen diferentes paradigmas o patrones que definen cómo escribir y estructrar un codigo
#   Cada paradigma tiene diferentes funcionalidades y comportamientos. Tales como:

#       PROGRAMACIÓN ESTRUCTURADA
#           Estructura el codigo que representa los datos con algunas funcionalidades básicas

#       PROGRAMACIÓN PROCEDURAL
#           Usa  funciones como bloques de construcción

#       PROGRAMACIÓN ORIENTADA A OBJETOS o OOP (Clases y Objetos)
#           Es un enfoque para modelar cosas concretas, del mundo real, y las relaciones entre esas cosas

#       Y mas...
#______________________________________________________________________________________________________________________________________________________________________________________

#PRINCIPIOS DE LA PROGRAMACIÓN ORIENTADA A OBJETOS
#   Los 4 principios/propiedades (pilares) de OOP son...

#       ABSTRACCIÓN
#           Abstraer solo los detalles/datos que puedan concernir al usuario
#           Ocultando los detalles de fondo o la implementación

#       ENCAPSULACIÓN
#           La abstracción y encapsulación van de la mano
#           Tratamos de encapsular todos los datos como una sola entidad, Tenemos la entrada, procesamiento y salida

#       HERENCIA
#           Orientada a objetos y soporta el concepto de reusabilidad
#           Cuando queremos crear una función y esta ya existe podemos simplemente incluirla en el codigo que necesitamos en vez de crearla

#       POLIMORFISMO
#           Significa tener muchas formas
#           Capacidad de diferentes objetos de responder de manera distinta a un mismo llamado de método, manteniendo una interfaz común
#_____________________________________________________________________________________________________________________________________________________________________________________

#BLOQUES DE CONSTRUCCIÓN
#   Abstracción, Encapsulación, Herencia y Polimorfismo (Son los 4 pilares)
#   Clases y Objetos son los bloques de construcción de la programación Orientada a Objetos OOP

#       CLASES
#           Es un tipo de estructura definida por el usuario que puede almacenar varios atributos
#           Datos primitivos o definidos por el usuario, junto con sus funcionalidades, todo como una sola unidad

#       OBJETOS
#           Son una instancia de la clase, Un objeto cuenta con dos cosas Atributos(Data variables of the class) y Comportamientos(Functions defined in the class)

#       EJEMPLO:
#           Los planos de un edificio serian una clase
#           Color, piso, apartamentos, entrada etc... serian los Atributos
#           EstaOcupado(), EstaLibre() etc.. serian los comportamientos
#______________________________________________________________________________________________________________________________________________________________________________________

#TRABAJANDO CON CLASES Y OBJETOS

#   Syntax para definir una clase...
#       class className: (Cuerpo de la clase)
#           class: es la palabra clave de Python para definir una clase
#           className: Nombre que le asignamos a la clase, similar auna variable o función

#   EJEMPLO:
#       Definamos una clase que nos ayudará a almacenar y procesar los detalles de los empleados
class Empleados:
    pass #pass es sólo un marcador temporal hasta que añadamos uncionalidades necesarias, pass es ignorada por el interpete ya que es vista como una declaración nula
#____________________________________________________________________________________________________________________________________________________________________
#Ahora nuevamente agrgando algunos atributos (Variables que contenran datos) a la clase Empleados..
class Empleados:
    EmpName = "John"
    Age = 35
    Designation = "Manager"
#Ahora creemos un Objeto usando la siguiente syntax: objName = className()
EmpOne = Empleados()
print(EmpOne.EmpName) #Imprimimos: John
#_______________________________________________________________________________________________________________________________________________________________________________________

#CONSTRUCTOR
#   Los constructores se usan generalmente para inicializar(asignar valores) los miembros de datos de la clase cuando se crea un objeto de la clase
#   syntax: def_init_(delf):

#   Existen dos tipos de constructores: Constructor por defecto y Constructor parametrizado...

#       CONSTRUCTOR POR DEFECTO
#           No acepta ningun argumento. Su definición tiene un solo argumento(self) que es referencia la instancia que se esta construyendo
#           syntax: objName = className()

#       CONSTRUCTOR PARAMETRIZADO
#           Toma el primer argumento como refenrencia a la instancia conocida como self y el resto de los argumentos se proporcionan
#           Estos son los atrivutos requeridos para la clase. Necesitaremos crear y pasar los argumentos similar a una función
#           syntax: objName = className(paraOne, paraTwo, etc...)


#USANDO _init_()
#   Ejemplo: Definamos una clase que nos ayudará a almacenar y procesar los detalles de los empleados
#   pero que sea dinamica para tener diferentes datos para diferentes objetos. Para ello usamos _init_()

class Empleados:# Método de inicialización de la clase
    def __init__(self,EmpName,Age,Designation): # def(difinimos) _ _ init _ _ (self,) 
        # Asignación de valores a los atributos del objeto
        self.EmpName = EmpName
        self.Age = Age
        self.Designation = Designation

# Creación de instancias de la clase Empleados
EmpOne = Empleados("Jhon",35,"Manager")
EmpTwo = Empleados("Sam",26,"Desarrollador de Python")

# Imprimir los nombres de los empleados
print(EmpOne.EmpName)
print(EmpTwo.EmpName)

#________________________________________________________________________________________________________________________________________________________________________________________

#AGREGANDO METODOS
#   Ejemplo: Definamos una clase que nos ayudará a almacenar y procesar los detalles de los empleados
class Empleados:  # Definimos la clase Empleados
    TotalEmpleados = 0  # Atributo de clase para contar el número total de empleados
    
    def __init__(self, EmpName, Age, Designation, Salary):  # Método de inicialización (__init__)
        # Asignación de valores a los atributos de la instancia (cada empleado tiene sus propios valores)
        self.EmpName = EmpName  # Nombre del empleado
        self.Age = Age  # Edad del empleado
        self.Designation = Designation  # Cargo o puesto de trabajo
        self.Salary = Salary  # Salario del empleado
        
        # Incrementar el contador de empleados cada vez que se crea una nueva instancia
        Empleados.TotalEmpleados += 1

    # Método para obtener los detalles del empleado como una tupla
    def GetEmpDetails(self):  
        return self.EmpName, self.Age, self.Designation, self.Salary

    # Método para actualizar el salario del empleado
    def UpdateSalary(self, NewSalary):
        self.Salary = NewSalary  # Se actualiza el atributo Salary
        print("Actualización Salarial: ")  # Mensaje de actualización
        return self.Salary  # Devuelve el nuevo salario 

# Creación de instancias de la clase Empleados
EmpOne = Empleados("John", 35, "Manager", 35000)
print(EmpOne.GetEmpDetails())  # Se llama correctamente al método con paréntesis ()

EmpTwo = Empleados("Sam", 26, "Desarrollador de Python", 27000)
print(EmpTwo.GetEmpDetails())  # Se llama correctamente al método con paréntesis ()

# Actualización del salario y visualización de los detalles del empleado
EmpOne.UpdateSalary(40000)
print(EmpOne.GetEmpDetails())

# Imprimir el número total de empleados creados
print(Empleados.TotalEmpleados)

#________________________________________________________________________________________________________________________________________________________________________________________

#HERENCIA
#   Clase Padre: La clase padre es la clase que se hereda de las otras clases. También se llama la clase base
#   Clase Hija: La clase hija es la clase que hereda de la clase padre. Tambien se le conoce como clase derivada
#       Syntax..
class ClasePadre:
    pass  # Indica que el cuerpo de la clase está vacío por ahora
class ClaseHija(ClasePadre):
    pass  # También puede estar vacío por ahora
#________________________________________________________________________________________________________________________________________________________________________________________
#   EJEMPLO:
class Empleados:  # Definimos la clase Empleados
    TotalEmpleados = 0  # Atributo de clase para contar el número total de empleados

    def __init__(self, EmpName, Age, Designation, Salary):  # Método de inicialización (__init__)
        # Asignación de valores a los atributos de la instancia (cada empleado tiene sus propios valores)
        self.EmpName = EmpName  # Nombre del empleado
        self.Age = Age  # Edad del empleado
        self.Designation = Designation  # Cargo o puesto de trabajo
        self.Salary = Salary  # Salario del empleado
        
        # Incrementar el contador de empleados cada vez que se crea una nueva instancia
        Empleados.TotalEmpleados += 1

    # Método para obtener los detalles del empleado como una tupla
    def GetEmpDetails(self):  
        return self.EmpName, self.Age, self.Designation, self.Salary

    # Método para actualizar el salario del empleado
    def UpdateSalary(self, NewSalary):
        self.Salary = NewSalary  # Se actualiza el atributo Salary
        print("Actualización Salarial: ")  # Mensaje de actualización
        return self.Salary  # Devuelve el nuevo salario

class Intern(Empleados): #La clase hija(Intern) hereda de la clase padre(Empleados)
    pass #Pasamos, ya que esta vacio por ahora
interOne = Intern("Tom", 22, "Marketing", 12000)
print(interOne.GetEmpDetails()) #Obtiene los detalles del interno(intern)
#______________________________________________________________________________________________________________________________________________________________________________________________

"""AHORA, AÑADAMOS ALGO DENTRO DE LA CLASE HIJA Y RETIRAMOS EL pass ya que no va estar vacia..."""

class Empleados:  # Definimos la clase Empleados
    TotalEmpleados = 0  # Atributo de clase para contar el número total de empleados

    def __init__(self, EmpName, Age, Designation, Salary):  # Método de inicialización (__init__)
        # Se asignan valores a los atributos del objeto empleado
        self.EmpName = EmpName  # Nombre del empleado
        self.Age = Age  # Edad del empleado
        self.Designation = Designation  # Cargo o puesto de trabajo
        self.Salary = Salary  # Salario del empleado

        # Se incrementa el contador de empleados cuando se crea una nueva instancia
        Empleados.TotalEmpleados += 1

    def GetEmpDetails(self):  # Método que devuelve los detalles del empleado
        return self.EmpName, self.Age, self.Designation, self.Salary

    def UpdateSalary(self, NewSalary):  # Método para actualizar el salario del empleado
        self.Salary = NewSalary  # Se actualiza el atributo Salary
        print("Actualización Salarial:")  # Mensaje de confirmación
        return self.Salary  # Devuelve el nuevo salario

# Definimos una clase Intern que hereda de Empleados
class Intern(Empleados):  # La clase hija Intern hereda de la clase Empleados
    pass  # Se deja vacío por ahora, sin métodos específicos

# Creación de una instancia de Intern (sin atributos adicionales)
internOne = Intern("Tom", 22, "Marketing", 12000)
print(internOne.GetEmpDetails())  # Se obtiene la información del interno

# AHORA, definimos Intern con un atributo adicional específico para los internos
class Intern(Empleados):  # La clase hija Intern hereda de la clase Empleados
    def __init__(self, EmpName, Age, Designation, Salary, InternPeriod):  # Método de inicialización (__init__)
        self.InternPeriod = InternPeriod  # Atributo adicional: duración de la pasantía en meses
        
        # Llamamos al constructor de la clase padre para inicializar los atributos heredados
        Empleados.__init__(self, EmpName, Age, Designation, Salary)

    def GetInternPeriod(self):  # Método para obtener el período de pasantía
        return "El periodo del empleado interno en meses es", self.InternPeriod

"""Explicación:
   - En lugar de redefinir todos los atributos heredados, solo definimos los nuevos para la clase hija.
   - Luego llamamos al constructor de la clase base (padre) dentro del constructor de la clase derivada (hija).
   - Esto se hace usando la siguiente sintaxis:
     Empleados.__init__(self, parametro1, parametro2, parametro3, etc...)
"""

# Creación de una instancia de Intern con su período de pasantía
InternOne = Intern("Tom", 22, "Marketing", 12000, 6)
print(InternOne.GetEmpDetails())  # Se obtienen los detalles del interno
print(InternOne.GetInternPeriod())  # Se obtiene el período de pasantía

#____________________________________________________________________________________________________________________________________________________________________________________________

#TIPOS DE HERENCIA
#   HERENCIA MULTINIVEL
#       Los atributos y comportamientos de la clase base y derivada se heredan además en la nueva clase derivada
class Empleados():
    pass
class Intern(Empleados):
    pass
class Bonus(Intern): #Aqui la clase Bonus puede acceder a Intern y Empleados ya que hereda Intern e Intern a su vez hereda Empleados
    pass  

#   HERENCIA MÚLTIPLE
#       Cuando una clase puede derivarse de más de una clase base, este tipo de herencia se le llama herencia multiple
class Company:
    pass
class Empleados:
    pass
class Intern(Company,Empleados): #Aqui la clase Bonus puede acceder a Intern y Empleados
    pass

#   HERENCIA JERARQUICA
#       Cuando se crea mas de una clase derivada a partir de una sola clase base
class Company:
    pass
class Empleados(Company):
    pass
class Intern(Company): 
    pass
"""En este caso la clase Company hereda mas de dos clases derivadas"""

#___________________________________________________________________________________________________________________________________________________________________________________________

#POLIMORFISMO EN PYTHON
#   Significa muchas formas. Encontramos do tipos de polimorfismo
#       SOBRECARGA DE MÉTODOS (NO COMPATIBLE CON PYTHON)
#           Es la situación en la que hay dos métodos con el mismo nombre pero con diferentes parámetros en la misma clase
""" class Geometry:
        method area(lenght,breath):
            return lenght * breath
    method area (side):
        return side * side """ 

#       SOBRECRITURA DE MÉTODOS
#           Es la situación donde hay dos métodos con el mismo nombre y los mismos parametros, pero en dos clases diferentes
class base:
    def method(self):
        print("método de clase base llamado")

class derived(base):
    def method(self):
        print("método de clase base llamado")
Objeto1 = derived()
Objeto1.method() #Este ejemplo ilustra el funcionamiento de la sobre escritura de métodos en Python