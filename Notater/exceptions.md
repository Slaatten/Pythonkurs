It is your duty as a programmer to handle exceptions. Use Try&Except cause. What type of except cause is based on the type of error. If you right a string to an integer input it is a value error. What we have in the else-cause only runs if we have noe exceptions. Try&Except&Else. 
You can add multiple except causes with (ValueError, ZeroDivisionEroor)
The function open() is a file-object. file = open("main.py")
The finally-clause will always run. You can for example but the file.close() here.
If you use the "with" method to open a file, it automatically closes when you are done. 
Python has many built-in exceptions, but you can also raise your own. But raising your own exceptions is costly. It is not recommended as best practice, but it is good to know what it is. 

# Exercise 1
while True:

    try:
        number = int(input("Write in a number: "))
    except ValueError:
        print("Invalid number. Must be an integer")
    else:
        sqaure_root = number ** 0.5
        print("Sqaure root of your number: ", sqaure_root)
        break

# Exercise 2
while True:
    try:
        number1 = int(input("Write a number: "))
        number2 = int(input("Write an another number: "))
        result = number1 / number2
    except (ZeroDivisionError, ValueError):
        print("Input must be an integer above zero")
    else:
        print(f"Your input: {number1}, {number2}")
        print("Result: ", result)
        break
    finally:
        print("Thanks for testing")

# Exercise 3
try:
    with open("data.txt") as data:
        content = data.read()
except FileNotFoundError:
    print("The file you are trying to open was not found")
else:
    print(content)    
