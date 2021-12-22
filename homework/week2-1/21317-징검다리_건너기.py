n = int(input())
energies = [tuple(map(int, input().split())) for _ in range(n-1)]
k = int(input())

min_energy = list()
huge_jump = [False for _ in range(n-1)]

# jb:just_before, bo:before_one, bt:before_two
for i in range(n-1):
    jb, bo, bt = 9999999, 9999999, 9999999
    if i == 0:
        jb = energies[i][0]
    else:
        jb = min_energy[i-1]+energies[i][0]
        if i == 1:
            bo = energies[i-1][1]
        else:
            bo = min_energy[i-2]+energies[i-1][1]
            if i == 2:
                bt = k
            elif not huge_jump[i-3]:
                bt = min_energy[i-3]+k
    me = min(jb, bo, bt)
    min_energy.append(me)
    if i>1:
        if me == jb and not huge_jump[i-1]:
            continue
        elif me == bo and not huge_jump[i-2]:
            continue
        else:
            huge_jump[i] = True
print(min_energy[-1])
