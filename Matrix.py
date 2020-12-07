A = [[1, 4, 5, 12],
     [-5, 8, 9, 0],
     [-6, 7, 11, 19]
     ]

print("A = ", A)
print("A[1] = ", A[1])
print("A[1][2] = ", A[1][2])
print("A[0][-1] = ", A[0][-1])

colum = []
for row in A:
    colum.append(row[2])

print("3rd colum  = ", colum)


# A basic code for matrix input from user

R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of colums: "))

# Initialize matrix
matrix = []
print("Enter the ebtries rowwise")

# For user input
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()