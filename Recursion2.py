# Recursion in Python

# Prepare one recursive function which counts the number from 10 to 0

def group(n):
    if n < 0:
        print("Done!")
    else:
        print(n)
        group(n -1)

group(10)


# Factorial

def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(1))
print(fact(10))

# Calculate sum of elements in a list

def listt(my_list):
    if len(my_list) == 0:
        return 0
    else:
        return my_list[0] + listt(my_list[1:])

abc = [10,20,30,40,50]

print(listt(abc))


# Recursive limit

import sys
print(sys.getrecursionlimit())






















