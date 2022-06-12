#2021.01.09 Code-Up 100제
n = int(input())
sum = 0

for i in range(1,n):
    if(sum < n):
        sum += i
    else:
        print(i-1)
        break
    