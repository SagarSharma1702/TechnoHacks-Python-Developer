'''Task 4 : Tic Tac Toe Game
Create a simple Tic Tac Toe game that can be
played between two players or against the
computer.'''
def print_board(board):
  for row in board:
      print(" | ".join(row))
      print("-" * 9)

def check_winner(board):
  # Check rows, columns, and diagonals for a winner
  for row in board:
      if row[0] == row[1] == row[2] != ' ':
          return True

  for col in range(3):
      if board[0][col] == board[1][col] == board[2][col] != ' ':
          return True

  if board[0][0] == board[1][1] == board[2][2] != ' ' or \
     board[0][2] == board[1][1] == board[2][0] != ' ':
      return True

  return False

def is_board_full(board):
  # Check if the board is full
  for row in board:
      for cell in row:
          if cell == ' ':
              return False
  return True

def get_player_move(player):
  # Get player's move
  while True:
      try:
          move = int(input(f"Player {player}, enter your move (1-9): "))
          if 1 <= move <= 9:
              return move
          else:
              print("Invalid move. Please enter a number between 1 and 9.")
      except ValueError:
          print("Invalid input. Please enter a number.")

def play_tic_tac_toe():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  players = ['X', 'O']
  current_player = players[0]

  print("Welcome to Tic Tac Toe!")

  while True:
      print_board(board)
      move = get_player_move(current_player)

      # Convert the move to board coordinates
      row = (move - 1) // 3
      col = (move - 1) % 3

      # Check if the selected cell is empty
      if board[row][col] == ' ':
          board[row][col] = current_player
      else:
          print("Invalid move. The cell is already taken. Try again.")
          continue

      # Check for a winner or a tie
      if check_winner(board):
          print_board(board)
          print(f"Player {current_player} wins!")
          break
      elif is_board_full(board):
          print_board(board)
          print("It's a tie!")
          break

      # Switch to the other player
      current_player = players[1] if current_player == players[0] else players[0]

# Call the play_tic_tac_toe function to start the game
play_tic_tac_toe()
