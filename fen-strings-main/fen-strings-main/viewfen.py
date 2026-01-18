def parse_fen(fen_string: str) -> dict:
    parts = fen_string.strip().split()
    if len(parts) != 6:
        raise ValueError(f"Invalid FEN - expected 6 parts, got {len(parts)}")
    
    return {
        'piece_placement': parts[0],
        'active_color': parts[1],
        'castling_availability': parts[2],
        'en_passant': parts[3],
        'halfmove_clock': parts[4],
        'fullmove_number': parts[5]
    }

def create_board(piece_placement):
    board = []
    rows = piece_placement.split('/')
    for row in rows:
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend(['.'] * int(char))
            else:
                board_row.append(char)
        board.append(board_row)
    return board

def display_board(board):
    for row in board:
        print(' '.join(row))

def describe_castling(castling):
    if castling == '-':
        return "No castling available"
    
    descriptions = []
    if 'K' and 'Q' in castling:
        descriptions.append("White can castle both sides")
    elif 'K' in castling:
        descriptions.append("White can castle kingside")
    elif 'Q' in castling:
        descriptions.append("White can castle queenside")
  
    if 'k' and 'q' in castling:
        descriptions.append("Black can castle both sides")
    elif 'k' in castling:
        descriptions.append("Black can castle kingside")
    elif 'q' in castling:
        descriptions.append("Black can castle queenside")

    return '\n'.join(descriptions)

def describe_en_passant(en_passant: str) -> str:
    return "En passant: " + (en_passant if en_passant != '-' else "None")

def main(fen_string):
    fen_data = parse_fen(fen_string)
    board = create_board(fen_data['piece_placement'])
    display_board(board)
    print("\nWhite to move" if fen_data['active_color'] == 'w' else "Black to move")
    print(describe_castling(fen_data['castling_availability']))
    print(describe_en_passant(fen_data['en_passant']))
    print(f"Halfmove clock: {fen_data['halfmove_clock']}")
    print(f"Fullmove number: {fen_data['fullmove_number']}")
    

if __name__ == "__main__":   
    fen_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    main(fen_string)