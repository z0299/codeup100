#2021.01.12 Code-Up 100제

a, m, d, n = input().split()

a = int(a) #시작 값
m = int(m) #곱할 값
d = int(d) #더할 값
n = int(n) #몇 번째 수
c = 1

while(c != n):
    a *= m
    a += d
    #a = a*m+d
    c += 1
    
print(a)