"""
GUI
 Interfaz Grafica Visual para interactuar con el usuario
 Para ello usaremos la bilioteca Tkinter

   TKINTER
        Es un modulo untegrado de Python que se usa para aplicaciones GUI
           Syntax: import tkinter (Luego debemos seguir los sencillos pasos seguientes...)
           1. Importarel modulo
           2. Crea la ventana principal
           3. Agregue cualquier número de widgets a la ventana principal
           4. Aplica el disparador de eventos en los widgets

        Para ello usaremos WIDGETS algunas clases son las siguientes...
            Label        - Se utiliza para proporcionar un título de una sola línea para otros widgets. 
                           Se usa para mostrar texto y también puede contener. Syntax: ObjectName = Label(parent, options) 
            Botón        - Se utiliza para agregar botones a la aplicación.
                           Estos botones pueden realizar varias acciones al hacer click en ellos.
            Entry        - Es justo como la función input() de python, pero de naturaleza más GUI.
                           Se usa para aceptar la entrada de usuario.
            Texto        - Es un Widget de entrada de texto que permite la entrada de texto multilinea.
            Frame        - Se utiliza como un widget contenedor para organizar otros widgets.
            ComboBox     - Contiene una flecha hacia abajo para seleccionar de la lista de opciones disponibles.
            Checkbutton  - Se usa para mostrar varias opciones como casillas de verificación.
                           El usuario puede seleccionar multiples opciones a la vez.
            Radiobutton  - Se usa para mostrar una serie de opciones como botones de radio.
                           El usuario solo puede seleccionar una opción a la vez.
            PanedWindow  - Es un Widget contenedor que puede contener cualquier número de paneles.
                           dispuestos horizontalmente o verticalmente.
            Canvas       - Se usa para dibujar formas, como lineas, óvalos, poligonos, rectangulos, en tu aplicación.
            TkMessageBox - No es un Widget, es un modulo completo de Python.
                           Se usa para mostrar cuadrados de mensaje (dialogo) en nuestras aplicaciones.
"""
# Daremos inicio con nuestra primera aplicacion...
# Iniciamos con una ventana, Es un contenedor en el que se colocan todos los demás elementos de la GUI

from tkinter import* # Usamos from import para importar el modulo tkinter y usamos * para importar todo de una manera que no necesitamos prefijarlos al usuario
window = Tk() # Creamos una ventana raiz llamando a Tk() , Esto crea una ventana grafica con la barra de título, minimizar, maximizar, y botones de cerrar. window wa un objeto la clase Tk()
window.mainloop() # La ventana de la plicación no aparece antes de que entre en el boble principal
                  # Este metodo, renderiza y responde a cualquier interacción, el programa permanece en bucle hasta que cerremos la ventana

"""
GESTIÓN DE GEOMETRIA
El diseño de tkinter está controlado por los Geometry Managers. No sayuda a colocar y organizar varios widgets en la ventana.
Para ello debemos llamar a los metodos especiales de GESTIÓN GEOMETRICA, a continuación se presentan los tres metodos proporcionados por tkinter para ello.

    pack()
        Organiza los widgets en bloques antes de colocarlos en widget padre.
        Coloca los widgets en el orden dado en que son creados.
        Podemos usar el metodo pack() para el gestor de geometría pack
         syntax: widget.pack(pack_options)
                 widget es el widget GUI que deseas colocar en el contenedor principal.
                 se llama a pack() en el widget que deseamos colocar
                 Este metodo toma varias opciónes opcionales (parametros) que nos ayudan a manipular el widget. con las siguientes opciones...
                 (expand, fill, lado)

    grid()
        Organiza los widgets en una estructura similar a una tabla en el widget principal.
        Coloca los widgets en una tabla bidimensional. Es uno de los gestores mas usados en tkinter,
        Y podemos usar el grid() para implementar la geometria cuadrada.
            syntax: widget.grid(grid_options)
                    widget es el widget GUI que deseas colocar en el contenedor principal.
                    grid() se llama en el widget que deseamos colocar
                    Este metodo toma varias opciónes opcionales (parametros) que nos ayudan a manipular el widget. con las siguientes opciones...
                    (fila, columna, rowspan, columnspan, sticky)
    
    place()
        Organiza los widgets colocándolos en una posición especifica en el widget padre.
        Es el mas sencilo de los tres administradores generales de geometria en tkinter.
        Establece esplicitamente: posición y tamaño de una ventaa, ya sea en términos absolutos , o en relación con otra ventana
            syntax: widget.place(place_options)
                 widget es el widget GUI que deseas colocar en el contenedor principal.
                 place() se llama en el widget que deseamos colocar
                 Este metodo toma varias opciónes opcionales (parametros) que nos ayudan a manipular el widget. con las siguientes opciones...
                 (height,width - x,y - relx,rely - relheight,relwith - bordermode)                                                          
"""

