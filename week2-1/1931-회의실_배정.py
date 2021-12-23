# Greedy
'''
n = int(input())
start_arr, end_arr = list(), list()
for i in range(n):
    start, end = map(int, input().split())
    start_arr.append(start)
    end_arr.append(end)

end_time = 0
count = 0
while len(start_arr) > 0:
    tmp = min(end_arr)
    if start_arr[end_arr.index(tmp)] < end_time:
        del start_arr[end_arr.index(tmp)]
        end_arr.remove(tmp)
    else:
        end_time = tmp
        count += 1

print(count)
'''

n = int(input())
meeting_time = [tuple(map(int, input().split())) for _ in range(n)]
meeting_time = sorted(meeting_time, key = lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for time in meeting_time:
    start, end = time[0], time[1]
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)
