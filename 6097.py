#2022.04.08 Code-Up 100제

def putstick(arr, stick):
    stick[2] = stick[2]-1
    stick[3] = stick[3]-1
    
    if stick[1] == 0:
        for i in range(stick[0]):
            arr[stick[2]][stick[3]+i] = 1
            
    elif stick[1] == 1:
        for i in range(stick[0]):
            arr[stick[2]+i][stick[3]] = 1

if __name__ == "__main__":
    h, w= input().split()
    h = int(h)
    w = int(w)

    arr = [[0 for j in range(w)] for i in range(h)]

    n = int(input())

    sticks = []

    for i in range(n):
        sticks.append(list(map(int, input().split())))

    for i in range(n):
        putstick(arr,sticks[i])
        
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()