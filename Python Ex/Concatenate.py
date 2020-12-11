# Write a Python program to concatenate all
# elements in a list into a string and return it.

def concatenate_list(list):
    result = ""

    for element in list:
        result += str(element)
    return result

print(concatenate_list([1, 5, 12, 2]))