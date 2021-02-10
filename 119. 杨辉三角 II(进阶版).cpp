class Solution1 {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> dp(rowIndex + 1, vector<int>(rowIndex + 1, 0));
        for (int i = 0; i <= rowIndex; i++) {
            dp[i][0] = 1;
            dp[i][i] = 1;
        }

        for (int i = 1; i <= rowIndex; i++) {
            for (int j = 1; j < i; j++) {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }
        }

        return dp[rowIndex];
    }
};

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> dp(rowIndex + 1, 1);
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i - 1; j >= 1; j--) {
                dp[j] = dp[j - 1] + dp[j];
            }
        }

        return dp;
    }
};