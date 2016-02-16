# tictactoe

TicTacToe game versions:<br>
1) One player mode, against computer<br>
2) Two player mode, choosing your board size<br>

Possible improvements/features:<br>
1) make an easier-to-beat computer player
  A) Way computer could decide on next move
    i) if computer can win in next move, do so
    ii) if human will win in next move, computer blocks
    ii) make random moves when no move "appeals"
  B) Make levels
    i) level 1: computer makes random moves
    ii) level 2: computer uses its turn to win when possible and moves randomly otherwise
    iii) level 3: computer wins when possible, blocks opponent otherwise, and otherwise moves randomly
    iv) level 4: computer is unbeatable, using minimax calculations to make moves, either beating or tying with opponent
        
2) 3D tic tac toe<br>
  A) Better to implement win-checking generically, so it's easily scalable and not hard coded<br>
  B) Need good way to visualize and accept input<br>
    i) text based<br>
        a) just input 3rd dimension (use T(op), M(iddle), B(ottom) along with usual input; ie TB3 or MA1)<br>
        b) display each level side by side with "Top," "Middle," and "Botton" annotating each board level<br>
    ii) GUI based<br>
        a) display in 3D<br>
        b) click where you want to move<br>
            o) show ghost of possible move when hovering over possible position to prevent accidental moves<br>
  C) Num players:<br>
    i) 2 player<br>
    ii)Play against computer <br>
        a) This be very processing intensive. Might need to precompute game outcomes for computer's move selection.)<br>

TODO: rename "two_player.py" since it includes code for playing against computer<br>
TODO: make first computer move in middle of board for unbeatable version
TODO: