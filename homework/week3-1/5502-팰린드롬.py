import sys

# => time out?
'''
n = int(input())
s = input()
'''

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
reverse_s = s[::-1]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if reverse_s[i-1] == s[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(n - dp[-1][-1])
