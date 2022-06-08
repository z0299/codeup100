#2021.01.09 Code-Up 100제
n = int(input())
sum = 0

for i in range(1, n+1):
    if(i % 2 == 0):
        sum += i
        
print(sum)