s1 = input()
s2 = input()

dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
LCS = [['' for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            LCS[i][j] = LCS[i-1][j-1] + s1[i-1]
        else:
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                LCS[i][j] = LCS[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                LCS[i][j] = LCS[i][j-1]

print(dp[-1][-1])
print(LCS[-1][-1])
