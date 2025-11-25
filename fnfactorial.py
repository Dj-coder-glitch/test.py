#f4. Factorial using function

def fact(n):
    result = 1
    while n>0:
        result = result * n
        n = n - 1
    return result

x=int(input(print("Enter number to find factorial :", end= " ")))
print(x)
print("Factorial of", x, "is:", fact(x))