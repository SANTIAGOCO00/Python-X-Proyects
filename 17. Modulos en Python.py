# MODULOS
#   Los modulos son archivos que contienen declaraciones y definiciones de Python
#   Son los codigos escritos por otra persona que podemos usar directamente en nuestro codigo
#___________________________________________________________________________________________________________________________________________________________________________________________

#TIPOS DE MODULOS
#   En general hay tres tipod de módulos en Python los cuales son:

#       MÓDULOS INTEGRADOS
#           Estan disponibles en Python por dfecto. Son desarrollados y mantenidos por el equipo de desarrolladoresde Python
#           Para usarlos solo debemos llamar los metodos. Ej: El modulo math que ofrece varias funciones matematicas

#       MÓDULOS DE TERCEROs
#           Debemos instalarlos para poder usarlos, y se usan de igual manera llamandolos una vez instalados
#           Se pueden descargar usando el comando pip. Es un gestor de paquetes para Python. Se cargan y almacenan en el repositorio PyPI(Pyhton Package Index)
#           syntax para descarga de modulos: pip install module_name

#       MÓDULOS PERSONALIZADOS
#           Son los modulos creados por nosotros los desarrolladores. Son Archivos que podemos importar a otro proyecto
#           Con ello podemos reutilizar nuestros codigos previamente creados en deviersos proyectos
#           Mejora la eficiencia el tener menos lineas de codigo
#___________________________________________________________________________________________________________________________________________________________________________________________

#¿CÓMO UAR UN MODULO?
#   A continuación se presentan las tres formas de utilizar un módulo de Python
#       The import statement
#       Import statement and renaming
#       The from...import statement

#IMPORTAR UN MÓDULO
#   Para usar un modulo primero debemos importarlo con: import
#       Syntax: import module_name Ej: import math

#   Para usar las iversas funciones del modulo importado usamos el operador punto (.)
#       Syntax: module_name.functionName() Ej: math.ceil(x)
#           module_name Es el nombre del módulo 
#           .funtionname() Es el nombre de la función que deseamos usar de ese módulo en particular

#RENOMBRAR UN MODULO
#   Podemos renombrar si deseamos el modulo al importarlo
#   Para ellos usamos...
#       Syntax: import module_name as m
#           module_name Es el nombre del módulo
#           m Es el nuevo nombre que le daremos y saremos en adelante

#DECLARACION From...import
#   Cuando unicamente queremos importar una función de un modulo sin importar el modulo en su totalidad usamos...
#       Syntax: from...import (atrivuto/funcion/clase)
#       Con ello el proyecto sera menos pesado y eficiente, cuando solo usamos lo que necesitamos
#       Syntax: FunctionName()

#EJEMPLO
#   Calcular el factorial de un número usando los diferentes metodos vistos anteriormente...
num=int(input("Digite el númer entero que desea factorizar: "))
import math #importar un modulo
print(math.factorial(num)) #Imprimimos: usando el modulo math y la función .factorial

import math as matematicas #Renombrar un modulo, en este caso a math le cambiamos el nombre a matematicas
print(matematicas.factorial(num)) #Imprrimimos: Usando el modulo matematicas con la función .factorial()

from math import factorial #Declaración from...import, from(de) math(modulo) import(importar) factorial(nombre de la función que necesitamos unicamente)
print(factorial(num)) #Imprimimos
#_________________________________________________________________________________________________________________________________________________________________________________________

