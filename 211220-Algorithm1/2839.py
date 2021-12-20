n = int(input())

ret = 0

while n != 0:
    if n % 5 == 0:
        ret += n//5
        n %= 5

    elif n < 3:
        ret = -1
        break

    else:
        ret += 1
        n -= 3

print(ret)
