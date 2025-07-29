"""
CAJERO DE SUPERMERCADO EN PYTHON
    Aceptara el nombre del producto comprado por el consumidor y la cantidad del producto comprado.
    El proceso anterior debe repetirse hasta que se hayan inscrito todos los productos.
    Luego aceptaremos la membresía del supermercado del consumidor y dependiendo del tipo de membresia daremos un descuento.
    Tendremos 3 membresias: Gold 20%, Silver 10% y Bronze 5% de descuento.
    Finalmente calcularemos el monto total de la factura dependiendo del precio de los productos y imprimiremos la factura detallada en la pantalla de salida.
___________________________________________________________________________________________________________________________________________________________________________________________
ACEPTAR PRODUCTOS
    Crearemos una función que aceptara dos cosas del usuario: Nombre del producto y cantidad del producto. Seguido a ello debemos almacenar tanto el nombre como su cantidad correspodiente 
    en una estructura de datos, por lo tanto almacenaremos nombre y cantidad en un diccionario, donde el nombre del producto sera la clave y la cantidad su valor (Clave-Valor).

REPITE EL PROCESO
    Ya que el numero de articulos comprados no es fijo debemos repetir el proceso anterior hasta que se hayan ingresado todos los productos y sus precios. Debido a que no sabemos cuantas
    cuantas veces se repetira el proceso usaremos un bucle while
    
CODIGO..."""
def Enter_Products(): #def(definimmos) una función vacia que llevara por nombre: Enter_Products():
    Buying_Data = {} #Creamos un diccionario vacio llamado: Buying_Data={}
    Enter_Details = True #Creamos una variable(bandera) de bucle (tipo bool: Verdadero o falso) que sera verdadera: Enter_Details=True. Apara permitir que el codigo se ejecute al menos una vez y solicite al usuario que ingrese algunos datos.
    while Enter_Details: #Usamos el siclo while(mientras) que Enter_Details sea verdadera 
        Details = input("Presiona A para añadir un producto y Q para quitar: ") #Creamos una variable que se llame Details, con salida al usuario para que elija A o Q
        if Details == "A": #Si la variable detalles es A...
            Product = input("Igrese un producto: ") #El usuario ingresara un producto que se almacenara en la variable Product
            Quantity = int(input("Introduzca la cantidad: ")) #El usuario ingresara la cantidad del producto en numeros enteros que se almacenara en la variable Quantity
            Buying_Data.update({Product:Quantity}) #A nuestro diccionario vacio Buying_Data{} le adicionamos el metodo .update() para añadir los elementos clave(Product)-valor(Quantity) 
        elif Details == "Q": #elif(Entonces si) la variable detalles es "Q"...
            Enter_Details = False #la variable de bucle sera falsa y saldremos del bucle El usuario eliminara quitara un producto
        else: #Si no se cumple ("A" o "Q")
            print("Seleccione una opción correcta") #Imprime: Seleccione una opción correcta
    return Buying_Data #Return regresa los datos y finaliza la función retornando al codigo
def Get_Price(Product,Quantity): #def(definimos) una función que llevara por nombre: Get_Price() esta contendra los parametros el Product y Quantity que retornamos en la función Enter_Products()
    Price_Data = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3} #Creamos un diccionario predefinido donde: Product que es la Clave y el precio de ese producto como su valor
    Subtotal = Price_Data[Product]*Quantity #Operamos: El diccionario Price_data con el producto dentro del argumento[Product] *(Multiplicado) por la cantidad del producto
    print(Product + ":$" + str(Price_Data[Product]) + "x" + str(Quantity) + "=" + str(Subtotal)) #Imprime: la operación visible al usuario de la linea anterior, Como algunos caracteres son enteros debemos usar str() para converitrlos en una cadena organizada 
    return Subtotal #Return regresa los datos y finaliza la función retornando al codigo
def Get_Discount(BillAmount,MemberShip): #def(definimos) una función que llevara por nombre: Get_Discount() esta contendra dos nuevos parametros BillAmount(Monto de la factura) y Membership(Membresia)
    Discount = 0 #Creamos una nueva varible(Discount) a la cual le asignamos el valor de 0 para inicializar
    if BillAmount >= 25: #Solo si, el monto de la factura es mayor o igual a $25 calcularemos el descuento. Con un if else anidado a continuación... 
        if MemberShip == "Gold": #Y si, la mebresia es igual a Gold 
            BillAmount = BillAmount * 0.80 #El monto de la factura sera igual al monto de la factura multiplicado por 0.80
            Discount = 20 #El valor del descuento sera 20
        elif MemberShip == "Silver": #Y si, la mebresia es igual a Silver...
            BillAmount = BillAmount * 0.90 #El monto de la factura sera igual al monto de la factura multiplicado por 0.90
            Discount = 10 #El valor del descuento sera 10
        elif MemberShip == "Bronze": #Y si, la mebresia es igual a Bronze...
            BillAmount = BillAmount * 0.95 #El monto de la factura sera igual al monto de la factura multiplicado por 0.95
            Discount = 5 #El valor del descuento sera 5
        print((str(Discount)) + "% Descuento por " + MemberShip + " memebership on total amount: $" + str(BillAmount)) #Imprime: (Discount)% Descuento por membresía sobre el monto total: $(BillAmount)
    else: #Si no se cumple ninguns de las condiciones anteriores...
        print("Para acceder a un descuento el valor debe ser superior a $25") #Imprime: Para acceder a un descuento el valor debe ser superior a $25
    return BillAmount #Return regresa los datos y finaliza la función retornando al codigo
def Make_Bill(Buying_Data,Membership): #def(definimos) una función que llevara por nombre: Make_Bill() esta contendra los parametros Buying_Data(Diccionario de Datos de compra) y Membership(Membresia)
    BillAmount = 0 #A nuestra variable BillAmount(Monto de la factura) le asignamos el valor de 0 para inicializar, cntendra el monto subtotal del consumidor
    for Key, Value in Buying_Data.items(): #Usamos el bucle de iteración for para asignar key(en la llave) y Value(en el valor) in(en) el diccionario(Buying_Data) y obtenemos la clave y valor con el metodo.items()
        BillAmount += Get_Price(Key,Value) #Usamos +=(para sumar) Get_Price() que devuelve el monto del subtotal por lo tanto lo almacenamos en la variable BillAmount. Se repite el proceso para todos los productos y agrega el subtotal de cada producto para obtener el monto final
    BillAmount = Get_Discount(BillAmount,Membership) #Con los datos almacenados en BillAmount llamamos Get_Discount para pasar el monto total de la factura que hemos calculado(BillAmount) y la membresia(Memebership) que hemos optenido como argumento de la función Make_Bill(), seguido a elllo devuelve el monto final de la factura con la función Get_Discount
    print("El monto del descuento es $" + str(BillAmount)) #Imprimimos: El monto del descuento es $ (BillAmount)
Buying_Data = Enter_Products() ##def(definimos) una función que llevara por nombre: Enter_Products() la cual pone el programa en acción y aceptará los detalles del producto como un dicionario y los almacenará en la variable Buying_Data
Membership = input("Enter customer membership: ")
Make_Bill(Buying_Data, Membership)