class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row1 = 0
        row2 = len(matrix)
        col = len(matrix[0]) - 1

        for row in range(len(matrix)):
            left = 0
            right = col

            while left <= right:
                mid = left + (right - left) // 2
                if target > matrix[row][mid]:
                    left = mid + 1
                elif target < matrix[row][mid]:
                    right = mid - 1
                else:
                    return True
            continue

        return False
        