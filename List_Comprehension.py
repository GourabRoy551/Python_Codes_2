# Example 1: Iterating through a string Using for Loop

h_letters = []

for letter in 'human':
    h_letters.append(letter)
    print(h_letters)

print("Final list: ", h_letters)

# Example 2: Iterating through a string Using List Comprehension
h_letters = [letter for letter in 'Comprehension']

# Output:  ['C', 'o', 'm', 'p', 'r', 'e', 'h', 'e', 'n', 's', 'i', 'o', 'n']
print(h_letters)

# List Comprehensions vs Lamda Function
h_letters = list(map(lambda x: x, 'human'))

# Output: ['h', 'u', 'm', 'a', 'n']
print(h_letters)

# If with list comprehensions
number_list = [x for x in range(20) if x % 2 == 0]

# Output : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(number_list)

# Nested If with list comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]

# Output : [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(num_list)

# If...Else with list comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

# Transposing a matrix using list comprehension
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[row[i] for row in matrix] for i in range(2)]

# Output : [[1, 3, 5, 7], [2, 4, 6, 8]]
print(transpose)