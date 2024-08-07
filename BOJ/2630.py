import sys

input = sys.stdin.readline

N = int(input())

arr = []

for i in range(N):
  arr.append(list(map(int, input().split())))

blue = 0
white = 0

def cut(x,y,N):
  global blue
  global white

  k = arr[x][y]

  for i in range(x, x+N):
    for j in range(y, y+N):
      if k != arr[i][j]:
        cut(x, y, N//2)
        cut(x, y+N//2, N//2)
        cut(x+N//2, y, N//2)
        cut(x+N//2, y+N//2, N//2)
        return
    
  if k == 0:
    white += 1
  else: 
    blue += 1
    
cut(0, 0, N)

print(white)
print(blue)


