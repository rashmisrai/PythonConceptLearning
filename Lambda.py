# Lambda function in python
# Syntax: lambda arguments: expression
'''
lambda
   │
   ├── parameters
   │
   └── expression
   '''

var = lambda a,b : a + b
print(var(2,3))

a = str(input("Enter your first name: "))
b = str(input("Enter your last name: "))
name = lambda fname,lname: fname+ " " + lname
print(name(a,b))
print(type(name))

#Default arguments

state = lambda name="Rashmi": "Hello" +" " + name
print(state())

# If else statement in lambda -  somewhat similar like list comprehension

check = lambda age: "Adult" if age>=18 else "Child"
print(check(45))
print(check(12))

# Lambda as a function argument

def calculate(a,b,operation):
    return operation(a,b)

print(calculate(5,6, lambda x,y: x + y))
print(calculate(5,6, lambda x,y: x - y))

# Lambda with built in functions

# 1. Lambda with map() - The map() function applies a function to every item in an iterable:

score = [12,45,32,67,21,11,46]
result = list(map(lambda x: x*2, score))
print(result)


words = ["runn", "sleep", "walk", "bath", "jump", "eat"]
verb = list(map(lambda x: x+ "ing",words))
print(verb)


# 2. Lambda with filter() - The filter() function creates a list of items for which a function returns True

num = [1,2,3,4,5,6,7,8,9]
result = list(filter(lambda x: x%2 == 0, num))
print(result)


# 3. Lambda with sorted() - The sorted() function can use a lambda as a key for custom sorting:

data = [("Rashmi", 23), ("Bunny",24),("Kavya",12)]
data.sort(key = lambda x: x[1])
print(data)


words = ["apple", "pie", "banana", "cherry"]
result = sorted(words, key = lambda x: len(x))
print(result)
 

# 4. Lambda with reduce() - reduce() takes a collection (like a list) and reduces it to a single value by repeatedly applying a function.

from functools import reduce
num = [1,2,3,4,5]
result = reduce(lambda x,y : x+y, num)
print(result)








