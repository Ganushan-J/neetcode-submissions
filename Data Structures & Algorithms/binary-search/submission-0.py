class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 
            else:
                if nums[mid] > target:
                    right = mid - 1
        
        return -1

# nums -> array of ints, target -> int 
# sorted array - asc 
# if target exists, return index
# else -> return -1 
# O(log n) time complexity

'''
binary search approach 
- left = 0 -> -1, right = len(nums) -> 8
- inspecting the middle value of the array seeing whether it = target
- if middle < target 
   - left = mid + 1
- if middle > target
   - right = mid - 1


brute force approach 
- iterate through each of the numbers in nums 
- if it matches target then we can return the index 
- else -> return -1

- not optimal(for now)
'''

        