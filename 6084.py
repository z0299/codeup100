#2021.01.12 Code-Up 100제

h,b,c,s = input().split()

h = int(h) #헤르쯔; 1초에 몇번 체크하는지
b = int(b) #비트수; 몇가지 비트수를 사용할 건지
c = int(c) #채널수; 모노는1개, 스테레오는 2개
s = int(s) #녹음시간; (초)

#PCM(Pulse Code Modulation)방식
pcm = (h * b * c * s)/8/1024/1024
print(f'{pcm:.1f} MB')