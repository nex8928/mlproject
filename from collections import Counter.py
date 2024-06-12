from collections import Counter
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0

        for r in range(len(nums)):
            count_sub = Counter(nums[l:r+1])
            while max(count_sub.values(), default=0) >= k:
                count += len(nums) - r
                l += 1
                count_sub = Counter(nums[l:r+1])
        
        return count

# Example usage
sol = Solution()
print(sol.countSubarrays([1, 3, 2, 3, 3], 2))  # Example input
