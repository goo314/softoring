n,k = map(int, input().split())

queue = list()
queue.append(n)

depth = [0]
prev = list()

ret = 0
x = queue.pop(0)
while x != k:
    print(x)
    d = depth[-1]
    queue.append(x-1)
    depth.append(d+1)
    
    queue.append(x+1)
    depth.append(d+1)

    queue.append(2*x)
    depth.append(d+1)
    x = queue.pop(0)
