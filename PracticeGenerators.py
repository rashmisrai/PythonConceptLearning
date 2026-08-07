# Practice Generators

# Question 1: Without using a class, write a generator that prints: 1,2,3,4,5

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

num = numbers()
for i in num:
    print(i)
