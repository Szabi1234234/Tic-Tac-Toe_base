def get_empty_board():
    '''
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    '''

    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]

    currentplayer = "X"
    gamerunning = True
    winner = None


def display_board(board):
  """
  Should print the tic tac toe board in a format similar to
       1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       --+---+---
    C   0 | X | . 
       --+---+---
  """
  print(board[0] + " I " + board[1] + " I " + board[2])
  print("----------------")
  print(board[3] + " I " + board[4] + " I " + board[5])
  print("----------------")
  print(board[6] + " I " + board[7] + " I " + board[8])


def is_board_full(board):
  """
  should return True if there are no more empty place on the board,
  otherwise should return False
  """
  pass


"""def get_winning_player(board):"""
  """
  Should return the player that wins based on the tic tac toe rules.
  If no player has won, than "None" is returned.
  """
  def checkCol(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
      winner = board[0]
      return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
      winner = board[3]
      return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
      winner = board[6]
      return True
  def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
      winner = board[0]
      return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
      winner = board[1]
      return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
      winner = board[1]
      return True
  def checkHorizontal(board):
# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)

    board = [
      ['X', "O", "."],
      ['X', "O", "."]
      ['0', "X", "."]
    ]
    print("""
    should print 
        1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       ---+---+---
    C   0 | X | . 
       ---+---+---
    """)
    
    display_board(board)
    
    board_1 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1)) 

    board_2 = [
      [".", "O", "O"],
      [".", "O", "X"],
      [".", "X", "X"],
    ]
    print("Should return False")
    print(is_board_full(board_2)) 

    board_3 = [
      ["O", "O", "X"],
      ["O", "X", "O"],
      ["O", "X", "X"],
    ]
    print("Should return True")
    print(is_board_full(board_3)) 

    board_4 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("Should return X")
    print(get_winning_player(board_4))

    board_5 = [
      ["X", "O", "O"],
      ["X", "O", "."],
      ["O", "X", "X"],
    ]
    print("Should return O")
    print(get_winning_player(board_5))

    board_6 = [
      ["O", "O", "."],
      ["O", "X", "."],
      [".", "X", "."],
    ]
    print("Should return None")
    print(get_winning_player(board_6))
    