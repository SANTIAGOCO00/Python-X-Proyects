""" DBMS (Sistema de gestión de Bases de Datos)
    Para trabajar con sistemas de bases de datos relacionales, usamos algo llamado SQL

    SQL:Es el lenguaje estándar para sistemas de bases de datos y existen diferentes versiones de lenguaje como:
        MySQL, MS Access, Oracle,Sybase, Informix, Postgres, SQL Server, y más que dependen de SQL y lo utilizan como base.
        MySQL es una de las versiones en esta sección en Pyhton...

    MySQL: Es un sistema de Gestión de Bases de datos Relacional (RDBMS) de código abierto y disponible de forma gratuita,
           que utiiza Lenguaje de Consulta Estructurada (SQL)

        Field          - Cada Tabla se divide en entidades más pequeñas llamadas fields.
        registro       - Un registro, tambien llamado fila de datos, es cada entrada individual que existe en una tabla.
        Columna        - Una Columna es una entidad vertical dentro de una tabla que contiene toda la información asociada con un campo específico en una tabla.
        Valor NULL     - Un valor NULL en un tabla es un valor en un campo que parece estar en blanco, lo que significa que un campo con un valor NULL es un campo sin valor.
        Clave Primaria - Una clave primaria nos ayuda a identificar de manera única una fila en la tabla. Un valor de clave no puede ocurrir dos veces en una tabla.
        Clave Foránea  - Una clave foránea actúa como un enlace entre dos tablas

    A continuación se presentan algunos de los tipos de datos mas usados en MySQL

        INT           - Es un número entero de tamaño normal. Podemos especificar un ancho de hasta 11 dígitos. Requiere 4 bytes para almacenamiento
        FLOAT(m,d)    - Es un número de punto flotante. Puedes definir la logitud de visualización (m) y el número de decimales (d)
                        Esto no es requerido y por defecto será 10,2 donde 2 es el número de decimales , y 10 es eñ número total de digitos(Incluyendo decimales)
        BOOL          - Solo se usa para condiciones verdadderas y falsas. Considera el valor numérico 1 como verdadero y 0 como falso
        CHAR(size)    - Puede tenerun tamaño máximo de 255 caracteres. Aquí size es el número de caracteres a almacenar.
        VARCHAR(size) - Puede tener un tamaño máximo de 255 caracteres. Aquí size es el número de caracteres a almacenar. Cadena de longitud variable.
"""

#DAMOS INCIO A CREAR NUESTRA BASE DE DATOS EN EL PROGRAMA MySQL de ORACLE ...
"""     1. Para crear una base de datos en MySQL usamos la siguiente syntax: CREATE DATABASE database_name;
        Aqui database_name es el nombre de nuestra base de datos que debe ser unica en MySQL
        Ademas, cada declaración en MySQL debe terminar con un pun y coma (;)

        2. Una vez creada la base de datos, podemos crear varias tablas en ella y comenzar a llenar los datos
        A continuación se muestra el comando que devolverá todas las bases de datos disponibles en el sistema: SHOW DATA BASES

        3. Usamos la instrucción USE para acceder a la base de datos que nos permie  crear una tabla y otros objetos de base de datos
        A continuación se muestra la syntax para ello: USE database_name
        database_name es el nombre de una base de datos que desea usar

        NOTA: Podemos eliminar una base de datos  usando la instrucción DROP
        A continuación se muestra las syntax: DROP DATABASE database_name;
        database_name es el nombre de una base de datos que deseamos eliminar
"""

#CREACIÓN DE TABLAS
""" Podemos crear una tabla en MySQL usando el comando CREATE TABLE
    A continuación  se muestra la syntax para crear una tabla: CREATE TABLE table_name(columnName1 data_type, columnName2 data_type, ...);
    Aqui los elementos de una tabla se definen entre paréntesis. columnName1 data_type es la definición de columna,
    donde data_type define el tipo de datos que se almacenará en la columna
"""

