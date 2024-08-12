import sys
input = sys.stdin.readline

N = int(input())

star = [[' ']*2*N for _ in range(N)]

def recursion(i, j, size):
  if size == 3: # 쪼갤 수 있는 가장 최소의 단위 
        star[i][j] = '*'            
        star[i + 1][j - 1] = '*'    
        star[i + 1][j + 1] = '*'    
        star[i + 2][j - 2] = '*'    
        star[i + 2][j - 1] = '*'    
        star[i + 2][j] = '*'        
        star[i + 2][j + 1] = '*'    
        star[i + 2][j + 2] = '*'   
  else:
    newSize = size//2
    recursion(i, j, newSize)
    recursion(i+newSize, j-newSize, newSize)  # 왼쪽 삼각형
    recursion(i+newSize, j+newSize, newSize)  # 오른쪽 삼각형

recursion(0, N-1, N)  # 초기 값 N=6이면 (0, 5, 6)

for s in star:
   print("".join(s))