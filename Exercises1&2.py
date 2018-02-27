# Week 1 Exercise 1
# Orla Higgins, 2018-02-20
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 16
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# Week 2 Exercise 2
# Orla Higgins, 2018-02-26
# A program that displays Fibonacci numbers using people's names.

name = "Higgins"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
