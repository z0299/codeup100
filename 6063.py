#2021.01.07 Code-Up 100제
n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)
big = n1 if (n1>n2) else n2
print(big)