import sys
input = sys.stdin.readline

a = list(input().rstrip('\n'))

stack = []
sum = 0
cur = 1

for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
        cur*=2
    elif a[i] == '[':
        stack.append(a[i])
        cur*=3
    elif a[i] == ')':
        if len(stack) == 0 or stack[-1] == '[':
            sum = 0
            break
        if a[i-1] == '(':
            sum += cur
        stack.pop()
        cur //= 2
    elif a[i] == ']':
        if len(stack) == 0 or stack[-1] == '(':
            sum = 0
            break
        if a[i-1] == '[':
            sum += cur
        stack.pop()
        cur //= 3

if len(stack) != 0:
    print(0)
else:
    print(sum)
    