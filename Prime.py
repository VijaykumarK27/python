# wap to find whether 'n' is prime or not

n = int(input())

count = 0
i = 1
while i<=n:
     if n%i == 0:
         count += 1
     i+=1
         
print(count == 2)