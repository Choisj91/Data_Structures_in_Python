def factorial(n):
    fac = 1
    for index in range(2, n + 1):
        fac = fac * index
    return fac

print(factorial(3))