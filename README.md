# Author: 
Kaixiang Liu
Jahn Tibayan
Jacob Sean Evasco


# Game of Nim

This project implements the Game of Nim using a Python class that defines the game rules. The game can be played between a computer using the Minimax algorithm with alpha-beta pruning and a human player. This project is part of a programming assignment and serves as a foundation for implementing adversarial search algorithms.

## Game Rules

- Two players take turns removing objects from distinct heaps or rows.
- In each turn, a player must remove at least one object from the same row.
- The player that removes the last object loses the game.
- The game state is represented by a list where each element denotes the number of objects in each row (e.g., `[5, 3, 1]`).

## Getting Started

### Prerequisites

- Python 3.x
- Git

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/onetrickollie/Game_Of_Nim.git
   cd Game_Of_Nim

### Running the Game

**Run this line of command in terminal**
/usr/bin/python3 game_of_nim.py


### Example Gameplay: 
- board:  [7, 5, 3, 1]
- Computer move: (0, 1)
- current state: board: [6, 5, 3, 1]
- available moves: [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]

- Your move? 1,2
- Move: (1, 2)
- current state: board: [6, 3, 3, 1]
- available moves: [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1)]
- Computer move: (0, 1)
- current state: board: [5, 3, 3, 1]
- available moves: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1)]

- ...

- (MAX won the game)
