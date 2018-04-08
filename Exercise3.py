# Orla Higgins, 2018-02-27
# Collatz Conjecture
# (Script that starts with an integer and repeatedly applies the Collatz function using a while loop and if statement)

# ask the user for the integer instead of specifying a value of 17
# (returns error when number is not an integer)
n = int(input("Please enter an integer: "))

# n is a positive number greater than 1 as 1 will produce infinite loop
while n > 1 :
    # if statement for n if it is divisible by 2/even number, divide n by 2
  if n % 2 == 0 :
      n = n / 2
    # otherwise/for odd numbers apply (multiply by three and 1)
  else:
      n = 3 * n + 1

  print (n)
