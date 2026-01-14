T = int(input())

n = [0]*T

for i in range(T):
    n[i] = int(input())

max_number = max(n)

dp = [0] * (max_number + 1)
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4, max_number + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    print(dp[n[i]])