class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # Sum 0 can always be formed
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(target + 1):
                
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]
