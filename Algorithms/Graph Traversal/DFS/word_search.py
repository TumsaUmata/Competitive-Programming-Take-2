class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0] and self.traverse(board, word, i, j, 0):
                    return True
        return False

    def traverse(self, board, word, row, col, idx):
        if idx == len(word):
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[idx]:
            return False

        temp = board[row][col]

        board[row][col] = "#"

        found = self.traverse(board, word, row - 1, col, idx + 1) \
                or self.traverse(board, word, row + 1, col, idx + 1) \
                or self.traverse(board, word, row, col - 1, idx + 1) \
                or self.traverse(board, word, row, col + 1, idx + 1)

        board[row][col] = temp

        return found

