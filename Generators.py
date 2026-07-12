# Generators in python

def num(n):
    for i in range(n):
        yield i

numbers = num(10)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) 
'''print(next(gen))''' # It will stop the iteration - When there are no more values to yield, the generator raises a StopIteration exception:

# Generator expressions

y = (x for x in range(5))
print(y)
print(list(y))