#CREAREMOS UNA TABLA CON LAS SIGUIENTES RESTICCIONES
""" userld
    username
    email
    userType

    Haremos la restricción userld como la PRIMARY KEY. Esta restricción identifica de maner única cada registro en una tabla.
    Las claves primarias deben contener vloers Únicos, y no puede contener valores Nulos.
    Ademas una tabla solo puede contener una clave primaria
"""
#RESUMEN DE LO QUE HICIMOS EN MySQL
"""
    Cada línea del código es una instrucción que le dice a MySQL qué hacer. Aquí lo explico en términos simples:
    1️⃣ SHOW DATABASES;
    - 👉 ¿Qué hace? Muestra todas las bases de datos que existen en el servidor MySQL.
    - 💡 Ejemplo: Es como pedirle a una computadora que muestre todos los archivos guardados en ella.

    2️⃣ USE pythonx;
    - 👉 ¿Qué hace? Le dice a MySQL que trabaje con la base de datos pythonx.
    - ⚠️ Nota: Antes de usar una base de datos, debe existir. Si pythonx no ha sido creada, dará un error.

    3️⃣ CREATE TABLE user(...);
    - 👉 ¿Qué hace? Crea una tabla llamada user donde se almacenarán datos de usuarios.
    - 📌 Columnas:
    - userId: Número único para cada usuario.
    - username: Nombre del usuario, hasta 10 letras.
    - email: Correo electrónico, hasta 25 letras.
    - userType: Tipo de usuario (por ejemplo, "PRO" o "REGULAR").
    - 💡 Ejemplo: Es como crear una hoja de cálculo con columnas para organizar información.

    4️⃣ SHOW TABLES;
    - 👉 ¿Qué hace? Muestra todas las tablas dentro de la base de datos pythonx.
    - 💡 Ejemplo: Es como mirar las diferentes hojas de una libreta.

    5️⃣ SELECT * FROM user;
    - 👉 ¿Qué hace? Muestra todos los usuarios guardados en la tabla user.
    - 💡 Ejemplo: Como abrir un archivo y ver toda la lista de contactos.

    6️⃣ INSERT INTO user VALUES(...);
    - 👉 ¿Qué hace? Agrega un usuario nuevo a la tabla.
    - 📌 Ejemplo:
    INSERT INTO user VALUES(1526, 'John', 'john@example.com', 'PRO');

    - El usuario John con ID 1526, correo john@example.com y tipo PRO se agrega.
    7️⃣ Otro INSERT INTO user VALUES(...);
    - 👉 ¿Qué hace? Agrega otro usuario, Smith, con ID 6745, correo smith@example.com y tipo "REGULAR".

    8️⃣ SELECT * FROM user;
    - 👉 ¿Qué hace? Muestra todos los datos de la tabla después de haber agregado usuarios.

    9️⃣ SELECT userId, userType FROM user;
    - 👉 ¿Qué hace? Muestra solo dos columnas: el ID del usuario y su tipo.
    - 💡 Ejemplo: Es como pedir que te muestren solo el número de teléfono y el nombre de un contacto, ignorando el resto.

    🔟 SELECT * FROM user WHERE userType = 'PRO';
    - 👉 ¿Qué hace? Filtra y muestra solo los usuarios que tienen el tipo "PRO".
    - 💡 Ejemplo: Es como buscar solo los contactos VIP en una agenda.

    🎯 Resumen Final
    ✅ Creamos una base de datos y una tabla.
    ✅ Insertamos datos en la tabla.
    ✅ Consultamos y filtramos información de los usuarios.
    📢 ¡Ya está! Con este código, puedes crear y gestionar información de usuarios en MySQL de manera básica.
"""

#CONECTAR MySQL a PYTHON (Usando el modulo en Python mysql.connector - Devemos instalarlo en la TERMINAL antes de usarlo)
""" Una vez instalado mysql.connector podremos crear la conexión entre la plicación y la base de datos
    Para ello saremos elmétodo connect() del módulo mysql-connector
    syntax: databaseObject(= mysql.connector.connect(host = <host-name>, user = <username>, paswd = <password>)"""

import mysql.connector


myDB = mysql.connector.connect(host="localhost", user="root",passwd="Santiago.MySQL")
print("Conexión exitosa con MySQL:", myDB)


#PASOS PARA EJECUTAR CONSULTAS EN MySQL
""" 1. Crea el objeto de conexión de la base de datos
    2. Cree el objeto cursor
    3. Haz la llamada al metodo execute() """