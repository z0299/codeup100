#2021.01.12 Code-Up 100제

n = int(input())

for i in range(1,n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
    #if '3' or '6' or '9' in str(i)는 문자가 str(i)에 있는지 판별(boolean)과 같은 의미이다
    #따라서 or문을 쓸 땐 각각에 대하여 써 주어야 한다.
    #or 연산자는 비교연산자가 아니고 bool타입 연산자이다.
        print("X", end = " ")
    else:
        print(i, end = " ")            