# Importamos todos los elementos de la librería Tkinter, que sirve para crear interfaces gráficas.
from tkinter import *

# Creamos una ventana principal de la aplicación.
window = Tk()

# Definimos un widget de tipo etiqueta (Label) dentro de la ventana.
# Esta etiqueta mostrará el texto "PythonX - Learn Python" con fondo blanco y letras azules en fuente Serif de tamaño 16.
name = Label(window, text="PythonX - Learn Python", bg="white", fg="Blue", font=("Serif", 16))

# Colocamos la etiqueta en la ventana utilizando pack(), que automáticamente ajusta su posición.
name.pack()

# Ejecutamos el bucle principal de la ventana, permitiendo que la interfaz permanezca activa y responda a eventos.
window.mainloop()
#_________________________________________________________________________________________________________________________________________________________________________________________

#CODIGO: NO ABRE YA QUE EL ARCHIVO NO EXISTE
"""
Instalamos el modulo Pillow de terceros en Python directamente en la terminal, para poder manejar imagenes en el widget de etiqueta: pip install Pillow

# Importamos la clase Image de la biblioteca PIL (Pillow), que sirve para trabajar con imágenes.
from PIL import Image

# Abrimos una imagen llamada "Python.png" utilizando el método open() de la clase Image.
img = Image.open("Python.png")

# Mostramos la imagen en la pantalla con el método show().
img.show()
"""
#________________________________________________________________________________________________________________________________________________________________________________________

#CODIGO: NO ABRE YA QUE EL ARCHIVO NO EXISTE
"""
# Importamos todos los elementos de la librería Tkinter, que se usa para crear interfaces gráficas en Python.
from tkinter import *

# Importamos ImageTk y Image de la biblioteca PIL (Pillow), que nos permite trabajar con imágenes en la interfaz gráfica.
from PIL import ImageTk, Image

# Creamos la ventana principal de la aplicación.
window = Tk()

# Creamos un widget de tipo etiqueta (Label) dentro de la ventana.
# Mostrará el texto "PythonX - Learn Python" con fondo negro, texto blanco y fuente Serif tamaño 16.
name = Label(window, text="PythonX - Learn Python", bg="black", fg="White", font=("Serif", 16))

# Abrimos una imagen llamada "Python.png" utilizando el método open() de la clase Image.
# Nota: Hay un error tipográfico en el nombre del archivo. En el código original se escribió "Pyhton.png", pero debería ser "Python.png".
img = Image.open("Python.png")  # Corregido

# Convertimos la imagen a un formato compatible con Tkinter utilizando ImageTk.PhotoImage().
logo = ImageTk.PhotoImage(img)

# Creamos otra etiqueta para mostrar la imagen dentro de la ventana.
image = Label(window, image=logo)

# Usamos el método pack() para añadir la etiqueta de texto a la ventana y organizar su posición automáticamente.
name.pack()

# Usamos pack() también para la imagen, colocándola en la ventana.
image.pack()

# Ejecutamos el bucle principal de la ventana, lo que permite que la interfaz permanezca abierta y responda a eventos.
window.mainloop() 
"""
#_______________________________________________________________________________________________________________________________________________________________________________________

# ELEMENTO DE ENTRADA
"""
    Ahora crearemos un campo de entrada para aceptar el nombre del usuario
    Podemos usar el widget Entry para aceptar la entrada de una sola línea de un usuario

        Sintax: objetcName = Entry (parent, options)
            objectName:       - Sera el objeto de la clase Entry. Podemos darle cualquier nombre, 
                                al igual que un nombre de .
            Entry():          - Sera la llamada a la clase Label que tiene dos parametros (padre, opciones)
            Parent/Padre:     - Representa la ventana principal en la que se colocará el widget.
            Options/Opciones: - Son parametros adicionales que ayudan a manipular y personalizar el campo Entry (bg, fg, comando, front, justificar, mostrar, estado)

    METODOS DE ENTRY
        get()                  - Devuelve el texto actual de la entrada como una cadena. En pocas palabras, se utiliza para optener el valor que se ha ingresado en el campo de entrada.
        delete()               - Elimina caracteres del widget.
        insert(index, "data")  - Inserta la cadena "data" antes del caracter en el indice dado.
"""
#_______________________________________________________________________________________________________________________________________________________________________________________

