# PROYECTO TRES, APLICACIÓN CRUD(Create, Read, Update, Delete) DE EMPLEADOS
"""
 ¿DE QUE SE TRATA EL PROYETO?
    Crearemos una aplicación GUI simple que interactuara con la base de datos MySQL y nos ayudará a realizar operaciones CRUD.
    La aplicación tendra las siguientes funcionalidades:
        - Insertar y almacenar detalles de empleados como ID de Empleado, Nombre de Empleado, y Departamento de Empleado en la base datos.
        - Realizar varias operaciones como optener datos, actualizar datos existentes, y mas...
        - Mostrando todos los datos disponibles es la base de datos.
        - Una interfaz gráfica de ususario simple para realizar todas las operacioens anteriores.

 FLUJO DEL PROYECTO
    1. Crear una GUI simple que permita interactuar con la aplicación y realizar operaciones sobre la base de datos.
    2. La GUI tendría las siguientes opciones para Insertar, Actualizar, Obtener y Eliminar los Datos.
       Además tendríamos que una opción de Restablecer que reiniciará todos los campos.
    3. Añadiríamos una ventana para mostrar los datos en tiempo real siemper que se realicen las operaciones.
    """

#INICIO EN MySQL
"""
 INICIO
    Primero iremos a MySQL y creemos lla base de datos de Empleados requerida y la tabla empDetails en ella.
    La tabla empDetails tendrá los siguientes campos...

        empId:      Almacenará el ID del empleados y será de tipo INT. Dado que cada empleado tendrá un ID único,
                    declararemos este campo como la CLAVE PRIMARIA.
        empName:    Almacenará el departamento del empleado y será de tipo VARCHAR.
        empDept:    Este cacmpo almacenará el departamento de del empleado y sera de tipo VARCHAR.

CREAMOS EN MySQL:
    CREATE DATABASE employee;
    SHOW DATABASES;
    USE employee;
    CREATE TABLE empDetails(empID int PRIMARY KEY, empName varchar(100), empDept varchar(100));
    DESCRIBE empDetails;
"""

# DESARROLLANDO LA GUI
"""
 Nuestra GUI contara con los siguientes Wdgets:
    - Label
    - Entry
    - Buttons
    - ListBox
    - Parent Window
"""

from tkinter import *                      # Importa todos los elementos de tkinter, biblioteca para crear interfaces gráficas.
from tkinter import messagebox            # Importa funciones para mostrar mensajes emergentes (alertas, info, advertencias).
import mysql.connector                    # Importa el conector para interactuar con bases de datos MySQL.

# Insertar...

def insertData():
    id = enterld.get()                    # Obtiene el texto ingresado en el campo de ID.
    name = enterName.get()                # Obtiene el texto ingresado en el campo de nombre.
    dept = enterDept.get()                # Obtiene el texto ingresado en el campo de departamento.

    if(id == "" or name == "" or dept == ""):  # Verifica si algún campo está vacío.
        messagebox.showwarning("Cannot Insert", "All the fields are requeried!")  # Muestra advertencia si faltan datos.
    else:
        myDB = mysql.connector.connect(
            host="localhost", user="root", passwd="Santiago.MySQL", database="employee")  # Conexión a la base de datos.
        myCur = myDB.cursor()             # Crea un cursor para ejecutar comandos SQL.
        myCur.execute("insert into empDetails values(""+id +"", "" + name +"", ""+ dept +"")")  # Inserta datos. (Revisar uso de comillas y concatenación)
        myDB.commit()                     # Confirma la transacción.

        enterld.delete(0, "end")          # Limpia el campo de ID.
        enterName.delete(0, "end")        # Limpia el campo de nombre.
        enterDept.delete(0, "end")        # Limpia el campo de departamento.

        messagebox.showinfo("Insert Status", "Data Inserted Successfully")  # Muestra mensaje de éxito.
        myDB.close()                      # Cierra la conexión a la base de datos.

# Actualizar...

