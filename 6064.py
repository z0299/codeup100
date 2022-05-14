#2021.01.07 Code-Up 100제
n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
small = n1 if (n1<n2) else n2
small = n3 if (n3<small) else small
print(small)