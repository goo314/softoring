# Dynamic Programming
n = int(input())
stairs = [int(input()) for _ in range(n)]

possible_next = list()
impossible_next = list()
max_value = list()


for i in range(n):
    if i == 0:
        possible = stairs[i]
        impossible = stairs[i]
    else:
        if i == 1:
            possible = stairs[i]
        else:            
            possible = max_value[i-2]+stairs[i]
        impossible = possible_next[i-1]+stairs[i]
    possible_next.append(possible)
    impossible_next.append(impossible)
    max_value.append(max(possible, impossible))

print(max_value[-1])
