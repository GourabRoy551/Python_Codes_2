def swap_case(s):
    arr = s
    x = arr.swapcase()
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)