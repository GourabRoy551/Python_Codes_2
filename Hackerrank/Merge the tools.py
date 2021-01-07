def merge_the_tools(string, k):
    # your code goes here
    while string:
        s = string[0:k]
        x = ''

        for i in s:
            if i not in x:
                x += i
        print(x)
        string = string[k:]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)