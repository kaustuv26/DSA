class Solution(object):
    def validTicTacToe(self, board):
        x_count = 0
        o_count = 0
        for row in board:
            x_count += row.count('X')
            o_count += row.count('O')
        
        if o_count > x_count or x_count - o_count > 1:
            return False
        
        def check_win(player):
            # Check rows
            for i in range(3):
                if all(cell == player for cell in board[i]):
                    return True
            # Check columns
            for j in range(3):
                if all(board[i][j] == player for i in range(3)):
                    return True
            # Check diagonals
            if board[0][0] == board[1][1] == board[2][2] == player:
                return True
            if board[0][2] == board[1][1] == board[2][0] == player:
                return True
            return False
        
        x_wins = check_win('X')
        o_wins = check_win('O')
        
        if x_wins and o_wins:
            return False
        if x_wins and x_count != o_count + 1:
            return False
        if o_wins and o_count != x_count:
            return False
        
        return True