#CODIGO: NO ABRE YA QUE EL ARCHIVO NO EXISTE
"""
# Importamos los módulos necesarios
from tkinter import *  # Tkinter nos permite crear interfaces gráficas
from PIL import ImageTk, Image  # PIL nos ayuda a manipular imágenes

# Creamos la ventana principal
window = Tk()  

# Creamos un Label (etiqueta) para mostrar el nombre de la aplicación
name = Label(window, text="PythonX - Learn Python", bg="white", fg="blue", font=("Serif", 16))

# Abrimos la imagen y la convertimos para que pueda ser usada en Tkinter
img = Image.open("Python.png")  # Cargamos la imagen desde el archivo
logo = ImageTk.PhotoImage(img)  # Convertimos la imagen para que Tkinter pueda manejarla

# Creamos un Label para mostrar la imagen
image = Label(window, image=logo)

# Creamos otro Label para mostrar el texto "Username"
username = Label(window, text="Username", font=("Serif", 12))

# Creamos un campo de entrada para que el usuario pueda escribir su nombre
inputBox = Entry(window)  

# Empaquetamos (organizamos) los elementos en la ventana
name.pack()  # Muestra el título de la aplicación en la ventana
image.pack()  # Muestra la imagen cargada en la ventana
username.pack(side=LEFT)  # Coloca la etiqueta "Username" a la izquierda
inputBox.pack(side=RIGHT)  # Coloca el campo de entrada a la derecha

# Iniciamos el bucle principal de la interfaz gráfica
window.mainloop()  # Permite que la ventana se mantenga abierta y sea interactiva
"""
#_________________________________________________________________________________________________________________________________________________________________________________________

# WIDGET BUTTON
"""
Para añadir un botón clicable que acionen una función demos hacerlo con la siguiente Syntax
   Syntax: objectName = Button (parent, options)
    Options/opciones: Text, bg, fg, command, fuente, height-weight, image, stade
"""

# ACTUALIZAMOS EL MISMO CODIGO AÑADIEDO EL BOTOÓN
"""
# Importamos los módulos necesarios
from tkinter import *  # Tkinter nos permite crear interfaces gráficas
from PIL import ImageTk, Image  # PIL nos ayuda a manipular imágenes

# Creamos la ventana principal
window = Tk()

# Creamos un Label (etiqueta) para mostrar el nombre de la aplicación
name = Label(window, text="PythonX - Learn Python", bg="white", fg="blue", font=("Serif", 16))

# Abrimos la imagen y la convertimos para que pueda ser usada en Tkinter
img = Image.open("Python.png")  # Cargamos la imagen desde el archivo
logo = ImageTk.PhotoImage(img)  # Convertimos la imagen para que Tkinter pueda manejarla

# Creamos un Label para mostrar la imagen
image = Label(window, image=logo)

# Creamos otro Label para mostrar el texto "Username"
username = Label(window, text="Username", font=("Serif", 12))

# Creamos un campo de entrada para que el usuario pueda escribir su nombre
inputBox = Entry(window)

# Creamos un botón y definimos su acción
button = Button(window, text="Enviar")  # Botón con el texto "Enviar"

# Empaquetamos (organizamos) los elementos en la ventana
name.pack()  # Muestra el título de la aplicación en la ventana
image.pack()  # Muestra la imagen cargada en la ventana
username.pack(side=LEFT)  # Coloca la etiqueta "Username" a la izquierda
inputBox.pack(side=RIGHT)  # Coloca el campo de entrada a la derecha
button.place(x=100, y=350)  # Posiciona el botón en las coordenadas (100, 350)

# Iniciamos el bucle principal de la interfaz gráfica
window.mainloop()  # Permite que la ventana se mantenga abierta y sea interactiva
"""
#__________________________________________________________________________________________________________________________________________________________________________________________

# WIDGET DE MARCO
"""
   Un marco se usa como widget contenedor para organizar otro widgets
    Syntax: objectName =  Frame (parent, options) 
     altura,  ancho y bg
"""

