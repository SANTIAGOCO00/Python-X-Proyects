""" 
PROYECTO DOS - APLICACIÓN DE GESTIÓN DE BIBLIOTECA
En este proyecto, crearemos una Aplicación de Gestión Bibliotecaria qué tendrá las siguientes funciones:
    - Obtener todos los libros disponibles en la biblioteca
    - Agregar nuevos libros
    - Lleva un registro de los libros prestados
    - Actualiza los detalles según los libros devueltos

FLUJO DEL PROYECTO
- Mostrar ek menú de de la aplicación de gestión de bibliotecas
    Opciones del menú
    1. Mostrar Libros
    2. Prestar un Libro
    3. Añadir un Libro
    4. Devolver un Libro

- Dependiendo de la opción ingresada, necesitaríamos realizar la operación y devolver los detalles a la pantalla de salida

- El proceso anterior se debe hacer repetidamente hasta que el usuario se retire

ENFOQUE
El enfoque principal sera en OOP, tendremos una clase que será responsable de la creación del objeto "Biblioteca".
Y un solo objeto biblioteca representará una biblioteca.
"""
class Biblioteca:  # Definimos una clase llamada "Biblioteca" que representará nuestra biblioteca.
    def __init__(self, ListadeLibros, Nombre):
        """
        Método constructor (__init__) que inicializa la biblioteca con una lista de libros disponibles
        y un nombre que identifica la biblioteca.
        """
        self.ListadeLibros = ListadeLibros  # Guardamos la lista de libros disponibles en un atributo de la clase.
        self.Nombre = Nombre  # Guardamos el nombre de la biblioteca.
        self.DicPrestar = {}  # Creamos un diccionario vacío para llevar un registro de los libros prestados.

"""
La clase Biblioteca esta lista, ahora crearemos los metodos necesios para ella. para cada funcionalidad,
Tendremos un método diferente, como se muestra a continuación:
    - Obtener todos los libros disponibles en la Biblioteca - MostrarLibros()Su objetivo será obtener los nombres de todos los libros disponibles en la biblioteca
    - Agregar nuevos libros - AñadirLibros()
    - Lleve un registro de los libros prestados - PrestarLibros()
    - Actualizalos detalles según los libros devueltos - DevolverLibros()
"""
class Biblioteca:  # Definimos una clase llamada "Biblioteca" que representará nuestra biblioteca.
    def __init__(self, ListadeLibros, Nombre):
        """
        Método constructor que inicializa la biblioteca con una lista de libros disponibles
        y un nombre que la identifica.
        """
        self.ListadeLibros = ListadeLibros  # Guardamos la lista de libros disponibles en la biblioteca.
        self.Nombre = Nombre  # Almacenamos el nombre de la biblioteca.
        self.DicPrestar = {}  # Diccionario que llevará el registro de los libros prestados.

    def MostrarLibros(self):
        """
        Método que muestra todos los libros disponibles en la biblioteca.
        """
        print(f"Tenemos los siguientes libros en nuestra biblioteca: {self.Nombre}")  # Mostramos el nombre de la biblioteca.
        for Libro in self.ListadeLibros:  # Recorremos la lista de libros disponibles.
            print(Libro)  # Imprimimos cada libro en la lista.

    def AñadirLibros(self, Libro):
        """
        Método que permite añadir un nuevo libro a la biblioteca.
        """
        if Libro in self.ListadeLibros:  # Verificamos si el libro ya existe en la lista.
            print("El libro ya existe")  # Informamos al usuario si el libro ya está registrado.
        else:
            self.ListadeLibros.append(Libro)  # Agregamos el libro si no está en la lista.
            BasedeDatosLibro = open(BasedeDatosNombre, "a")
            BasedeDatosLibro.write("\n")
            BasedeDatosLibro.write(Libro)
            print("Libro agregado exitosamente.")  # Confirmamos la operación.

    def PrestarLibros(self, Libro, Usuario):
        """
        Método que permite prestar un libro a un usuario.
        """
        if Libro in self.ListadeLibros:  # Verificamos si el libro está disponible en la biblioteca.
            if Libro not in self.DicPrestar.keys():  # Comprobamos si el libro no ha sido prestado aún.
                self.DicPrestar.update({Libro: Usuario})  # Registramos el préstamo del libro al usuario.
                print("Libro prestado. Base de datos actualizada.")  # Confirmamos que el préstamo se realizó correctamente.
            else:
                print(f"El libro ya está siendo utilizado por: {self.DicPrestar[Libro]}")  # Informamos quién tiene el libro actualmente.
        else:
            print("¡Disculpas! No tenemos este libro en nuestra biblioteca.")  # Informamos que el libro no existe en el catálogo.

    def DevolverLibros(self, Libro):
        """
        Método que permite devolver un libro prestado.
        """
        if Libro in self.DicPrestar.keys():  # Comprobamos si el libro está registrado como prestado.
            self.DicPrestar.pop(Libro)  # Eliminamos el libro de la lista de préstamos.
            print("Libro devuelto exitosamente.")  # Confirmamos que el libro ha sido devuelto.
        else:
            print("El libro no existe en la base de datos de préstamos de libros.")  # Informamos si el libro no estaba prestado.

    def main():
        while(True):
            print(f"Bienvenido a la biblioteca {Biblioteca.Nombre}. A continuación, las opciones:")
            choice = """
            1. Mostrar Libros
            2. Prestar Libros
            3. Añadir Libros
            4. Devolver Libros
            """
            print(choice)

            AportedeUsuario = input("Presiona Q para salir y C para continuar: ")
            if AportedeUsuario == "C":
                ElecciondeUsuario = int(input("Seleccione una opción para continuar: "))
                if ElecciondeUsuario == 1:
                    Biblioteca.MostrarLibros()
                
                elif ElecciondeUsuario == 2:
                    Libro = input("Introduce el nombre del libro que deseas que te presten: ")
                    Usuario = input("Introduzca el nombre del usuario: ")
                    Biblioteca.PrestarLibros(Libro, Usuario)

                elif ElecciondeUsuario == 3:
                    Libro =input("Introduce el nombre del libro que deseas Añadir: ")

                    Biblioteca.AñadirLibros(Libro)
                elif ElecciondeUsuario == 4:
                    Libro = input("Introduzca el nomnre del libro que desea regresar: ")
                    Biblioteca.DevolverLibros(Libro)
                
                else:
                    print("Por favor escoja una opción valida")
            
            elif AportedeUsuario == "Q":
                break

            else:
                print("Por favor intoduzca una opción valida")

if __name__ == "__main__":
    ListadeLibros = []
    BasedeDatosNombre = input("Introduzca el nombre del archivo de base de datos con extensión: ")
    BasedeDatosLibro = open(BasedeDatosNombre, "r")
    for Libro in BasedeDatosLibro:
        ListadeLibros.append(Libro)
    Biblioteca = Biblioteca(ListadeLibros,"PythonX")
    Biblioteca.main()
