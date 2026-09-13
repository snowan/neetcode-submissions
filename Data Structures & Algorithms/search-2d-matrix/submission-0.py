class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            row = matrix[r]
            if self.binarySearch(row, target) != -1:
                return True
        
        return False
                
        
    def binarySearch(self, lists, target):
        l, r = 0, len(lists) - 1
        while l <= r:
            m = l + (r - l) // 2
            if lists[m] == target:
                return m
            elif lists[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
    
    
            