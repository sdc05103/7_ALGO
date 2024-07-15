import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = list(map(str, input().rstrip('\n')))
    n = int(input())
    x = input().rstrip(']\n').lstrip('[').split(',')
    for i in p:
        if i == 'R':
            y = deque(list(reversed(x)))
        if i == 'D':
            y.popleft()
    output = '[' + ','.join(map(str, y)) + ']'
    if output:
        print(output)
    elif output == '[]':
        print("error")
            