a, b, v = map(int, input().split())

s = 0

if (v-a)%(a-b) != 0:
    s += 1

s += (v-a)//(a-b) + 1

print(s)
