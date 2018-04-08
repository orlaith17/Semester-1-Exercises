# Orla Higgins, 2018-04-08
# Project Eulor Problem 5
# smallest positive number divisible all numbers from 1 to 20
# http://code.jasonbhill.com/python/project-euler-problem-5/
 
# I removed the time code in the above reference

# function to factor a given positive integer n
def factors(n):
    factors = []
    # remove any factors of 2 first
    while n % 2 == 0:
        factors.append(2)
        n = n/2
    # now look for odd factors
    p = 3
    while n != 1:
        while n % p == 0:
            factors.append(p)
            n = n/p
        p = p + 2
    return factors
 
# merge two lists of factors based on maximum multiplicities
def factor_append(factors,new):
    if len(factors) == 0: return new
    for i in range(len(new)):
        if i > 0 and new[i] == new[i-1]: continue
        new_count = new.count(new[i])
        old_count = factors.count(new[i])
        if new_count > old_count:
            for j in range(new_count - old_count): factors.append(new[i])
    factors.sort()
    return factors
 
# find the smallest positive evenly divisible number for a positive integer n
def smallest_evenly_divisible(num):
    F = []
    for i in range(1,num + 1):
        F = factor_append(F,factors(i))
    product = 1
    for i in F: product *= i
    return product
 

product = smallest_evenly_divisible(20)

 
print(product)