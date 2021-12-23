n = int(input())
seq = list(map(int, input().split()))

nums = list(set(seq))
nums.sort()

max_length = [0 for _ in range(len(nums))]

for a in seq:
    i = nums.index(a)
    if i == 0:
        max_length[i] = 1
        continue
    tmp = max(max_length[:i])+1
    if tmp > max_length[i]:
        max_length[i] = tmp

print(max(max_length))

'''
binary search
sorted_arr
delete small
O(nlgn)


# union find
# no6: [n-1]+1
'''