#CODIGO
# Importamos el módulo Tkinter para crear la interfaz gráfica
from tkinter import *

# Creamos la ventana principal
window = Tk()

# Creamos un marco (Frame) dentro de la ventana principal
frame = Frame(window)  # Un Frame es un contenedor que agrupa otros widgets

# Creamos una etiqueta (Label) dentro del marco
lbl = Label(frame, text="Inside the frame")  # Muestra un texto dentro del Frame

# Creamos un botón (Button) dentro del marco
btn = Button(frame, text="Inside the frame")  # Botón con texto dentro del Frame

# Empaquetamos (organizamos) los elementos en la ventana
frame.pack()  # Añade el marco a la ventana principal
lbl.pack(side=TOP)  # Coloca la etiqueta en la parte superior dentro del Frame
btn.pack(side=BOTTOM)  # Coloca el botón en la parte inferior dentro del Frame

# Iniciamos el bucle principal de la interfaz gráfica
window.mainloop()  # Permite que la ventana se mantenga abierta y sea interactiva
#___________________________________________________________________________________________________________________________________________________________________________________________

# WIDGET CHECKBUTTON
"""
Muestra varias opciones como casillas de verificación
    Syntax: objetname = Checkbutton (parent, options)
        Opciones: offvalue, onvalue, estado, text, imagen, command
        Metodos: deselect(), invoke(), select()
"""
# CODIGO
# Importamos el módulo Tkinter para crear la interfaz gráfica
from tkinter import *

# Creamos la ventana principal
window = Tk()

# Creamos una etiqueta (Label) para mostrar el título de la selección de lenguajes
lbl = Label(window, text="Choose your favorite programming languages: ")  # Texto que indica al usuario qué hacer

# Creamos un marco (Frame) que contendrá los botones de selección
frame = Frame(window)  # Un Frame ayuda a organizar varios elementos dentro de un mismo contenedor

# Creamos botones de selección (Checkbutton) para diferentes lenguajes de programación
python = Checkbutton(frame, text="Python")  # Opción para Python
java = Checkbutton(frame, text="Java")  # Opción para Java
js = Checkbutton(frame, text="JavaScript")  # Opción para JavaScript 
cpp = Checkbutton(frame, text="C++")  # Opción para C++

# Organizamos los elementos dentro de la ventana
lbl.pack()  # Muestra la etiqueta con el mensaje principal
frame.pack()  # Agrega el marco a la ventana
python.pack()  # Muestra el botón de selección para Python
java.pack()  # Muestra el botón de selección para Java
js.pack()  # Muestra el botón de selección para JavaScript
cpp.pack()  # Muestra el botón de selección para C++

# Iniciamos el bucle principal de la interfaz gráfica
window.mainloop()  # Mantiene la ventana abierta e interactiva
#___________________________________________________________________________________________________________________________________________________________________________________________

# RADIO BUTTON WIDGET
"""
    Muestra varias opciones como botones de radio
        Syntax: objectName = Radiobutton(parent, options)
            Opciones: texto, imaen, comando, state, variable, value
            Metodo: deselect(), invoke(), selelct()
"""
#CODIGO
# Importamos el módulo Tkinter para crear la interfaz gráfica
from tkinter import *

# Creamos la ventana principal
window = Tk()

# Creamos una etiqueta (Label) para mostrar el texto "GENDER:"
lbl = Label(window, text="GENDER: ")  # Indica que se debe seleccionar un género

# Creamos una variable de tipo StringVar() que será usada por los botones de opción
var = StringVar()  # Variable que almacenará la opción seleccionada (M o F)

# Creamos un botón de opción (Radiobutton) para "Male"
male = Radiobutton(window, text="Male", variable=var, value="M")  # Si se selecciona, var tendrá el valor "M"

# Creamos un botón de opción (Radiobutton) para "Female"
female = Radiobutton(window, text="Female", variable=var, value="F")  # Si se selecciona, var tendrá el valor "F"

# Organizamos los elementos dentro de la ventana
lbl.pack()  # Muestra la etiqueta con el texto "GENDER:"
male.pack()  # Muestra el botón de opción "Male"
female.pack()  # Muestra el botón de opción "Female"

# Iniciamos el bucle principal de la interfaz gráfica
window.mainloop()  # Mantiene la ventana abierta e interactiva
#__________________________________________________________________________________________________________________________________________________________________________________________

