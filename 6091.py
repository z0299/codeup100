#2021.01.12 Code-Up 100제

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

#최소공배수 구하는 소스
for i in range(max(a,b,c), a*b*c+1):
    if i%a == 0 and i%b == 0 and i%c == 0:
        print(i)
        break
    else:
        continue