# Calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum

x, y, z = [int(x) for x in input("Enter three value: ").split()]


def sum_thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(x, y, z))
