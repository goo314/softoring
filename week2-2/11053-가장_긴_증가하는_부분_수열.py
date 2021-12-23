n = int(input())
seq = list(map(int, input().split()))

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

arr = [seq[0]]
for a in seq:
    idx = binary_search(arr, a)
    if idx == len(arr):
        arr.append(a)
    else:
        arr[idx] = a
print(len(arr))

'''
binary search
sorted_arr
delete small
O(nlgn)


# union find
# no6: [n-1]+1
'''
