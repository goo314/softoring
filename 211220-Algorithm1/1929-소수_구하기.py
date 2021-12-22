m, n = map(int, input().split())

'''
primes = list()

for i in range(2, n+1):
    check = True
    for x in primes:
        if i % x == 0:
            check = False
            break
        if x*x > i:
            break
    if check:
        primes.append(i)

primes.append(1)

for j in primes:
    if j >= m:
        print(j)
'''

# Sieve of Eratosthenes
n += 1
nums = [True]*n
for i in range(2, int(n**(1/2))+1):
    if nums[i]:
        for j in range(2*i, n, i):
            nums[j] = False

for i in range(m, n):
    if i > 1 and nums[i] == True:
        print(i)
