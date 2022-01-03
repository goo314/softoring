n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
pos = [list(map(int, input().split())) for _ in range(k)]

sum_array = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        sum_array[i][j] = sum_array[i-1][j] + sum_array[i][j-1] - sum_array[i-1][j-1]
        sum_array[i][j] += array[i-1][j-1]

ret = 0
for i in range(k):
    i, j, x, y = pos[i][0], pos[i][1], pos[i][2], pos[i][3]
    ret = sum_array[x][y]
    ret -= sum_array[x][j-1] + sum_array[i-1][y]
    ret += sum_array[i-1][j-1]
    print(ret)
