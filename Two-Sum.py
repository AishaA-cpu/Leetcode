class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in enumerate(nums):
            idx, val = i
            diff = target - val
            if diff in seen:
                return [idx, seen[diff]]
            seen[val] = idx

        