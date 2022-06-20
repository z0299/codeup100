#2021.01.11 Code-Up 100제

c = int(input(), 16)

for i in (range(1,16)):
    print(f'{c:X}*{i:X}={c*i:X}')
    #print('%X'%c, '*%X'%i, '=%X'%(c*i), sep ='')
    #print('%X*%X=%X' %(c,i,c*i))