#¿CUALES SON LOS MÓDULOS INTEGRADOS?
#   Como sabemos estan disponibles en Python por defecto. Son desarrollados y mantenidos por el equipo de desarrolladoresde Python
#   Acontinuación el listado...
"""	    __future__	Definiciones de declaraciones futuras
        __main__	El entorno donde se ejecuta el código de nivel superior. Abarca las interfaces de línea de comandos, el comportamiento en tiempo de importación y ``__name__ == '__main__'``.
        _thread	API de subprocesos de bajo nivel.
        _tkinter	Un módulo binario que contiene la interfaz de bajo nivel a Tcl/Tk.
            
        a	
        abc	Clases base abstractas según :pep:`3119`.
        aifc	Obsoleto: eliminado en 3.13.
        argparse	Biblioteca de análisis de argumentos y opciones de línea de comandos.
        array	Matrices de valores numéricos tipificados uniformemente y que ahorran espacio.
        ast	Clases y manipulación del árbol de sintaxis abstracta.
        asynchat	Obsoleto: eliminado en 3.12.
        asyncio	E/S asincrónica.
        asyncore	Obsoleto: eliminado en 3.12.
        atexit	Registrar y ejecutar funciones de limpieza.
        audioop	Obsoleto: eliminado en 3.13.
            
        b	
        base64	RFC 4648: Codificaciones de datos Base16, Base32, Base64; Base85 y ASCII85
        bdb	Marco de depuración.
        binascii	Herramientas para convertir entre sistemas binarios y diversas representaciones binarias codificadas en ASCII.
        bisect	Algoritmos de bisección de matrices para búsqueda binaria.
        builtins	El módulo que proporciona el espacio de nombres integrado.
        bz2	Interfaces para compresión y descompresión bzip2.
            
        do	
        calendar	Funciones para trabajar con calendarios, incluida alguna emulación del programa cal de Unix.
        cgi	Obsoleto: eliminado en 3.13.
        cgitb	Obsoleto: eliminado en 3.13.
        chunk	Obsoleto: eliminado en 3.13.
        cmath	Funciones matemáticas para números complejos.
        cmd	Construir intérpretes de comandos orientados a líneas.
        code	Facilidades para implementar bucles de lectura-evaluación-impresión.
        codecs	Codificar y decodificar datos y transmisiones.
        codeop	Compilar código Python (posiblemente incompleto).
        collections	Tipos de datos de contenedor
        colorsys	Funciones de conversión entre RGB y otros sistemas de color.
        compileall	Herramientas para compilar en bytes todos los archivos fuente de Python en un árbol de directorios.
        concurrent	
        configparser	Analizador de archivos de configuración.
        contextlib	Utilidades para contextos de declaraciones with.
        contextvars	Variables de contexto
        copy	Operaciones de copia superficial y profunda.
        copyreg	Registrar funciones de soporte de pickle.
        cProfile	
        crypt	Obsoleto: eliminado en 3.13.
        csv	Escribir y leer datos tabulares hacia y desde archivos delimitados.
        ctypes	Una biblioteca de funciones extranjeras para Python.
        curses (Unix)	Una interfaz para la biblioteca curses, que proporciona manejo de terminal portátil.
            
        d	
        dataclasses	Generar métodos especiales en clases definidas por el usuario.
        datetime	Tipos básicos de fecha y hora.
        dbm	Interfaces con varios formatos de "base de datos" de Unix.
        decimal	Implementación de la Especificación Aritmética Decimal General.
        difflib	Ayudantes para calcular diferencias entre objetos.
        dis	Desensamblador de código de bytes de Python.
        distutils	Obsoleto: eliminado en 3.12.
        doctest	Pruebe fragmentos de código dentro de cadenas de documentación.
            
        mi	
        email	Paquete que admite el análisis, la manipulación y la generación de mensajes de correo electrónico.
        encodings	
        ensurepip	Arrancar el instalador "pip" en una instalación de Python existente o en un entorno virtual.
        enum	Implementación de una clase de enumeración.
        errno	Símbolos del sistema errno estándar.
            
        F	
        faulthandler	Desechar el seguimiento de Python.
        fcntl (Unix)	Las llamadas al sistema fcntl() y ioctl().
        filecmp	Compare archivos de manera eficiente.
        fileinput	Realizar un bucle sobre la entrada estándar o una lista de archivos.
        fnmatch	Coincidencia de patrones de nombre de archivo en estilo shell Unix.
        fractions	Números racionales.
        ftplib	Cliente de protocolo FTP (requiere sockets).
        functools	Funciones y operaciones de orden superior sobre objetos invocables.
            
        gramo	
        gc	Interfaz con el recolector de basura de detección de ciclos.
        getopt	Analizador portátil para opciones de línea de comandos; admite nombres de opciones tanto cortos como largos.
        getpass	Lectura portátil de contraseñas y recuperación de id de usuario.
        gettext	Servicios de internacionalización multilingüe.
        glob	Expansión de patrón de ruta de acceso al estilo shell de Unix.
        graphlib	Funcionalidad para operar con estructuras tipo grafo
        grp (Unix)	La base de datos del grupo (getgrnam() y amigos).
        gzip	Interfaces para la compresión y descompresión gzip utilizando objetos de archivo.
            
        h	
        hashlib	Algoritmos seguros de hash y resumen de mensajes.
        heapq	Algoritmo de cola de montón (también conocido como cola de prioridad).
        hmac	Implementación de hash con clave para autenticación de mensajes (HMAC)
        html	Ayudantes para manipular HTML.
        http	Códigos y mensajes de estado HTTP
            
        i	
        idlelib	Paquete de implementación para el shell/editor IDLE.
        imaplib	Cliente de protocolo IMAP4 (requiere sockets).
        imghdr	Obsoleto: eliminado en 3.13.
        imp	Obsoleto: eliminado en 3.12.
        importlib	La implementación del mecanismo de importación.
        inspect	Extraer información y código fuente de objetos vivos.
        io	Herramientas básicas para trabajar con streams.
        ipaddress	Biblioteca de manipulación de IPv4/IPv6.
        itertools	Funciones que crean iteradores para realizar bucles eficientes.
            
        yo	
        json	Codificar y decodificar el formato JSON.
            
        k	
        keyword	Pruebe si una cadena es una palabra clave en Python.
            
        yo	
        linecache	Proporciona acceso aleatorio a líneas individuales de archivos de texto.
        locale	Servicios de internacionalización.
        logging	Sistema de registro de eventos flexible para aplicaciones.
        lzma	Un contenedor de Python para la biblioteca de compresión liblzma.
            
        metro	
        mailbox	Manipular buzones de correo en varios formatos
        mailcap	Obsoleto: eliminado en 3.13.
        marshal	Convierte objetos de Python en flujos de bytes y viceversa (con diferentes restricciones).
        math	Funciones matemáticas (sin() etc.).
        mimetypes	Asignación de extensiones de nombre de archivo a tipos MIME.
        mmap	Interfaz para archivos mapeados en memoria para Unix y Windows.
        modulefinder	Encuentra módulos utilizados por un script.
        msilib	Obsoleto: eliminado en 3.13.
        msvcrt (Ventanas)	Rutinas útiles diversas del entorno de ejecución de MS VC++.
        multiprocessing	Paralelismo basado en procesos.
            
        norte	
        netrc	Carga de archivos .netrc.
        nis	Obsoleto: eliminado en 3.13.
        nntplib	Obsoleto: eliminado en 3.13.
        numbers	Clases base abstractas numéricas (complejas, reales, integrales, etc.).
            
        o	
        operator	Funciones correspondientes a los operadores estándar.
        optparse	Biblioteca de análisis de opciones de línea de comandos.
        os	Interfaces de sistemas operativos misceláneos.
        ossaudiodev	Obsoleto: eliminado en 3.13.
            
        pag	
        pathlib	Rutas del sistema de archivos orientadas a objetos
        pdb	El depurador de Python para intérpretes interactivos.
        pickle	Convierte objetos de Python en flujos de bytes y viceversa.
        pickletools	Contiene comentarios detallados sobre los protocolos pickle y los códigos de operación de la máquina pickle, así como algunas funciones útiles.
        pipes	Obsoleto: eliminado en 3.13.
        pkgutil	Utilidades para el sistema de importación.
        platform	Recupera tantos datos de identificación de plataforma como sea posible.
        plistlib	Generar y analizar archivos plist de Apple.
        poplib	Cliente de protocolo POP3 (requiere sockets).
        posix (Unix)	Las llamadas al sistema POSIX más comunes (normalmente utilizadas a través del módulo os).
        pprint	Impresora de datos bonita.
        profile	Generador de perfiles de código fuente de Python.
        pstats	Objeto de estadísticas para utilizar con el generador de perfiles.
        pty (Unix)	Manejo de pseudo-terminales para Unix.
        pwd (Unix)	La base de datos de contraseñas (getpwnam() y amigos).
        py_compile	Generar archivos de código de bytes a partir de archivos fuente de Python.
        pyclbr	Admite la extracción de información para un navegador de módulos de Python.
        pydoc	Generador de documentación y sistema de ayuda en línea.
            
        q	
        queue	Una clase de cola sincronizada.
        quopri	Codifique y decodifique archivos utilizando la codificación MIME citada e imprimible.
            
        o	
        random	Generar números pseudoaleatorios con varias distribuciones comunes.
        re	Operaciones con expresiones regulares.
        readline (Unix)	Soporte de GNU readline para Python.
        reprlib	Implementación alternativa de repr() con límites de tamaño.
        resource (Unix)	Una interfaz para proporcionar información sobre el uso de recursos en el proceso actual.
        rlcompleter	Completado de identificador de Python, adecuado para la biblioteca GNU readline.
        runpy	Localice y ejecute módulos de Python sin importarlos primero.
            
        s	
        sched	Programador de eventos de propósito general.
        secrets	Genere números aleatorios seguros para gestionar secretos.
        select	Espere a que se complete la E/S en múltiples transmisiones.
        selectors	Multiplexación de E/S de alto nivel.
        shelve	Persistencia de objetos de Python.
        shlex	Análisis léxico simple para lenguajes tipo shell Unix.
        shutil	Operaciones de archivos de alto nivel, incluida la copia.
        signal	Establecer controladores para eventos asincrónicos.
        site	Módulo responsable de la configuración específica del sitio.
        sitecustomize	
        smtpd	Obsoleto: eliminado en 3.12.
        smtplib	Cliente de protocolo SMTP (requiere sockets).
        sndhdr	Obsoleto: eliminado en 3.13.
        socket	Interfaz de red de bajo nivel.
        socketserver	Un marco para servidores de red.
        spwd	Obsoleto: eliminado en 3.13.
        sqlite3	Una implementación de DB-API 2.0 utilizando SQLite 3.x.
        ssl	Envoltorio TLS/SSL para objetos de socket
        stat	Utilidades para interpretar los resultados de os.stat(), os.lstat() y os.fstat().
        statistics	Funciones de estadística matemática
        string	Operaciones de cadena comunes.
        stringprep	Preparación de cadenas, según RFC 3453
        struct	Interpretar bytes como datos binarios empaquetados.
        subprocess	Gestión de subprocesos.
        sunau	Obsoleto: eliminado en 3.13.
        symtable	Interfaz con las tablas de símbolos internas del compilador.
        sys	Acceda a parámetros y funciones específicos del sistema.
        sysconfig	Información de configuración de Python
        syslog (Unix)	Una interfaz para las rutinas de la biblioteca syslog de Unix.
            
        el	
        tabnanny	Herramienta para detectar problemas relacionados con espacios en blanco en archivos fuente de Python en un árbol de directorios.
        tarfile	Leer y escribir archivos de almacenamiento en formato tar.
        telnetlib	Obsoleto: eliminado en 3.13.
        tempfile	Generar archivos y directorios temporales.
        termios (Unix)	Control tty estilo POSIX.
        test	Paquete de pruebas de regresión que contiene la suite de pruebas para Python.
        textwrap	Ajuste y relleno de texto
        threading	Paralelismo basado en hilos.
        time	Acceso y conversiones de tiempo.
        timeit	Mide el tiempo de ejecución de pequeños fragmentos de código.
        tkinter	Interfaz con Tcl/Tk para interfaces gráficas de usuario
        token	Constantes que representan nodos terminales del árbol de análisis.
        tokenize	Escáner léxico para código fuente Python.
        tomllib	Analizar archivos TOML.
        trace	Rastrear o seguir la ejecución de declaraciones de Python.
        traceback	Imprima o recupere un seguimiento de la pila.
        tracemalloc	Rastrear asignaciones de memoria.
        tty (Unix)	Funciones de utilidad que realizan operaciones comunes de control de terminal.
        turtle	Un marco educativo para aplicaciones gráficas sencillas
        turtledemo	Un visor, por ejemplo, de scripts de tortugas.
        types	Nombres para tipos incorporados.
        typing	Soporte para sugerencias de tipo (ver :pep:`484`).
            
        tú	
        unicodedata	Acceda a la base de datos Unicode.
        unittest	Marco de pruebas unitarias para Python.
        urllib	
        usercustomize	
        uu	Obsoleto: eliminado en 3.13.
        uuid	Objetos UUID (identificadores únicos universales) según RFC 4122
            
        v	
        venv	Creación de entornos virtuales.
            
        o	
        warnings	Emitir mensajes de advertencia y controlar su disposición.
        wave	Proporciona una interfaz para el formato de sonido WAV.
        weakref	Soporte para referencias débiles y diccionarios débiles.
        webbrowser	Controlador fácil de usar para navegadores web.
        winreg (Ventanas)	Rutinas y objetos para manipular el registro de Windows.
        winsound (Ventanas)	Acceso a la maquinaria de reproducción de sonido para Windows.
        -	wsgiref	Utilidades WSGI e implementación de referencia.
            
        incógnita	
        xdrlib	Obsoleto: eliminado en 3.13.
        xml	Paquete que contiene módulos de procesamiento XML
        xmlrpc	Módulos de servidor y cliente que implementan XML-RPC.
            
        z	
        zipapp	Administrar archivos zip ejecutables de Python
        zipfile	Leer y escribir archivos de almacenamiento en formato ZIP.
        zipimport	Soporte para importar módulos Python desde archivos ZIP.
        zlib	Interfaz de bajo nivel para rutinas de compresión y descompresión compatibles con gzip.
        zoneinfo	Compatibilidad con zonas horarias de la IANA """
