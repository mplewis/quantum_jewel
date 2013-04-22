from pprint import pprint
from board import Board

use_superset_board  = False
use_one_match_board = False
use_one_t_board     = True

superset_board  = ([[7, 4, 0, 5, 3, 4, 3, 0],
                    [4, 5, 3, 5, 7, 7, 7, 7],
                    [5, 1, 6, 0, 2, 0, 1, 4],
                    [5, 4, 6, 3, 0, 1, 1, 1],
                    [1, 4, 4, 7, 0, 6, 2, 5],
                    [4, 0, 4, 4, 4, 7, 7, 1],
                    [3, 2, 3, 4, 2, 2, 5, 1],
                    [5, 5, 3, 3, 2, 4, 0, 7]])

one_match_board = ([[3, 4, 1, 3, 5, 2, 1, 6],
                    [0, 1, 4, 7, 4, 7, 5, 5],
                    [5, 2, 1, 0, 5, 5, 5, 1],
                    [4, 2, 2, 4, 2, 3, 0, 6],
                    [4, 1, 3, 7, 1, 5, 7, 0],
                    [1, 5, 0, 1, 3, 4, 4, 2],
                    [5, 0, 3, 5, 1, 5, 6, 0],
                    [6, 7, 0, 0, 2, 6, 6, 3]])

one_t_board     = ([[3, 4, 1, 3, 5, 2, 1, 6],
                    [0, 1, 4, 7, 4, 7, 5, 5],
                    [5, 2, 1, 0, 5, 5, 5, 1],
                    [4, 2, 2, 4, 2, 5, 0, 6],
                    [4, 1, 3, 7, 1, 5, 7, 0],
                    [1, 5, 0, 1, 3, 4, 4, 2],
                    [5, 0, 3, 5, 1, 5, 6, 0],
                    [6, 7, 0, 0, 2, 6, 6, 3]])

if use_superset_board:
    bd = Board()
    bd.set_board(superset_board)
    matched_gems = bd.get_matched_gems()
elif use_one_match_board:
    bd = Board()
    bd.set_board(one_match_board)
    matched_gems = bd.get_matched_gems()
elif use_one_t_board:
    bd = Board()
    bd.set_board(one_t_board)
    matched_gems = bd.get_matched_gems()
else:
    # create board with default size 8x8
    num_gems_matched = 0
    while num_gems_matched < 20:
        bd = Board()
        matched_gems = bd.get_matched_gems()
        num_gems_matched = len(matched_gems)
    pprint(matched_gems)

raw_board = bd.get_board()
pprint(raw_board)
sparse_board = [[' ' for x in xrange(8)] for x in xrange(8)]
pprint(matched_gems)

for coord_pair in matched_gems:
    x_coord, y_coord = coord_pair
    sparse_board[y_coord][x_coord] = str(raw_board[y_coord][x_coord])

pprint(sparse_board)

bd.get_matches_t_l()