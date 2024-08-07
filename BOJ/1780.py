import sys

input = sys.stdin.readline

N = int(input())

arr = []

negative = 0
zero = 0 
positive = 0

for _ in range(N):
    arr.append(list(map(int, input().split())))
    
def cut(x,y,n):
    global negative, zero, positive

    k = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if k != arr[i][j]:
                cut(x, y, n//3)
                cut(x, y + n//3, n//3)
                cut(x, y + 2 * n//3, n//3)
                cut(x + n//3, y, n//3)
                cut(x + n//3, y + n//3, n//3)
                cut(x + n//3, y + 2 * n//3, n//3)
                cut(x + 2 * n//3, y, n//3)
                cut(x + 2 * n//3, y + n//3, n//3)
                cut(x + 2 * n//3, y + 2 * n//3, n//3)
                return
    
    if k == -1:
        negative += 1
    elif k == 0:
        zero += 1
    else:
        positive += 1

cut(0,0,N)

print(negative)
print(zero)
print(positive)