#____________________________________________________________________________________________________________________________________________________________________________________________


#MODULOS PERSONALIZADOS
#    Son los modulos creados por nosotros los desarrolladores. Son Archivos que podemos importar a otro proyecto
#    Con ello podemos reutilizar nuestros codigos previamente creados en deviersos proyectos
#    Mejora la eficiencia el tener menos lineas de codigo

#EJEMPLO:
#   Creemos una calculadora simple...
def suma(num1,num2): #Definimos la funcióon suma
    return num1+num2 #Retornamos las varibles num1+num2 a la función

def resta(num1,num2): #Definimos la funcióon resta
    return num1+num2 #Retornamos las varibles num1-num2 a la función

def multiplicación(num1,num2): #Definimos la función multiplicación
    return num1+num2 #Retornamos las varibles num1*num2 a la función

def division (num1,num2): #Definimos la función división
    return num1+num2 #Retornamos las varibles num1/num2 a la función
"""NOTA: Escribimos el codigo en un proyecto nuevo, donde lo guardamos como: calculator.py(py es la extensión)""" #Para usar este nuevo modulo personalizado usamos import

import calculator #Importamos nuestr modulo personalizado
a=int(input("Ingrese en primer número: ")) #El usuario ingresa el primer número
b=int(input("Ingrese el segundo número: ")) #El usuario ingresa el segundo número
print("La suma es", calculator.suma(a,b)) #Imprimimos: La suma es calculator(modulo que creamos).suma(metodo que creamos) y (a,b) (Para num1 y num2, respectivamente)

#IMPORTAMOS TODO EL MODULO ANTERIORMENTE, AHORA UNCICAMENTE EL METODO QUE NECESITAMOS QUE ES SUMA...
from calculator import suma
a=int(input("Ingrese en primer número: ")) #El usuario ingresa el primer número
b=int(input("Ingrese el segundo número: ")) #El usuario ingresa el segundo número
print("La suma es", suma(a,b)) #Imprimimos: La suma es suma(metodo que creamos) y (a,b) (Para num1 y num2, respectivamente)

"""NOTA: Los modulos personalizados que deseamos usar deben estar en la misma carpeta donde tenemos el proyecto"""




