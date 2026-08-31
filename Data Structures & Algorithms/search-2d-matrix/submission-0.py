# same tosame but 2d meaning x[i][j] could be fun 



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])


        l =  0
        r = (m*n) - 1
        while l<=r:
            mid = (l+r) // 2

            row = mid // n# smart idea not my logic we will comeup with it next time thouuuuuuu
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid +1
            else:
                r = mid -1
        return False