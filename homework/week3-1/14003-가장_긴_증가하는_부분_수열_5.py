n = int(input())
seq = list(map(int, input().split()))

prev = list()
arr = list()

for a in seq:
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > a:
            high = mid-1
        elif arr[mid] == a:
            low = mid
            break
        else:
            low = mid+1

    if low == len(arr):
        arr.append(a)
    else:
        arr[low] = a
    prev.append(low+1)

reverse_LIS = list()
length = len(arr)
print(length)

for i in range(len(prev)-1, -1, -1):
    if prev[i] == length:
        length -= 1
        reverse_LIS.append(seq[i])

for a in reverse_LIS[::-1]:
    print(a, end = ' ')
print()
