n = int(input())
sum = 0
i = 1
while i<n:
    if n%i==0:
        sum += i
        i += 1
        print(sum ==n)