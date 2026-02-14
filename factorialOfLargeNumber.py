class Solution:
    def factorial(self, n):
        fact = 1
        
        for i in range(1, n + 1):
            fact *= i
        return [int(d) for d in str(fact)]
