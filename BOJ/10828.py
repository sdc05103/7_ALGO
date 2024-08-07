import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    order = input().split()
    a = order[0]
    if a == 'push':
        stack.append(int(order[1]))
    elif a == 'size':
        print(len(stack))
    elif a == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif a == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif a == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    

