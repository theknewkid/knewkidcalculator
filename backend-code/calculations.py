#Let's set up functions for the different calculations here. We'll create a float from the user's input.

hey = "Welcome to my very elementary calculator!"

print(hey)

def addition():
    '''This is a function for adding.'''
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a + b)


def subtraction():
    """This is a funciton for subtracting."""
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)


def multiply():
    '''This is a function for multiplying.'''
    a = float(input("Enter a number. "))
    b -= float(input("Enter another number. "))
    print(a * b)


def division():
    '''This is a function for multiplying.'''
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)

#This is where the user will choose either addition, subtraction, multiplication, or division.

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
