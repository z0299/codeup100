#2021.01.12 Code-Up 100제

a, d, n = input().split()

a = int(a) #시작 값
d = int(d) #등차의 값
n = int(n) #몇 번째 수인지
c = 1

while(c != n):
    a += d
    c += 1
print(a)