import numpy as np
import pandas as pd

# Series
x = ['a', 'b', 'c', 'd', 'e']
y = [1, 2, 3, 4, 5]
# z = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

a = pd.Series(data=y, index=x)
print(a)
print(type(a))

# Dataframes
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = [9, 0, 1, 2]
D = [3, 4, 5, 6]
E = [7, 8, 9, 0]

df = pd.DataFrame([A, B, C, D, E], ['a', 'b', 'c', 'd', 'e'], ['W', 'X', 'Y', 'Z'])

print(df)

print("------------------------------------------")
df['P'] = df['Y'] + df['Z']
print(df)

A = ['👻', '😁', '❤', '💀']
B = ['👻', '😁', '❤', '💀']
C = ['👻', '😁', '❤', '💀']
D = ['👻', '😁', '❤', '💀']
E = ['👻', '😁', '❤', '💀']

df1 = pd.DataFrame([A, B, C, D, E], ['a', 'b', 'c', 'd', 'e'], ['W', 'X', 'Y', 'Z'])
print(df1)

print("------------------------------------------")
df1['P'] = df1['Y'] + df1['Z']
print(df1)

print('############################################')
df1.drop('e', inplace=True)
df1.drop('P', axis=1, inplace=True)
print(df1)

