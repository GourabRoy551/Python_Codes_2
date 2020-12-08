def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

# Output : Factorial of 5 is  120
print("Factorial of 5 is ", fact(5))