class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = {}
        seen_col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        seen_sq = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i in range(9):
            seen_row = {}
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen_row or board[i][j] in seen_col[j] or board[i][j] in seen_sq[(i//3)* 3 + (j//3)]:
                        return False
                    else:
                        seen_row[board[i][j]] = 1
                        seen_col[j][board[i][j]] = 1
                        seen_sq[(i//3)* 3 + (j//3)][board[i][j]] = 1
        return True
