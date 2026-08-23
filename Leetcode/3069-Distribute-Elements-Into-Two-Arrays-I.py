class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            arr1.append(nums[i]) if arr1[-1] > arr2[-1] else arr2.append(nums[i])
        return arr1 + arr2

    # def resultArray(self, nums: List[int]) -> List[int]:
    #     res = [nums[0], nums[1]]
    #     arr1, arr2 = 0, 1
    #     for i in range(2, len(nums)):
    #         if res[arr1] > res[arr2]:
    #             arr1+=1
    #             arr2+=1
    #             res.insert(arr1, nums[i])
    #         else:
    #             arr2+=1
    #             res.insert(arr2, nums[i])
    #     return res

        
