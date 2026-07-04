# Python Decorators

# A decorator is a special Python function that adds extra work or extra behavior to another function without changing its original code.
# A decorator is like a helper that wraps around a function and gives it new powers.

name = str(input("Enter your name user: "))
def GreetingScreen(func):
    def greet(*args):
        print(f"Welcome to the ATM: {name}")
        func(*args)
        print("Thank you for banking with us")
    return greet


B = 5000

while True:
        try:
            A = int(input("Please enter the money to be withdraw: "))
            break
        except ValueError:
            print("Please enter the amount in numbers")
            
@GreetingScreen            
def withdraw(amount, balance_amount):
    
    if balance_amount>= amount:
        print("Yes, you can procced for money transaction")
        while True:
            try:
                C = int(input("Please enter you 4 digit pin number: "))
                if 1000<=C<=9999:
                    print(f"User has successfully withdrawn Rs. {amount}")
                    break
                else:
                    print("Invalid pin number, please enter your pin number again")
            except ValueError:
                print("Please should contain numbers only")
        balance_amount -= amount
        print(f"The balance amount is: {balance_amount}")
    else:
        print("Insufficient amount in account")

withdraw(A,B)


