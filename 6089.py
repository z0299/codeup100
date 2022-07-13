#2021.01.12 Code-Up 100제

a, r, n = input().split()

a = int(a) #시작 값
r = int(r) #등비
n = int(n) #몇 번째인지
c = 1

while(c != n):
    a *= r
    c += 1
    
print(a)