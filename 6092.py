#2021.01.12 Code-Up 100제

n = int(input())
nums = list(map(int,input().split()))
d = []

for i in range(23):
    d.append(0)

for i in nums:
    d[i-1] += 1

for i in d:
    print(i, end = " ")