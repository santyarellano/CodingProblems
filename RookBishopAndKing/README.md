# Rook, Bishop and King
## Description
Little Petya is learning to play chess. He has already learned how to move a king, a rook and a bishop. Let us remind you the rules of moving chess pieces. A chessboard is 64 square fields organized into an 8 × 8 table. A field is represented by a pair of integers (r, c) — the number of the row and the number of the column (in a classical game the columns are traditionally indexed by letters). Each chess piece takes up exactly one field. To make a move is to move a chess piece, the pieces move by the following rules:

* A rook moves any number of fields horizontally or vertically.
* A bishop moves any number of fields diagonally.
* A king moves one field in any direction — horizontally, vertically or diagonally.

> The pieces move like that

Petya is thinking about the following problem: what minimum number of moves is needed for each of these pieces to move from field (r1, c1) to field (r2, c2)? At that, we assume that there are no more pieces besides this one on the board. Help him solve this problem.

### Input
The input contains four integers r1, c1, r2, c2 (1 ≤ r1, c1, r2, c2 ≤ 8) — the coordinates of the starting and the final field. The starting field doesn't coincide with the final one.

You can assume that the chessboard rows are numbered from top to bottom 1 through 8, and the columns are numbered from left to right 1 through 8.

### Output
Print three space-separated integers: the minimum number of moves the rook, the bishop and the king (in this order) is needed to move from field (r1, c1) to field (r2, c2). If a piece cannot make such a move, print a 0 instead of the corresponding number.

## Solution
Basically all we have to do is split the problem in 3 parts with the same input. First, we'll need to check how to solve the problem with the rook's rules, then with the Bishop's rules, and finally with the King's rules. Let's go over each one of them.

### Rook
The Rook moves horizontally or vertically in any amount of tiles with the rule of only moving in one direction. So, knowing this, we can check in 3 steps:
- If the destination is the same tile as the origin, then it nees 0 moves.
- If the destination is in the same axis as the origin, then it needs only 1 move.
- If none of the above apply, it will need 2 moves (as the rook can reach any tile in the map).

### Bishop
The Bishop follows the same formula as the Rook, with the exception that if the destinations is not in the same axis (in this case diagonal) we'll need to check if both the destination and the origin are on the same type of tile (black or white). To do this we'll consider that tile (1,1) is a black tile, this way all (pair, pair) and (odd, odd) tiles will be the black tiles.

### King
The King moves in any direction, but only one tile. Knowing this, we know that the fastest amount of moves we need to move from origin to destination is the greatest absolute difference between axis components.

Example:
```
Origin is (1, 1)
Destination is (5, 4)

diffX = |1-5| = 4
diffY = |1-4| = 3
max(diffX, diffY) = 4

So the total amount of moves required is 4
```