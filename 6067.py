#2021.01.07 Code-Up 100제
n = int(input())

if(n % 2 == 0 and n < 0):
    print("A")
elif(n % 2 != 0 and n < 0):
    print("B")
elif(n % 2 == 0 and n > 0):
    print("C")
else:
    print("D")