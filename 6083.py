#2021.01.12 Code-Up 100제

red, green, blue = input().split()
red = int(red)
green = int(green)
blue = int(blue)
count = 0

for r in range(red):
    for g in range(green):
        for b in range(blue):
            print(r,g,b)
            count += 1
print(count)