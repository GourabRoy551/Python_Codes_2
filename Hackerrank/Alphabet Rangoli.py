def print_rangoli(size):
    # your code goes here
    w = (size -1) * 2 +((size * 2) - 1)

    # First half
    for i in range(1, n, 1):
        num_of_letter = (i*2) - 1
        s = ''

        letter_value = 97+n-1

        for i in range(0, num_of_letter):
            if i != 0:
                s += '-'
            s += chr(letter_value)
            if i < (num_of_letter - 1) / 2:
                letter_value = letter_value-1
            else:
                letter_value = letter_value + 1

        print(s.center(w, '-'))

    # Last half
    for i in range(n, 0, -1):
        num_of_letter = (i*2) - 1
        s = ''
        letter_value = 97+n-1
        for i in range(0, num_of_letter):
            if i != 0:
                s += '-'
            s += chr(letter_value)
            if i < (num_of_letter - 1) / 2:
                letter_value = letter_value - 1
            else:
                letter_value = letter_value + 1
        print(s.center(w, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)