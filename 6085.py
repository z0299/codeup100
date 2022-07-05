#2021.01.12 Code-Up 100제

w, h, b = input().split()
w = int(w) #이미지 가로 해상도
h = int(h) #이미지 세로 해상도
b = int(b) #한 픽셀을 저장하기 위한 비트

#이미지를 압축하지 않고 그대로 저장하는 .bmp파일 용량 구하기
bmp = (w * h * b)/8/1024/1024
print(f'{bmp:.2f} MB')