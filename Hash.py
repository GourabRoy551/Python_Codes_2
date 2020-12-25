# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:', hash(181.23))

# hash for string
print('Hash for Python is:', hash('Python'))

# ---------------------------------------------------------

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))

# -------------------------------------------------------------
"""Example 3: hash() for Custom Objects by overriding __hash__()"""


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))


person = Person(23, 'Adam')
print(hash(person))
