'''
factorials = [1]
def factorial(n):
    if n >= len(factorials):
        factorials.append(n*factorial(n-1))
    return factorials[n]
'''

import math

n = int(input())

ret = 0
for i in range(n//2+1):
    p = i # nums of 2
    q = n-2*i # nums of 1
    ret += math.factorial(p+q)//(math.factorial(p)*math.factorial(q))
    # ret += int(factorial(p+q)/(factorial(p)*factorial(q)))
print(ret % 10007)
