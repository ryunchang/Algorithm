
def factorial(i):

    if i == 1:
        return 1 

    return i * factorial(i-1)
    

print(factorial(5))