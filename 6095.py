#2021.01.15 Code-Up 100제
#코드다시복기하기!!!!!!!!!!!!!!!!**

n = int(input())
ia = []

for i in range(n):
    ia.append(list(map(int, input().split())))
    
#19*19 2차원 배열 생성
a = [[0 for col in range(19)] for row in range(19)]

for i in ia:
    a[i[0]-1][i[1]-1] = 1

for i in a:
    for j in i:
        print(j, end = " ")
    print()