n, k = map(int, input().split())
listA = [int(input()) for i in range(n)]

ret = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    ret += k//listA[i]
    k %= listA[i]

print(ret)
