class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            counterpart = target - nums[i]
            if counterpart in seen:
                return [i, seen[counterpart]]
            seen[nums[i]] = i