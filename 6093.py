#2021.01.12 Code-Up 100제

n = int(input())
nums = list(map(int,input().split()))

#list 뒤에서부터 출력하기
for i in reversed(nums):
    print(i, end = " ")