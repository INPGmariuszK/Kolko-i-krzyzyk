#!/usr/bin/python
# -*- coding: utf-8 -*-

# 'stałe' globalne
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
X = "X"
O = "O"

# zwraca listę dozwolonych ruchów
def legal_moves(board):
    """Utwórz listę prawidłowych ruchów."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

# wyznacza zwycięzcę
def winner(board):
    """Ustal zwycięzcę gry."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

if __name__ == "__main__":
    pass
