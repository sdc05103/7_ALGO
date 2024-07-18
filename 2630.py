import sys

input = sys.stdin.readline

N = int(input())

arr = []

for i in range(N):
  arr.append(list(map(int, input().split())))

blue = 0
white = 0

def cut(x,y,n):
  global blue
  global white

