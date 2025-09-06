class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """
        rows, cols = len(matrix), len(matrix[0])

        # Bước 1: gom tất cả toạ độ có số 0
        zero_matrix = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_matrix.append((i, j))

        # Bước 2: với mỗi (r, c), set cả hàng r và cột c về 0
        for r, c in zero_matrix:
            # set hàng r
            for j in range(cols):
                matrix[r][j] = 0
            # set cột c
            for i in range(rows):
                matrix[i][c] = 0
