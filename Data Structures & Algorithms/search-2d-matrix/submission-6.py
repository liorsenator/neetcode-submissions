class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        row = 0
        a, b = 0, m - 1
        while a <= b:
            mid = (a + b) // 2
            if matrix[mid][n-1] == target:
                return True
            if matrix[mid][n-1] < target:
                a += 1
            if matrix[mid][n-1] > target:
                b -= 1
            if matrix[mid][0] <= target and matrix[mid][n-1] >= target:
                row = mid
        l, r = 0, n-1
        while l <= r:
            mid1 = (l + r) // 2
            if matrix[row][mid1] == target:
                return True
            if matrix[row][mid1] < target:
                l += 1
            else:
                r -= 1
        return False