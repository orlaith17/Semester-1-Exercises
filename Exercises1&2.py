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

# Comments on Discussions Board for Topic 1: 
# My name is Orla, so the first and last letter of my name (O + A = 15 + 1) give the number  16. The 16th Fibonacci number is 987. 

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

# Comments on Discussions Board for Topic 2: 
# My surname is Higgins
# The first letter H is number 72
# The last letter s is number 115
# Fibonacci number 187 is 538522340430300790495419781092981030533
# ord() is a built-in function of Python. Given a string representing one Unicode character, the function will return an integer representing the Unicode code point of that character in decimal form. 
