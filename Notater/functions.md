You define a functions with the "def" notation. For example def greet(): Be careful with indents here aswell. We have two types of functions, either performs a task or returns a value.  

Parameter is the defition of arguments in a defintion. An argument is the actual value. 

If you are calling a function with multiple arguments you should use keyword arguments. For example if the function is def increment(number, by) you can call it using increment(2, by=1). If you write by=1 in the definition of the function you set a default. Make sure the optinal parameters is after the required parameters. 

If you prefix the parameters in the defition of a function with for example def multiply(*numbers) you can put in as many arguments as you like. By prefixing it with ** you can have multiply key value arguments like (id=1, name='John', age=22)

# if the number is divisible by 3 it shall return Fizz
# if the number is divisible by 5 it shall return Buzz
# if the number is divisible by both 3 and 5 it shall return Fizzbuzz
# if the number is not divisible by either it shall return the number itself

def fizzbuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizzbuzz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"
    return input


print(fizzbuzz(15))