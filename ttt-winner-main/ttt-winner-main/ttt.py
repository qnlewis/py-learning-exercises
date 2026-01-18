def find_winner(board):
    """Determine the winner of a tic-tac-toe game.
    
    Args:
        board: A 3x3 list of lists where each element is 'X', 'O', or None/empty.
        
    Returns:
        'X' if X has three in a row, 'O' if O has three in a row,
        None if there is no winner.
        
    Raises:
        ValueError: If the board is not 3x3, contains invalid players,
                    or has empty strings (only None is allowed for empty spaces)."""
                    
    if len(board) != 3 or any(len(row) != 3 for row in board):
        raise ValueError("Board must be 3x3")
    
    valid_players = {'X', 'O', None}
    for row in board:
        for cell in row:
            if cell not in valid_players:
                raise ValueError("Board can only contain 'X', 'O', or None")
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None