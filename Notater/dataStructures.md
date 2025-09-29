Lists: Is made by []. A matrix is a list inside a list. You can combine 2 lists easly with +. We have a list function list(). For example list(range(20)), this gives the numbers from 0-19. print(numbers[::2]) will hop to every other element. To unpack a list you can: first, second, third = numbers. If the list you want to unpack has many element but you only care about the first two you can: first, second, *other = numbers.
If you want the index of the item when looping over list you need to use the "enumerate". This will return a tuple and you must unpack it. for index, letter in enumerate(letters):

Everthing in python is a object so everthing got methods. If you define a list "letters" this will for example have the .append method which is used to add elements. .insert is more spesific, you must write the index you want to add. You can remove items by pop, remove methods or used the del function. Pop removes an index, remove removes a value. The del statement can remove a range of items. Clear method removes everthing. 

You can use a if "d" in letters: to find it occurance. Count method will give us the number of occurances. 

.sort method will sort the list, it will modify it. The sorted() built in function will give you a new lists.

Lambda functions: (key=lambda parameters:expression). We use lambda function when you are only gonna use it once as an argument to an other function. 

The map function is where we want to apply a function to each element in a list, for example to double it. For example if we got a list of numbers we can result = map(lambda x: x * 2, numbers). It returns a map function so we need to convert it into a list. Then print if with print(list(result)). Alternative: [item[1] for item in items]

The filter function is where we want to pick at the elements in a list based on a condition. It returns a filter object which needs to be converted to a list object. Same syntax only you switch "map" with "filter. Alternative: [item for item in items if item[1] >= 10]

The Zip function takes in one or more iterable. Can cast it with list().

0, "", [] is considired Falsy values. Stacks = LIFO. Typically undo-functions. 

from collections import deque. Queues = FIFO. queue = deque([]). Messagesystems. 

Tuples = ReadOnlyLists. Can not be changed. Cordinates. syntax (). tuple() is a function

from array import array. numbers = array("i", [1, 2, 3]). Just use if you deal with a large number og numbers. 

numbers = [1, 1, 2, 3]. uniqes = set(numbers). The set functions removes duplicates. A union of sets syntax is used by the pipe |. This includes the uniques from both sets. the syntax & prints the values that is in both. The syntax - shows what is in the first set and not the second. The syntax ^ shows the values that is in the sets but not both. Sets does not supports indexing. Unordered sets of uniqe collections. set() is a function. syntax s = {1,2,3,4}

Dictionaries is collections of keyvalue pairs. for example a name to contact information, brukernavn + passord. The key is often a String or an integer. The value can be anything. dict() is a function. Does not support indexing. point = dict("x" = 1, "y" = 2). You can use the .get method to check if a key exists. You can use the .items method to iterate over a dictionary and make it a tuple. 
Comprehensions: we can use this on lists, sets and dictionaries. syntax d = {"user_name": "Stian", "age": 13}. Both dictionaries and sets are unordered collections and cant be sorted. You must convert to a tuple, then convert to a list to do so. 
You can use the unpack operator * before a value/argument. 



