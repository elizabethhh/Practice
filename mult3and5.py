#Project Euler
#Multiples 3 and 5

sum = 0
for num in list(range(1, 1000)):
    if num % 3 == 0 or num % 5 == 0:
        sum += num
print(sum)

#233168