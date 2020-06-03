#Project Euler
#Even Fibonacci


prev_first = 1
prev_next = 2
fibo_sum = 2
arr = []

while True:
    next = prev_first+prev_next
    #limit in problem is 4,000,000
    if next >= 4000000:
        break
    if next % 2 == 0:
        fibo_sum += next
    arr.append(next)
    prev_first = prev_next
    prev_next = next

print(fibo_sum)
#4613732