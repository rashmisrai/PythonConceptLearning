# Iterators in Python

'''
iter(iterable) creates an iterator.
next(iterator) retrieves the next item.
When no items remain, StopIteration is raised.
for loops use iterators automatically.
Custom iterators are created by implementing __iter__() and __next__().
'''
'''
fruits = ["Apple","Mango","Banana"]
print(fruits)

basket = iter(fruits) # iter() is present for iterable objects
# print(basket)

print(next(basket)) # next() is present for iterated objects
print(next(basket))
print(next(basket))


name = "Rashmi"
spell = iter(name)

print(next(spell))
print(next(spell))
print(next(spell))
print(next(spell))
print(next(spell))
print(next(spell))


# Using for loop through iterable object
country = ("India", "Russia", "Israel", "USA", "Antartica")
print(country)

for x in country:
    print(x)

for x in name:
    print(x)

'''

# Creating an iterator object
#Step1: Create a class

class Numbers:

    def __init__(self): #Initialize
        self.num = 1
    
    def __iter__(self): #Iterate
        return self

    def __next__(self):
        if self.num <=10:
            x = self.num
            self.num +=1
            return x
        else:
            raise StopIteration

number = Numbers()
for i in number:
    print(i)
    













