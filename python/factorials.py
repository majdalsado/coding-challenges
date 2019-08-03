# The Challenge: 
# The recursive function for this challenge should 
# return the factorial of an inputted integer. 
# factorial(4) = 4! = 4 x 3 x 2 x 1 = 24 = Output

def factorial(n):
    # The base case
    if (n==0):
        return 1
    # The recursive
    return n*factorial(n-1)
# Test case
print(factorial(20))