def updateData():
    id = enterld.get()
    name = enterName.get()
    dept = enterDept.get()

    if(id == "" or name == "" or dept == ""):
        messagebox.showwarning("Cannot Update", "All the fields are required")  # Verifica si faltan campos.
    else:
        myDB = mysql.connector.connect(
            host="localhost", user="root", passwd="Santiago.MySQL", database="employee")
        myCur = myDB.cursor()
        myCur.execute("Update empDetails set empName="" + name + "", empDept="" + dept + ""where empld="" +id + """)  # Actualiza los datos. (Revisar)
        myDB.commit()

        enterld.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

        messagebox.showinfo("Update Status", "Data Updated Successfully")
        myDB.close()

# Obtener...

def getData():
    if(enterld.get() ==""):
        messagebox.showwarning("Fetch Status", "Please provide the Emp ID to the fetch the data")  # Solicita el ID si no fue ingresado.
    else:
        myDB = mysql.connector.connect(
            host="localhost", user="root", passwd="Santiago.MySQL", database="employee")
        myCur = myDB.cursor()
        myCur.execute("Select * from empDetails where empID="" + enterld.get() + """)  # Consulta para obtener el registro por ID. (Revisar)
        rows = myCur.fetchall()           # Recupera los resultados.

        for row in rows:                  # Muestra los datos en los campos correspondientes.
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])

            #Eliminar?  # (Comentario suelto sin funcionalidad)

# Eliminar...

def deleteData():
    if(enterld.get() ==""):
        messagebox.showwarning("Cannot Delete", "Please provide the Emp ID to delete the data")  # Solicita ID para eliminar.
    else:
        myDB = mysql.connector.connect(
            host="localhost", user="root", passwd="Santiago.MySQL", database="employee")
        myCur = myDB.cursor()
        myCur.execute("delete from empDetails where empID="" + enterld.get() + """)  # Elimina registro por ID. (Revisar)
        myDB.commit()

        enterld.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

        messagebox.showinfo("Delete Status", "Data Deleted Successfully")
        myDB.close()

# CRUD

def show():
    myDB = mysql.connector.connect(
        host="localhost", user="root", passwd="Santiago.MySQL", database="employee")
    myCur = myDB.cursor()
    myCur.execute("select * from empDetails")  # Recupera todos los registros.
    rows = myCur.fetchall()
    showData.delete(0, showData.size())  # Limpia la lista antes de mostrar nuevos datos.

    for row in rows:
        addData = str(row[0]) + " " + row[1] + " " + row[2]  # Convierte el registro a cadena.
        showData.insert(showData.size() + 1, addData)        # Inserta en el Listbox.

        myDB.close()  # Cierra la conexión (Nota: está dentro del bucle, se ejecutará solo una vez pero está mal ubicado).

# ResetFields()...

def resetFields():
    enterld.delete(0, "end")  # Limpia el campo de ID.
    enterName.delete(0, "end")  # Limpia el campo de nombre.
    enterDept.delete(0, "end")  # Limpia el campo de departamento.

# GUI Part

window = Tk()
window.geometry("600x270")  # Establece las dimensiones de la ventana.
window.title("Employee CRUD App")  # Establece el título de la ventana.

# (All Labels) Añadiendo widgets de Etiqueta y Entrada...

empld = Label(window, text = "Employee ID", font=("Serif", 12))
empld.place(x=20, y=30)

empName = Label(window, text="Employe Name", font=("Serif", 12))
empName.place(x=20, y=60)

empDept = Label(window, text="Employee Dept", font=("Serif", 12))
empDept.place(x=20, y=90)

# All Entry Boxes respective to labels

enterld = Entry(window)
enterld.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

# Añadiendo Botones...

insertBtn = Button(window, text="Insert", font=("Sans", 12), bg="white", command=insertData)
insertBtn.place(x=20, y=160)

updateBtn = Button(window, text="Update", font=("Sans", 12), bg="white", command=updateData)
updateBtn.place(x=80, y=160)

getBtn = Button(window, text="Fetch", font=("Sans", 12), bg="white", command=getData)
getBtn.place(x=150, y=160)

deleteBtn = Button(window, text="Delete", font=("Sans", 12), bg="white", command=deleteData)
deleteBtn.place(x=210, y=160)

resetBtn = Button(window, text="Reset", font=("Sans", 12), bg="white", command=resetFields)
resetBtn.place(x=20, y=210)

# Agregando Listbox...

showData = Listbox(window)
showData.place(x=330, y=30)

window.mainloop()  # Ejecuta la ventana principal, inicia el bucle de eventos de la GUI.
