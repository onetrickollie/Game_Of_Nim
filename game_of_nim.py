# File: game_of_nim.py

from games import Game, GameState

class GameOfNim(Game):
    def __init__(self, initial):
        if isinstance(initial, list):
            moves = self.actions_from_board(initial)
            initial = GameState(to_move='MAX', utility=0, board=initial, moves=moves)
        self.initial = initial

    def actions_from_board(self, board):
        moves = []
        for r, count in enumerate(board):
            moves.extend((r, n) for n in range(1, count + 1))
        return moves

    def actions(self, state):
        return state.moves
    
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
    
    def terminal_test(self, state):
        return sum(state.board) == 0
    
    def utility(self, state, player):
        return state.utility if player == 'MAX' else -state.utility
    
    def compute_utility(self, board, player):
        if sum(board) == 0:
            return -1 if player == 'MAX' else +1
        return 0

# Example main function to test the game
if __name__ == '__main__':
    nim_game = GameOfNim([7, 5, 3, 1])
    state = nim_game.initial

    while not nim_game.terminal_test(state):
        print("board:", state.board)
        move = input("Your move? (format: r,n): ")
        r, n = map(int, move.split(','))
        state = nim_game.result(state, (r, n))
        print(f"Move: ({r}, {n})")
        print("New board:", state.board)
        if nim_game.terminal_test(state):
            break
        computer_move = nim_game.actions(state)[0]  # Simplified: just pick the first available move
        state = nim_game.result(state, computer_move)
        print(f"Computer move: {computer_move}")
        print("New board:", state.board)
    
    if state.utility == +1:
        print("MAX won the game")
    else:
        print("MIN won the game")
