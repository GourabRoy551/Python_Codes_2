# Get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference

n = int(input("Enter a number: "))


def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


print(difference(n))
