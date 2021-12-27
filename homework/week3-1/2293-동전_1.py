n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp = [[0 for _ in range(k+1)] for _ in range(n)]
dp = [0 for _ in range(k+1)]

# O(nk^2) => out of time
'''
for coin in range(n):
    worth = coins[coin]
    for target in range(k+1):
        if (coin==0 and target%worth==0) or target == 0:
            dp[coin][target] = 1
            continue
        for count in range(0, target//worth+1):
            dp[coin][target] += dp[coin-1][target-worth*count]
'''

# O(nk), space: nk => out of memory
'''
for coin in range(n):
    worth = coins[coin]
    for target in range(k+1):
        if (coin==0 and target%worth==0) or target == 0:
            dp[coin][target] = 1
            continue
        else:
            dp[coin][target] += dp[coin][target-worth] + dp[coin-1][target]
'''

# O(nk), space: k => correct
for coin in range(n):
    worth = coins[coin]
    for target in range(k+1):
        if (coin==0 and target%worth==0) or target == 0:
            dp[target] = 1
        elif target-worth>=0:
            dp[target] += dp[target-worth]

print(dp[k])
