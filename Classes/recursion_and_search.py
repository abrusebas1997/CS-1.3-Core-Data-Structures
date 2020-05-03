#using stacks is a really good way to understand the recursion

def factorial(n):
    if n == 1:
        return 1 #base case
    else:
        f = factorial(n-1) #recursive case
        return n*f

print(factorial(3))
