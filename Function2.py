# Function in python -2

# Python *args (Positional arguments) and **kwargs (keyword arguments)

# Arbitrary Arguments - *args (class 'Tuple')
'''
def food(*args):
    print(f"{args} are available in market")

food("Apple","Mango") # This value will return in tuple, bcz inside a function is actually a tuple

def studentDetails(*args):
    print("Type: ", type(args))

studentDetails(1)

# Addition function
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,4,5))
print(add(34,56,78,97))
    
# Substraction function
def subtract(*numbers):
    sub = numbers[0]
    for n in numbers[1:]: # loop through remaining numbers
        sub -= n
    return sub

print(subtract(10,5,1))

# Find the maximum value

def max(*numbers):
    if len(numbers) == 0:
        return "Invalid number"
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


print(max(4,6,7,3))
print(max())

def names(*name):
    return name


print(names(1,23))
print(type(names("Rashmi", "Rahul")))
'''
'''           
# Arbitrary Keyword arguments
def fruits(**fruits):
    return fruits


print(fruits(fruit1 = "Apple",fruit2 = "Mango")) # This will print the value in dictionary


def DomesticAndWild(**animals):
    print("These are the list of Domestic and Wild animals that we have")
    for key,value in animals.items():
        print(" ", key + ":" + " ", value)

DomesticAndWild(Wild = "Lion", Domestic = "Cat")
        
    
def studentDetails(Username, **details):
    print("StudentName: ",Username)
    print("Here are the details of the present Student : ")
    for key, value in details.items():
        print(" ", key + ":" + " ", value)

studentDetails(Username = "Rashmi", age = 23, Class = 10, Height = 177, Weight = 57, Subject = "Computer Science")


# If you have a list and you want to add them, then we can unpack it using *args

def myFunc(a,b,c):
    return a + b + c

listn = [2,3,4]
result = myFunc(*listn) # unpacking the list
print(result)


# If you have a dict and you want to use them, then we can unpack it using **kwargs

def name(fname, lname):
    print(fname + " " + lname)

myData = {
    "fname": "Rashmi",
    "lname" : "Rai"
    }

name(**myData)

'''

# Python scope

#1. Local Variable scope
def a():
    x = 300 # local variable
    print(x)

a()


# Rule1 :  A local variable declared inside the func is not available outside the func, but can be accessed from function inside the func (Nested func)
def a():
    x = 300 # local variable
    def newA():
        print(x)

a()


#2. Global variable scope - A variable created outside of a function is global and can be used by anyone:

y = 20 # global variable

def num():
    print(y)

num()

# Same variable name

name = "Rashmi" # global variable

def Uname():
    name = "Baby" #local variable
    print(name)

print(name)
Uname()

# Global keyword

#1. When u want to create a global variable, inside a local scope (use this keyword: global)

def age():
    global x
    x= 23
    print(x)

age()
print(x)


#2. When a variable is already created as global variable, and if u want to change the value of it, use global keyword

name = "Rashmi"
print(name)

def person():
    global name
    name = "Baby"
    print(name)
person()
print(name)


# Nonlocal keyword - The nonlocal keyword is used to work with variables inside nested functions. The nonlocal keyword makes the variable belong to the outer function.

def game():
    score = 0

    def collect_coins():
        nonlocal score
        score +=10
        print("Current Score: ", score)

    collect_coins()
    collect_coins()
    collect_coins()
    collect_coins()
    collect_coins()

game()

# LEGB rule
'''
Memory Trick 🌟

Think of LEGB as four boxes:

┌────────────────────┐
│ Local              │ ← Current function
├────────────────────┤
│ Enclosing          │ ← Outer function
├────────────────────┤
│ Global             │ ← Outside all functions
├────────────────────┤
│ Built-in           │ ← Python's own functions


'''
































