"""
Mode	Description
r	    Opens a file for reading. (default)
w	    Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	    Opens a file for exclusive creation. If the file already exists, the operation fails.
a	    Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	    Opens in text mode. (default)
b	    Opens in binary mode.
+	    Opens a file for updating (reading and writing)
"""

f = open("test.txt", 'a')

# f.write('In this Python Tutorial for Beginners video I am going to show you \nHow to Create a Text File and Write
# in It Using Python .') f.close()

try:
    for i in range(10):
        f.write("this is line no %d\n" % (i+1))
finally:
    f.close()

f = open('test.txt')
print(f.readline())
f.close()