upper = 10

print("Prime numbers between", "and", upper, "are:")

for num in range(upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
