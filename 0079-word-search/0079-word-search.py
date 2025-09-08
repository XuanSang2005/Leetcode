class Solution(object):
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        L = len(word)

        def dfs(r, c, k):
            if k == L:
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False
            
            ch = board[r][c]
            board[r][c] = '#'

            found = (dfs(r+1, c, k+1) or    
                     dfs(r-1, c, k+1) or   
                     dfs(r, c+1, k+1) or   
                     dfs(r, c-1, k+1))     
                    
            board[r][c] = ch
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
