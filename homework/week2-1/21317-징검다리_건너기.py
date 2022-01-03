n = int(input())
energies = [tuple(map(int, input().split())) for _ in range(n-1)]
k = int(input())

'''
not_jump_3[n][0] = [n-1][0], [n-2][0]
jump_3[n][1] = [n-1][1], [n-2][1], [n-3][0]

'''

without_jump = [0 for _ in range(n)]
with_jump = [ 0 for _ in range(n)]

for i in range(1, n):
    if i == 1:
        without_jump[i] = energies[i-1][0]
    else:
        without_jump[i] = min(without_jump[i-1]+energies[i-1][0],
                              without_jump[i-2]+energies[i-2][1])
        if i == 2:
            with_jump[i] = k
        else:
            if with_jump[i-2] == 0:
                with_jump[i] = min(with_jump[i-1], without_jump[i-3]+k)
            elif with_jump[i-1] == 0:
                with_jump[i] = min(with_jump[i-2], without_jump[i-3]+k)
            else:
                with_jump[i] = min(with_jump[i-1], with_jump[i-2], without_jump[i-3]+k)

print( min(with_jump[-1], without_jump[-1]))
