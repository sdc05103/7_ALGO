import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    a = list(map(int, input().split()))

    cnt = 1

    while a:
        if a[0] >= max(a):
            if M == 0:
                break
            a.pop(0)
            cnt += 1

        else:
            a.append(a.pop(0))

        if M > 0:
            M = M-1
        else:
            M = len(a) -1

    print(cnt)
        