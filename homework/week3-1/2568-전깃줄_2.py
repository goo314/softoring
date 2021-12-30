n = int(input())
wires = [tuple(map(int, input().split())) for i in range(n)]

# Sort by left element
wires.sort(key=lambda x: x[0])

# LIS, Longest Increase Sequence
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
    return low

arr = list()
prev = list()
for _, end in wires:
    idx = binary_search(arr, end)
    prev.append(idx+1)
    if idx == len(arr):
        arr.append(end)
    else:
        arr[idx] = end

s = len(arr)
print(n-s)

delete_wires = list()
for i in range(len(prev)-1, -1, -1):
    if prev[i] == s:
        s -= 1
    else:
        delete_wires.append(wires[i][0])

for i in delete_wires[::-1]:
    print(i)

