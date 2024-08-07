"""
flag = True가 되어도 계속 실행되어 시간 초과 발생 

"""

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

cnt = 0
flag = False
S = 2 ** N

def z(x,y,S):
    global cnt, flag

    if S == 1:  
        if x == c and y == r:
            flag = True 
            return
        cnt += 1
        return
    
    
    if flag == False:
        z(x,y,S//2)
        z(x+S//2,y,S//2)
        z(x,y+S//2,S//2)
        z(x+S//2,y+S//2,S//2)

z(0,0,S)

print(cnt)