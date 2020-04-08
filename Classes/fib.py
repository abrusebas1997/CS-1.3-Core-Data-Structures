#f(n) = f(n-1) + f(n-2)
# n is the mth fib nimber in the fib sequence
# 0, 1

def fib(n):
    # base case
    if n == 1:
        return 0
    if n == 2:
        return 1
    #recursive case
    else:
        return fib(n-1) + fib(n-2)

print(fib(13))
