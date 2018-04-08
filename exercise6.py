# Orla Higgins, 2018-04-08


def factorial(x):
    n = x - 1
    while n > 0:
        x = x * n
        n -= 1
    return x

print(factorial(5))
print(factorial(7))
print(factorial(10))

