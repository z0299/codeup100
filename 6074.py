#2021.01.08 Code-Up 100제
"""
from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

c = input()

for i in alphabet_list:
    if i <= c:
        print(i, end = ' ')
    else:
        break
"""
c = input()

a = ord('a')
c = ord(c)

while(a <= c):
    print(chr(a), end = ' ')
    a += 1