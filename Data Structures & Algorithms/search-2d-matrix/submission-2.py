class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l=0
        r = len(matrix) - 1

        while l<=r:
            m = (l + r)//2
            if target < matrix[m][0]:
                r = m-1
            elif target > matrix[m][-1]:
                l=m+1
            else:
                break

        l2,r2 = 0,len(matrix[m])-1

        while l2<=r2:
            m2 = (l2+r2)//2
            if target == matrix[m][m2]:
                return True
            elif target < matrix[m][m2]:
                r2 = m2 -1
            else:
                l2 = m2+1
        return False
            