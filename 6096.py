#2022.04.08 Code-Up 100제

def change(coordinate, arr):
    for i in range(len(arr)):
        arr[coordinate[0]-1][i] = int(not arr[coordinate[0]-1][i])
        arr[i][coordinate[1]-1] = int(not arr[i][coordinate[1]-1])

if __name__ == "__main__":
    arr = []

    for i in range(19):
        arr.append(list(map(int, input().split())))

    n = int(input())
    coordinates = []

    for i in range(n):
        coordinates.append(list(map(int, input().split())))

    for i in range(n):
        change(coordinates[i], arr)
        
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()