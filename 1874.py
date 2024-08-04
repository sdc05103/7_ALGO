import sys

input = sys.stdin.readline

n = int(input())
stack = []
result = []
point = 1
flag = True

for _ in range(n):
    num = int(input())
    while point <= num:
        stack.append(point)
        result.append('+')
        point += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if flag == True:
    for i in range(len(result)):
        print(result[i])
else:
    print("NO")

