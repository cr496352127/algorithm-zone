/*
CF1037D - 1300'
分析: 贪心 (区间贪心)
首先, 按区间 real 值递增排序
然后, 遍历各个区间, 若 l <= k <= r, 则更新 k = max(k, real)
注意 k 值可能比 max(real) 还大, 因此更新时不能直接设置 k = real
时间复杂度 O(nlogn), 空间复杂度 O(logn)
*/
#include <bits/stdc++.h>
using namespace std;
int t, n, k, l, r, rl;
vector<vector<int>> casinos;

bool cmp(vector<int>& c1, vector<int>& c2) {
    return c1[2] < c2[2];
}

int main() {
    cin >> t;
    while (t--) {
        cin >> n >> k;

        casinos.clear();
        for (int i = 0; i < n; i++) {
            cin >> l >> r >> rl;
            casinos.push_back({l, r, rl});
        }
        sort(casinos.begin(), casinos.end(), cmp);

        int res = k;
        for (int i = 0; i < n; i++) {
            l = casinos[i][0], r = casinos[i][1], rl = casinos[i][2];
            if (res >= l && res <= r) {
                res = max(res, rl);
            }
        }
        cout << res << endl;
    }
    return 0;
}
