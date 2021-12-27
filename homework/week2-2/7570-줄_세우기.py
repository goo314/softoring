n = int(input())
seq = list(map(int, input().split()))

max_length = [0 for _ in range(n+1)]
for a in seq:
    max_length[a] = max_length[a-1]+1

print(n-max(max_length))
