import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())

    q = deque(input().rstrip()[1:-1].split(','))

    cnt_r = 0
    error = False

    if (n == 0):
        q = []

    for i in p:
        if i == 'R':
            cnt_r += 1
        elif i == 'D':
            if (q):
                if (cnt_r % 2 == 1):
                    q.pop()
                
                else:
                    q.popleft()

            else:
                error = True
                break
    
    if (error == True):
        print('error')
    else:
        if (cnt_r % 2 == 1):
            q.reverse()
            print('[' + ','.join(q) + ']')
        else:
            print('[' + ','.join(q) + ']')
