#2021.01.07 Code-Up 100제
n = input().split()
n[0] = int(n[0])
n[1] = int(n[1])
n[2] = int(n[2])

for i in n:
    if(i % 2 == 0):
        print("even")
    else:
        print("odd")