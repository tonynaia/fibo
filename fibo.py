#Run in Python3

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end='\n')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
