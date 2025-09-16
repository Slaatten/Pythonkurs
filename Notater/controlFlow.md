if argument > 30:   
    print("Hello")
else:
    print("Hello not")
Super important with indent with conditional statements. You can write this easier and more direct: message = "Hello" if argument > 30 else "Hello not"

We can use the and, or, not operators with conditional statements. 

for number in range(3): You can combine a for loop with an else statement. But then you have to have a break line in the for loop. The else statement only runs if the break never runs. 

When using a while-loop you must always have a way to get out of it. 
if command.lower() == "quit":
    break

ControlFlow quiz:

count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print(f"We have {count} even numbers")