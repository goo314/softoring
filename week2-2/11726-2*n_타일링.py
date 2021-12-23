n = int(input())

fibos = [0, 1, 2]
for i in range(3, n+1):
    fibos.append(fibos[i-1]+fibos[i-2])

print(fibos[n]%10007)
