'''
Question 1 (Easy) - Every Third Character

Given a string, print:

all characters at indices divisible by 3
all remaining characters

Example
Input: PythonProgramming

Output: PhPoig ytnrgrammn
'''

Input = str(input())

Divisible  = ""
NonDivisible = ""
for i in range(len(Input)):
    if i %3 == 0:
        Divisible += Input[i]
    else:
        NonDivisible += Input[i]

print(Divisible, NonDivisible)
    
'''
Question 2 - Vowels and Consonants

Given a string, separate vowels and consonants while maintaining their order.

Input
Education
Output
Euaio dctn
'''
S = str(input())

Vowels = ""
Consonants = " "
for character in S:
    if character in "aeiouAEIOU":
        Vowels += character
    else:
        Consonants += character

print(Vowels, Consonants)


















