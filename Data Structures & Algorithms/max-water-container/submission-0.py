class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mat = []
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                mat.append(min(heights[i], heights[j])  * (j-i))
        return max(mat)