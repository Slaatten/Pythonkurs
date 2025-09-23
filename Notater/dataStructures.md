Lists: Is made by []. A matrix is a list inside a list. You can combine 2 lists easly with +. We have a list function list(). For example list(range(20)), this gives the numbers from 0-19. print(numbers[::2]) will hop to every other element. To unpack a list you can: first, second, third = numbers. If the list you want to unpack has many element but you only care about the first two you can: first, second, *other = numbers.
If you want the index of the item when looping over list you need to use the "enumerate". This will return a tuple and you must unpack it. for index, letter in enumerate(letters):

Everthing in python is a object so everthing got methods. If you define a list "letters" this will for example have the .append method which is used to add elements. .insert is more spesific, you must write the index you want to add. You can remove items by pop, remove methods or used the del function. Pop removes an index, remove removes a value. The del statement can remove a range of items. Clear method removes everthing. 

You can use a if "d" in letters: to find it occurance. Count method will give us the number of occurances. 

.sort method will sort the list, it will modify it. The sorted() built in function will give you a new lists.

Lambda functions: (key=lambda parameters:expression). We use lambda function when you are only gonna use it once as an argument to an other function. 

The map function is where we want to apply a function to each element in a list, for example to double it. For example if we got a list of numbers we can result = map(lambda x: x * 2, numbers). It returns a map function so we need to convert it into a list. Then print if with print(list(result)). Alternative: [item[1] for item in items]

The filter function is where we want to pick at the elements in a list based on a condition. It returns a filter object which needs to be converted to a list object. Same syntax only you switch "map" with "filter. Alternative: [item for item in items if item[1] >= 10]