#2021.01.12 Code-Up 100제

n = int(input())
sum = 0

for i in range(1,n+1):
    if sum < n:
        sum += i
    else:
        break
print(sum)