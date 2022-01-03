n, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(n)]
sushis += sushis

num_sushi = [0 for _ in range(d+1)]

# Initialize
num_sushi[c] = 1
for i in range(k):
    x = sushis[i]
    num_sushi[x] += 1

start, end = 0, k
maximum = 0
while end < 2*n:
    var = d - num_sushi.count(0)+1
    if maximum < var:
        maximum = var

    a, b = sushis[start], sushis[end]
    if a != b:
        num_sushi[a] -= 1
        num_sushi[b] += 1
    
    start += 1
    end += 1

print(maximum)
