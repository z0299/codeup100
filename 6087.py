#2021.01.12 Code-Up 100제

n = int(input())

for i in range(1, n+1):
    if(i % 3 != 0):
        print(i, end = " ")
    else:
        continue