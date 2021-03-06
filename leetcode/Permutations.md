https://leetcode.com/problems/permutations/
https://leetcode.com/problems/permutations-ii/

```
class Solution:

    # Use each value for each location till path has n values
    # Common solution is to build arrays, nums[i] + backtrack(nums[:i] + nums[i + 1:])
    # Generalization is to use Hashmap

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1 
            
        sols = []
        path = []
        
        self.backtrack(counts, sols, path, len(nums))
        
        return sols
    
    def backtrack(self, counts, sols, path, n):
        
        if len(path) == n:
            sols.append(path.copy())
            return
        
        for k, v in counts.items():
            
            if v:
                
                counts[k] -= 1
                path.append(k)
                self.backtrack(counts, sols, path, n)
                path.pop()
                counts[k] += 1
                
        return
```