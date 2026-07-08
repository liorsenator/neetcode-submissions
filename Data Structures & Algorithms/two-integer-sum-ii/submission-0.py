class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left < right:
            sum_r_l = numbers[left] + numbers[right]
            if sum_r_l > target:
                right -= 1
            elif sum_r_l < target:
                left += 1
            elif sum_r_l == target:
                return [left + 1, right +1]
        