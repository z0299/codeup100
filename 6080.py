#2021.01.09 Code-Up 100제
n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)

d1 = range(1,n1+1)
d2 = range(1,n2+1)

for i1 in d1:
    for i2 in d2:
        print(i1, i2)