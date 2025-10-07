A class is a blueprint for creating new objects. A object is an instance of a class. For example a class named Human and the objects is the humans themselves like John and Henry.
Defining a class, first letter of every word is uppercase and no underscore. Every function you define should have atleast one parameter. 
class Point:
    def draw(self):
        print("Draw")
You can call the Point class like a function: point = Point()

Self is a refrence to the current object. A constructor is a special method in a class that runs automatically every time you make a new object. 
def __init__(self, x, y):
    self.x = x # means that we set the value from the parameter x into the object x-variable. 
    self.y = y

Instance attributes are uniqe to each Object. Class level attributes is shared among all objects. 

This is a class method and the first parameter is always cls. They can be used witout making an object and can for example count the number of objects in a class.
@classmethod # this is a decorator
def zero(cls):
    return cls(0, 0)

Search magic methods python 3 to get the different ones. __init__ and __str__ is an example. With __str__ you define yourself how an object will be printed out. Methods like __eq__ __gt__ and many others are for comparing. 
def __gt__(self, other);
    return self.x == other.x and self.y == other.y

We use custom cointainers so we can have more control on how a list or set behaves. We can preifx attributes and make them private by __ before an attribute. More like warning to others not to touch, is it not security based. To supress accidents.  
def __init__(self):
    self.data = []
def __len__(self):
    return len(self.data)    


