from pip._vendor.distlib.compat import raw_input

n = raw_input()
input_line = raw_input()
input_list = input_line.split()

input_list = map(int, input_list)

t = tuple(input_list)

x = hash(t)
print(x)