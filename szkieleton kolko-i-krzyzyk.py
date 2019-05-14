#!/usr/bin/python
# -*- coding: utf-8 -*-

# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

"""
Kółko i krzyżyk
Komputer gra w kółko i krzyżyk przeciwko człowiekowi
"""

# wyświetla zasady gry i obsługi programu
def display_instruct():
    """Wyświetl instrukcję gry."""  
    print(
    """
    Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
    gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim
    ludzkim mózgiem a moim krzemowym procesorem.  

    Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
    Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Przygotuj się, Człowieku.  Ostateczna batalia niebawem się rozpocznie. \n
    """
    )
 
# odebranie od użytkownika decyzji, kto powinien rozpocząć grę
def ask_yes_no(question):


# zadanie pytania użytkownikowi, pole o którym numerze, chce zająć
# posiada system zabezpieczający przed podaniem liczby spoza zakresu
def ask_number(question, low, high):
     
# ustalenie do kogo należy ruch i przypisanie graczowi odpowiedniego znaku (X lub O)
def pieces():

# wyświetla planszę do gry
def display_board(board):

# komunikat o błędnym ruchu
def false_move():

# komunikat o poprawnym ruchu
def move_accepted():

# podanie informacji o ruchu komputera
def print_computer_move(move):

# wyświetla wynik gry
def congrat_winner(the_winner, computer, human):
   
"""
/ \
 |
 Funkcje odpowiadające za komunikację z użytkownikiem

#############################################################################################

Funkcje odpowiadające, za właściwą grę
 |
\ /
"""

# tworzy nową planszę do gry
def new_board():
    
# sprawdza dozwolone ruchy na zadanej planszy
def legal_moves(board):

# sprawdza wynik gry, decyduje także o remisie
def winner(board):

# odpowiada za przepisanie danych podanych od użytkownika to komputerowej reprezentacji planszy
def human_move(board, human):
 
# implementacja algorytmu otpowiadającego za grę komputera
def computer_move(board, computer, human):
 """Spowoduj wykonanie ruchu przez komputer."""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę
    board = board[:]
    # najlepsze pozycje do zajęcia według kolejności
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    # pułapki człowieka
    TRAP = ((0,8),(2,6))
    print("Wybieram pole numer", end=" ")
    
    # jeśli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY
    
    # jeśli człowiek może wygrać, zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # jeśli człowiek próbuje oskrzydlić komputer
    for move in (1,3,5,7):
      if (human in board[0] and human in board[8]) or (human in board[2] and human in board[6]) :
          board[move] = computer
          print(move)
          return move
        
      board[move]=EMPTY
      

    # ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


# zmiana wykonawcy ruchu
def next_turn(turn):



# main
def main():
 
# rozpocznij program
main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")