# MessageBox
"""
  Es un aventana emergente y cuadros de dialogo  
    Syntax de imporatción: from tkinter import messagebox
    Syntax de uso: messagebox.functionName(title, message, options)
        FuntionName - Nombre de la función de la caja apropiada.
        title       - Es el texto que se mostrará en la barra de título de un cuadro de mensaje.
        message     - Es el texto que se mostrará en la barra de título de un cuadro de mensajes.
        options     - Opciones alternativas que puedes usar para personalizar un cuadro de mensaje estándar.
    
    FUNCIONES DE MESSAGEBOX:
        showinfo()
        showwarning()
        showererror()
        askquestions()
        askokcancel()
        askyesno()
        askretrycancel()
"""
#__________________________________________________________________________________________________________________________________________________________________________________________

# MANEJO DE EVENTOS
"""
    Existen dos maneras de manejar eventos en Tkinter para que la GUI sea interactiva
        Usando la función bind()
            La función bind() vincula el evento y ejecuta la función siempre que ocurren los eventos
                Syntax: widget.bind(event, handler)
                    Events en Pyhton: <Button>, <Buttonrealse>, <Double-Button>, <Focusin>, <FocusOut>, <Key>

        Usando la opción de comando
            Todos los widgets proporcioan la opción de comando, que llama a un método cada vez queel usuario interactua
                Syntax: objectName = Widget (command = function_Name)
"""

# CODIGO: no funciona ya que el archivo de imagen no existe

# Importamos los módulos necesarios
from tkinter import *  # Tkinter nos permite crear interfaces gráficas
from PIL import ImageTk, Image  # PIL nos ayuda a manipular imágenes
from tkinter import messagebox  # Para mostrar mensajes emergentes

# Definimos una función para saludar al usuario cuando haga clic en el botón
def greetUser(event):
    username = inputBox.get()  # Obtiene el texto del campo de entrada
    greet["text"] = "Welcome " + username  # Actualiza el texto de la etiqueta greet

# Definimos la función que muestra un cuadro de diálogo con un mensaje
def showMessage():
    messagebox.showinfo("PythonX - Learn Python", "Welcome")  # Muestra un mensaje emergente

# Creamos la ventana principal
window = Tk()

# Creamos un Label (etiqueta) para mostrar el nombre de la aplicación
name = Label(window, text="PythonX - Learn Python", bg="white", fg="blue", font=("Serif", 16))

# Abrimos la imagen y la convertimos para que pueda ser usada en Tkinter
img = Image.open("Python.png")  # Cargamos la imagen desde el archivo
logo = ImageTk.PhotoImage(img)  # Convertimos la imagen para que Tkinter pueda manejarla

# Creamos un Label para mostrar la imagen
image = Label(window, image=logo)

# Creamos un marco (Frame) que nos ayudará a organizar los elementos
frame = Frame(window)

# Creamos otro Label para mostrar el texto "Username"
username = Label(frame, text="Username", font=("Serif", 12))  # Se coloca dentro del frame

# Creamos un campo de entrada para que el usuario pueda escribir su nombre
inputBox = Entry(frame)  # También dentro del frame

# Creamos un botón y definimos su acción
button = Button(window, text="Let's Start", command=showMessage)  # Botón con el texto "Let's Start"

# Vinculamos el botón con la función greetUser cuando se haga clic en él
button.bind("<Button-1>", greetUser)

# Creamos una etiqueta vacía que mostrará el saludo
greet = Label(window)

# Empaquetamos (organizamos) los elementos en la ventana
name.pack()  # Muestra el título de la aplicación en la ventana
image.pack()  # Muestra la imagen cargada en la ventana
frame.pack()  # Agrega el frame antes de empaquetar los elementos dentro de él
username.pack(side=LEFT)  # Coloca la etiqueta "Username" a la izquierda dentro del frame
inputBox.pack(side=RIGHT)  # Coloca el campo de entrada a la derecha dentro del frame
button.pack()  # Posiciona el botón en la parte inferior
greet.pack()  # Muestra el saludo generado

# Iniciamos el bucle principal de la interfaz gráfica
window.mainloop()  # Permite que la ventana se mantenga abierta y sea interactiva

# Corrección de error en la condición "__name__"
if __name__ == "__main__":
    showMessage()  # Llama a la función showMessage si el script se ejecuta directamente