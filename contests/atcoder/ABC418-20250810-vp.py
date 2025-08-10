"""
ABC418 A-E
A. I'm a teapot
分析: 字符串
直接判断包含最后三个字符的子串是否是 "tea" 即可
时间复杂度 O(n), 空间复杂度 O(1)
"""
if __name__ == '__main__':
    n = int(input())
    s = str(input())
    res = "No"
    if len(s) >= 3 and s[-3:] == "tea":
        res = "Yes"
    print(res)


"""
B. You're a teapot
分析: 字符串 + 模拟
枚举所有长度 >= 3 的子串 s[i...j] (0 <= i <= j < n), 根据题目要求计算 x 和 t 的值
维护 max((x - 2) / (t - 2)) 即可
时间复杂度 O(n^2), 空间复杂度 O(n) (不预先维护前缀和数组也可以达到空间 O(1))
"""
if __name__ == '__main__':
    s = str(input())
    n = len(s)
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + (s[i] == "t")

    res = 0
    for i in range(n):
        for j in range(i + 2, n):
            if s[i] != "t" or s[j] != "t":
                continue
            sub_str = s[i: j + 1]
            t = j - i + 1
            x = pre_sum[j + 1] - pre_sum[i]
            res = max(res, (x - 2) / (t - 2))
    print(res)


"""
C. Flush
分析: 数组 + 前缀和 + 二分查找
对于 b > max(a), 选择所有 tea bags 也不能满足要求, 无解
否则, 在数组 a 中二分查找第一个 >= b 的索引 pos
从而满足要求的最小 x 包括三部分: 
pos 左侧所有的 tea bags 全选, 即 sum(a[0...pos - 1]), 可通过前缀和预处理
pos 处的 tea bags 选 b 个, 即 b
pos 右侧的 tea bags, 每种均选 (b - 1) 个, 即 (b - 1) * (n - pos - 1)
上述三部分之和即为所求
时间复杂度 O(q * logn), 空间复杂度 O(n)
"""
if __name__ == '__main__':
    n, q = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    up = max(a)
    a.sort()

    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + a[i]

    for _ in range(q):
        b = int(input())

        if b > up:
            print(-1)
            continue

        left, right, pos = 0, n - 1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if a[mid] >= b:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1

        res = pre_sum[pos] + b + (b - 1) * (n - pos - 1)
        print(res)


"""
D. XNOR Operation
分析: 字符串 + 动态规划 (线性 DP)
合并规则为异或的取反运算, 可考虑自左向右的合并过程, 使用动态规划求解
记: dp[i][0/1] = 以索引 i 结尾的子串 t[0...i], 最终合并为单个 "0"/"1" 时的方案数
从而有状态转移方程: 
Case 1. i == 0 时: 
    dp[0][int(t[0])] = 1
Case 2. i >= 1 时: 
    dp[i][0] = dp[i - 1][1] (t[i] == "0", "10" -> "1")
               dp[i - 1][0] (t[i] == "1", "01" -> "1")
    dp[i][1] = dp[i - 1][0] (t[i] == "0", "00" -> "1")
               dp[i - 1][1] (t[i] == "1", "11" -> "1")
最终, sum(dp[i][1]), 0 <= i < n 即为所求
时间复杂度 O(n), 空间复杂度 O(n)
"""
if __name__ == '__main__':
    n = int(input())
    t = str(input())

    dp = [[0] * 2 for _ in range(n)]; dp[0][int(t[0])] = 1
    for i in range(1, n):
        dp[i][int(t[i])] = 1
        if t[i] == "0":
            dp[i][0] += dp[i - 1][1]
            dp[i][1] += dp[i - 1][0]
        else:
            dp[i][0] += dp[i - 1][0]
            dp[i][1] += dp[i - 1][1]

    res = 0
    for i in range(n):
        res += dp[i][1]
    print(res)


"""
E. Trapezium
分析: 哈希表 + 数学
注意梯形 (trapezoid) 的特点是两底边平行且不等长
可将原问题 (二维平面上任取 4 个不同的点, 可构成的矩形个数) 转换为 计算平行边的对数
因此可借助两个哈希表 k_freq 和 side_freq, 分别统计各斜率对应的边数, 以及各 (斜率, 边长) 二元组对应的边数
然后遍历 k_freq 中的各个斜率 k, 则不考虑长度时平行边的对数
    target_ans = sum(k_freq[k] * (k_freq[k] - 1) / 2)
然后遍历 side_freq 中的(斜率, 边长) 二元组, 则等长的平行边的对数
    repeated_ans = sum(side_freq[k] * (side_freq[k] - 1) / 2)
从而, target_ans 为可以构成的梯形个数 (含平行四边形), repeated_ans * 2 为可以构成的平行四边形个数
target_ans - repeated_ans * 2 即为最终结果
时间复杂度 O(n^2 * logn), 空间复杂度 O(n^2) (考虑哈希表插入操作 logn 复杂度)
"""
import collections


if __name__ == '__main__':
    n = int(input())
    points = []
    for _ in range(n):
        x, y = list(map(int, input().strip().split()))
        points.append([x, y])

    INF = float("inf")
    k_freq = collections.defaultdict(int)
    side_freq = collections.defaultdict(int)
    target_ans, repeated_ans = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            k = INF
            if x2 != x1:
                k = (y2 - y1) / (x2 - x1)
            target_ans += k_freq[k]
            k_freq[k] += 1

            side_len = (x2 - x1) ** 2 + (y2 - y1) ** 2
            repeated_ans += side_freq[(k, side_len)]
            side_freq[(k, side_len)] += 1

    res = target_ans - repeated_ans // 2
    print(res)
"""
5
0 2
0 5
1 0
2 1
2 4

7
0 2
0 5
1 0
2 1
2 4
4 5
4 2
"""
