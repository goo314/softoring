n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

combine = [0, 0]
close = 2000000000

posA, posB = 0, n-1
while posA < posB:
    a, b = liquids[posA], liquids[posB]
    s = a+b
    if abs(s) < close:
        close = abs(s)
        combine[0], combine[1] = a, b

    if s < 0:
        posA += 1
    elif s > 0:
        posB -= 1
    else:
        break

print(combine[0], combine[1])
