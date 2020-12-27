arr = []
n = int(input())

for i in range(0, n):
    str = input()
    str_ar = str.strip().split(" ")
    cmd = str_ar[0]
    if cmd == "print":
        print(arr)
    elif cmd == "sort":
        arr.sort()
    elif cmd == "reverse":
        arr.reverse()
    elif cmd == "pop":
        arr.pop()
    elif cmd == "count":
        val = int(str_ar[1])
        arr.count(val)
    elif cmd == "index":
        val = int(str_ar[1])
        arr.index(val)
    elif cmd == "remove":
        val = int(str_ar[1])
        arr.remove(val)
    elif cmd == "append":
        val = int(str_ar[1])
        arr.append(val)
    elif cmd == "insert":
        pos = int(str_ar[1])
        val = int(str_ar[2])
        arr.insert(pos, val)
