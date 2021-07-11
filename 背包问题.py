"""
背包问题，动态规划
"""

if __name__ == '__main__':
    weights = [1, 2, 3, 6, 7, 3, 5, 12, 45, 67, 9, 13]
    values = [2, 34, 5, 8, 78, 32, 4, 5, 15, 90, 111, 23]
    max_weight = 100
    nums = len(weights)
    dp = [[0 for j in range(max_weight+1)] for i in range(nums)]  # [nums, weights]， 建立二维数组
    # 先遍历物品，再遍历背包重量
    for i in range(nums):  # i 表示物品的索引，i+1表示物品数
        for j in range(max_weight+1):
            if j < weights[i]:
                # 物品重量大于包重量，肯定是不能放进去的
                dp[i][j] = dp[i-1][j]
            else:
                # 第i 个物品重量小于背包重量
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
                # dp[i-1][j] 不取第i个物品
                # dp[i-1][j-weights[i]]+values[i]  # 取第i个物品

    max_value = dp[-1][-1]
    print(max_value)


    dp = [[0 for j in range(max_weight + 1)] for i in range(nums)]
    # 也可以先遍历背包重量再遍历物品--需要额外初始化第一行--先遍历物品比先遍历背包更好理解一些
    for j in range(max_weight+1):
        if j >= weights[0]:
            dp[0][j] = values[0]
    for j in range(1, max_weight+1):
        for i in range(1, nums):
            if j < weights[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
    print(dp[-1][-1])


    # 比前一个数组多了一行--个人更喜欢第一种写法
    dp2 = [[0 for j in range(max_weight+1)] for i in range(nums+1)]
    for i in range(1, nums+1):  # i 表示物品数
        for j in range(1, max_weight+1):
            if j < weights[i-1]:
                dp2[i][j] = dp2[i-1][j]
            else:
                dp2[i][j] = max(dp2[i-1][j], dp2[i-1][j-weights[i-1]]+values[i-1])
    print(dp2[-1][-1])

    # 一维dp数组--滚动数组---物品价值可能还会有负数，此时初始化为负无穷!!!!
    # 二维数组可以重复利用，后一行是在前一行基础上进行滚动优化得到的。
    dp = [0 for j in range(max_weight+1)]
    # 物品数量i--滚动优化i次
    for i in range(nums):
        for j in range(max_weight, weights[i]+1, -1):
            # 注意这里的滚动优化方式，每一行是倒序优化的！！！！因为如果正序遍历，同一个物品会被放入多次！！！
            # 二维数组正序遍历就可以，因为前一行的数据不会被滚动覆盖！！！
            dp[j] = max(dp[j], dp[j-weights[i]]+values[i])
    print(dp[-1])





