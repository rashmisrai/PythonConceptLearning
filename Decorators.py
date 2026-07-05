# Decorators in Python

user = str(input("Enter your name: "))


num1 = int(input("Enter the first number: " ))
num2 = int(input("Enter the second number: "))

def greet(func):
    def msg(*args):
        print(f"Welcome {user}!")
        func(*args)
        print("Activity completed successfully, Thanks for participating")

    return msg



@greet
def add(a,b):
    print(f"The sum of {a} and {b} is:",a + b)

add(num1,num2)


# Create a decorator that upper cases thevaluein function

#Multiple decorator calls
def changecase(func):
    def case(*args):
        ans = func(*args).upper()
        return ans
    return case

@changecase
def name(user):
   return f"My name is {user}"

print(name(user))
     
@changecase
def speak():
    return "Hello Everyone"


print(speak())


# Decorator With Arguments - Decorators can accept their own arguments by adding another wrapper level.

def a(role):
    def dec(func):
        def wrapper(*args):
            print(f"Welcome {role}")
            return func(*args)
        return wrapper
    return dec

@a("Admin")       
def hello(user):
    return f"Hello {user}"


print(hello(user))

# Multiple decorators on one func

@a("Guest")
@changecase
def name(user):
   return f"My name is {user}"

print(name(user))
print(name.__name__)

# Preserving Function Metadata

from functools import wraps

def a(role):
    def b(func):
        @wraps(func)
        def wrapper(*args):
            print(f"Hello {role}")
            return func(*args)
        return wrapper
    return b
    
    
@a("Admin")
def add(a,b):
    return a + b

print(add(2,3))

























