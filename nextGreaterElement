class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # remove smaller or equal elements
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            # assign result
            if stack:
                result[i] = stack[-1]

            # push current element
            stack.append(arr[i])

        return result
