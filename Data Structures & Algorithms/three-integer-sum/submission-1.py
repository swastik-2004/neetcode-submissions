from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array (Required for two-pointer approach)
        ans = []
        n = len(nums)
        
        for i in range(n):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # If the current number is positive, we can't find a sum of 0 
            # because the array is sorted and all subsequent numbers are positive
            if nums[i] > 0:
                break
                
            # Step 2: Two-pointer approach for the remaining part of the array
            l, r = i + 1, n - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    
                    # Skip duplicates for the second element
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Skip duplicates for the third element
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    # Move both pointers after finding a valid triplet
                    l += 1
                    r -= 1
                    
                elif total < 0:
                    l += 1  # Need a larger sum
                else:
                    r -= 1  # Need a smaller sum
                    
        return ans