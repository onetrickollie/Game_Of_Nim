# Kaixiang Liu, Jahn Tibayan ,Jacob Sean Evasco
# CPSC 481 - 02
# Instructor: Dr. Panangadan

from games import Game, GameState

class GameOfNim(Game):
    # Initialize game board
    def __init__(self, initial):
        if isinstance(initial, list):
            moves = self.actions_from_board(initial)
            initial = GameState(to_move='MIN', utility=0, board=initial, moves=moves)
        self.initial = initial
    # function to determine actions
    def actions_from_board(self, board):
        moves = []
        for r, count in enumerate(board):
            moves.extend((r, n) for n in range(1, count + 1))
        return moves

    def actions(self, state):
        return state.moves
    
    # Function to determine results after each move
    def result(self, state, move):
        r, n = move
        new_board = state.board[:]
        new_board[r] -= n
        new_moves = self.actions_from_board(new_board)
        return GameState(
            to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
            utility=self.compute_utility(new_board, state.to_move),
            board=new_board,
            moves=new_moves
        )
    
    # Function to determine if the game ended
    # If board sum == 0, no more moves on the board
    def terminal_test(self, state):
        return sum(state.board) == 0
    
    # Function to determine the current state of a player
    # Using +/- as a switch
    def utility(self, state, player):
        return state.utility if player == 'MAX' else -state.utility
    
    def compute_utility(self, board, player):
        if sum(board) == 0:
            return -1 if player == 'MAX' else +1
        return 0

# Example main function to test the game
# Change the board here for other tests
if __name__ == '__main__':
    nim_game = GameOfNim([7, 5, 3, 1])
    state = nim_game.initial
    
    # Picking the first available moves
    computer_move = nim_game.actions(state)[0]  
    state = nim_game.result(state,computer_move)
    print(f"Computer move: {computer_move}")
    print("New board:", state.board)

    while not nim_game.terminal_test(state):
        print("current state: board:", state.board)
        print("available moves:", nim_game.actions(state))

        move = input("Your move? ")
        r, n = map(int, move.split(','))
        state = nim_game.result(state, (r, n))
        print(f"Move: ({r}, {n})")
        print("New board:", state.board)
        if nim_game.terminal_test(state):
            break
        computer_move = nim_game.actions(state)[0]
        state = nim_game.result(state, computer_move)
        print(f"Computer move: {computer_move}")
        print("New board:", state.board)
    
    if state.utility == +1:
        print("MAX won the game")
    else:
        print("MIN won the game")