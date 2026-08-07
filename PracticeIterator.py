# Practice Iterators

# Question 1: Print numbers from 1 to 5
'''
class Numbers:
    def __init__(self):
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <=5:
            x = self.count
            self.count +=1
            return x
        else:
            raise StopIteration

num = Numbers()

print(next(num))
for i in num:
    print(i)
'''

# Question 2: Print numbers from 10 to 20
'''
class Sum:
    def __init__(self):
        self.a= 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

num = Sum()

for i in num:
    print(i)

'''

# Question 3: Create an iterator that prints only even numbers from 2 to 20.
'''
class EvenNumbers:
    def __init__(self):
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 20:
            x = self.current
            self.current +=2
            return x
        else:
            raise StopIteration

number = EvenNumbers()

for i in number:
    print(i)
'''

# Question 4: Create an iterator that prints the square of numbers from 1 to 10.

class SquareOfNum:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 10:
            x = self.current*self.current
            self.current += 1
            return x
        else:
            raise StopIteration
        
Square = SquareOfNum()

for i in Square:
    print(i)
            
            
















































