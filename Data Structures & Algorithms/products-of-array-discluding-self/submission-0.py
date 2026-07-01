class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        temp_mult = 1
        for i in range(len(nums)):
            res[i] = temp_mult
            temp_mult *= nums[i]
        postfix = 1  
        for i in range(len(res)- 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
            