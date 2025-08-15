#include <bits/stdc++.h>
using namespace std;
int t, n, d, k, l, r;
int main() {
    cin >> t;
    while (t--) {
        cin >> n >> d >> k;

        vector<int> ans(n + d + 1, 0);
        for (int i = 1; i <= k; i++) {
            cin >> l >> r;
            ans[l]++;
            ans[r + d]--;
        }

        for (int i = 1; i <= n; i++) {
            ans[i] += ans[i - 1];
        }

        int maxEnd = d, minEnd = d;
        for (int i = d; i <= n; i++) {
            if (ans[i] > ans[maxEnd]) {
                maxEnd = i;
            }
            if (ans[i] < ans[minEnd]) {
                minEnd = i;
            }
        }
        cout << maxEnd - d + 1 << " " << minEnd - d + 1 << endl;
    }
    return 0;
}