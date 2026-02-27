class Solution:
    

    def minSwaps(self, arr):
        n = len(arr)
        
     
        arrpos = list(enumerate(arr))
        
 
        arrpos.sort(key=lambda x: x[1])
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            
           
            if visited[i] or arrpos[i][0] == i:
                continue
            
            cycle_size = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                j = arrpos[j][0]
                cycle_size += 1
            
            if cycle_size > 0:
                swaps += cycle_size - 1
        
        return swaps
