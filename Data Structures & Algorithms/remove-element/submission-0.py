class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        i, j = 0, n-1
        while i < j:
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i] == val and nums[j] == val:
                j -= 1
            elif nums[i] != val:
                i += 1
        
        count = 0
        for num in nums:
            if num != val:
                count += 1
        
        return count
