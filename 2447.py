"""
생각을 바꿔서 딱 가운데만 *이 없다. 
그니까 (1,1)만 공백..
"""

import sys
input = sys.stdin.readline

N = int(input())

star = [[" " for _ in range(N)] for _ in range(N)]

print(star)

def recursion(x, y, size):
    if size == 1:
        star[y][x] = "*"
        return
    
    size //= 3

    recursion(x, y, size)
    recursion(x, y+size, size)
    recursion(x, y+2*size, size)

    recursion(x+size, y, size)
    recursion(x+size, y+2*size, size)

    recursion(x+2*size, y, size)
    recursion(x+2*size, y+size, size)
    recursion(x+2*size, y+2*size, size)


recursion(0,0,N)

for s in star:
    print(''.join(s))

    