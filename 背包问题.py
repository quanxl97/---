"""
01背包问题，动态规划
"""

if __name__ == '__main__':
    weights = [1, 2, 3, 6, 7, 3, 5, 12, 45, 67, 9, 13]
    values = [2, 34, 5, 8, 78, 32, 4, 5, 15, 90, 111, 23]
    max_weight = 100
    nums = len(weights)
    dp = [[0 for j in range(max_weight+1)] for i in range(nums)]  # [nums, weights]
    # 先遍历物品，再遍历背包
    for i in range(nums):
        for j in range(max_weight+1):
            if j < weights[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
    max_value = dp[-1][-1]
    print(max_value)

