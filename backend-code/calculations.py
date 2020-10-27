#Let's set up functions for the different calculations here. We'll create a float from the user's input.

hey = "Welcome to my very elementary calculator!"

print(hey)

def addition():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a + b)


def subtraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)


def multiply():
    a = float(input("Enter a number. "))
    b -= float(input("Enter another number. "))
    print(a * b)


def division():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)


calc = input("Here's how this works. Type either +, -, *, or / ")

if calc == "+":
    addition()
elif calc == "-":
    subtraction()
elif calc == "*":
    multiply()
elif calc == "/":
    division()
else:
    print("The selection is invalid. Please choose again. ")
