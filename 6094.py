#2021.01.15 Code-Up 100제

n = int(input())
nums = list(map(int,input().split()))
min = nums[0]

for i in nums:
    if (min > i):
        min = i
    else:
        continue
        
print(min)