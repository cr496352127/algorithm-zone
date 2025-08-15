/*
Technocup2022C - 1300'
分析: 贪心
注意数组 x 中的元素可以为正数/负数/0, 且可能有重复
同时除最后一趟外, 每趟不论向左还是向右, 必然会经过原点
因此, 左右两侧分开处理:
1. 将数组 x 递增排序, 左右两侧每 k 个一组考虑 (因为这 k 个快递中, 距离远的一定会送到, 距离近的可以在去程/返程途中顺便送到)
2. 不妨假设最后一趟返回原点, 然后减去最后一趟移动距离的最大值即可
2.1 计算数组 x 中第一个 >= 0 的索引 pos (假设从 1 开始, 不存在则记为 n + 1)
2.2 处理左侧: 循环索引 1 到 pos - 1, 步长为 k, 累加经过的元素和的相反数 (左侧最远位置, 可送达 <= k 个快递)
2.3 处理右侧: 循环索引 pos 到 n, 步长为 k, 累加经过的元素和 (右侧最远位置, 可送达 <= k 个快递)
2.4 最后, 将左右两侧累加结果之和减去 max(-x[1], a[n]) 即为所求 (最后一趟不返回原点, 最后一趟向左/向右取最大值)
时间复杂度 O(nlogn), 空间复杂度 O(logn)
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MAXN = 200005;
ll t, n, k, x[MAXN];
int main() {
    cin >> t;
    while (t--) {
        cin >> n >> k;
        for (int i = 1; i <= n; i++) {
            cin >> x[i];
        }

        int pos = n + 1;
        sort(x + 1, x + n + 1);
        for (int i = 1; i <= n; i++) {
            if (x[i] >= 0) {
                pos = i;
                break;
            }
        }

        ll res = 0;
        for (int i = 1; i < pos; i += k) {
            res -= x[i];
        }
        for (int i = n; i >= pos; i -= k) {
            res += x[i];
        }

        res = 2 * res - max(-x[1], x[n]);
        cout << res << endl;
    }
    return 0;
}