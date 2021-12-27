n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

'''
for coin: 1~n
    for target: 1~k
        for count: 0 ~ target/worth
            dp[coin][target] += dp[coin-1][target-worth*count]
O(nk^2)

        dp[coin][target] += dp[coin][target-worth] + dp[coin-1][target]

O(nk) space: nk

space: k
        dp[coin][target] += dp[coin][target-worth]

'''
