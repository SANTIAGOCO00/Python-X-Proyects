#Declaraciones Condicionales: if, if-else, if-elif-else, if-else anidada
age = int (input("Enter your age:"))
if age >= 18 :
    print ("Congratulations!, you are eligible to vote")
else:
    print ("Sorry, you are not eligible to vote.")

#Elif
marks = int (input("Enter your marks: "))
if marks >= 90: 
    print ("Grade - Excellent")
elif marks < 90 and marks >= 75:
    print ("Grade - First Class")
elif marks < 75 and marks >= 40:
    print ("Grade - Average")
else:
    print ("Grade - Frail")

#Anidadas
username = input ("Enter your username: ")
password = input ("Enter your password: ")
if username == "john":
    if password == "12345":
        print ("Login Successful")
    else: 
        print ("Incorrect Password")
else:
    print ("Incorrect Username")

#Repaso, Ej: Semaforo
light = input ("Which color is the ligh indicating? (red, yellow, green): ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Caution")
elif light == "green":
    print("Go")
else:
    print("Invalid color")

#Repaso2, Ej: El numero mayor gana
userOne = int (input ("user One, choose a number: "))
UserTwo = int (input ("user Two, choose a number: "))
UserThree = int (input ("user Three, choose a number: "))
if (userOne > UserTwo) and (userOne > UserThree):
    print ("User One is the winner")
elif (UserTwo > userOne) and (UserTwo > UserThree):
    print ("User Two is the winner")
else:
    print ("User Three is the winner")

