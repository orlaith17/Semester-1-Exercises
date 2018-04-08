# Orla Higgins, 2018-04-08
# Functions
# Script containing a function called factorial() 

# https://www.w3resource.com/python-exercises/python-functions-exercise-5.php
# https://www.codecademy.com/en/forum_questions/50fa316de2719346b0000a30

def factorial(x):
    # n is a positive integer
    n = 1
    for i in range(x):
        # loop for each item in range of value x
        # i does not have to be defined for return on n
        n = n * (i + 1)
        # calculation on the loop to reach a factorial of a value
    return n

# verify: 
print(factorial(5))
print(factorial(7))
print(factorial(10))


# ask the user for the integer instead of specifying a value or 5, 7 or 10
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))