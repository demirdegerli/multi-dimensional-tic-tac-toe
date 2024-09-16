# Multi Dimensional Tic-Tac-Toe Algorithm
Yeah, I know this is bad and spaghetti code :D But it works with no issues.

Took 5-6 hours to write from scratch.

This is an algorithm that I made for fun. The idea is came from my friend.
Basically two bots play the multi dimensional tic-tac-toe. Interactive mode can be enabled so the game can be played between the computer and human too.

You have to change the `interactive_mode` to `True` in order to play the game with the computer.

If `bot_sleep` is `True`, then bots will wait between the moves so you can watch and understand it.

## Game logic
There are 9 tic-tac-toe instances on the grid. The grid itself is another tic tac-toe-game. The moves on the small tic-tac-toe instances decide the next move.

Grid index scheme:
```
0 1 2
3 4 5
6 7 8
```

### Example
```
Start move from X (7,4)
**************************
|       |       |       |
|       |       |       |
|       |       |       |
-------------------------
|       |       |       |
|       |       |       |
|       |       |       |
-------------------------
|       |       |       |
|       |   X   |       |
|       |       |       |
**************************
O is placing to 4,4
**************************
|       |       |       |
|       |       |       |
|       |       |       |
-------------------------
|       |       |       |
|       |   O   |       |
|       |       |       |
-------------------------
|       |       |       |
|       |   X   |       |
|       |       |       |
**************************
X is placing to 4,0
**************************
|       |       |       |
|       |       |       |
|       |       |       |
-------------------------
|       | X     |       |
|       |   O   |       |
|       |       |       |
-------------------------
|       |       |       |
|       |   X   |       |
|       |       |       |
**************************
O is placing to 0,4
**************************
|       |       |       |
|   O   |       |       |
|       |       |       |
-------------------------
|       | X     |       |
|       |   O   |       |
|       |       |       |
-------------------------
|       |       |       |
|       |   X   |       |
|       |       |       |
**************************
X is placing to 4,2
**************************
|       |       |       |
|   O   |       |       |
|       |       |       |
-------------------------
|       | X   X |       |
|       |   O   |       |
|       |       |       |
-------------------------
|       |       |       |
|       |   X   |       |
|       |       |       |
**************************
```
... and so on.
