class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        util_array = ["_"] * len(nums)
        n = len(nums)
        
        
        for i in range(n):
            util_array[(i + k) % n] = nums[i]
            
        nums[:] = util_array[:]
            

        