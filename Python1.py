import math

input(("Welcome to Ashkan's Calculator\n for further information please press enter"))
input(("Here you can have - + / * sin cos \n please press enter to start"))
a = float(input("enter number:"))
opt = input("inset operator")
c = input("Do you need more numbers?")
if c == "yes":
    b = float(input("enter number:"))
else:
    print("Ok now we start")
if opt == "+":
    result = a + b       


if opt == "*":
    result = a * b       


if opt == "-":
    result = a - b     


if opt == "/":
    if b != 0:
        result = a/b
    else:    
        result = "ERROR" 

if opt == "sin":
    result = math.sin(a)

if opt == "cos":
    result = math.cos(a)

print(result)
