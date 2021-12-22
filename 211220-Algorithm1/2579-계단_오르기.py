# Dynamic Programming
'''
Dynamic programming is...
simplifying a complicated problem
by breaking it down into simpler sub-problems in recursive manner

ex)
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else return fibo(n-1) + fibo(n-2)

-> store in list

fibos = [1, 1]
def fibo(n):
    if n not in fibos:
        fibos.append(fibos[n-1]+fibos[n-2])
    return fibos[n]
'''
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
