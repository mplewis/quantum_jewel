from pprint import pprint
from board import Board

use_superset_board = False

superset_board = ([[7, 4, 0, 5, 3, 4, 3, 0],
                   [4, 5, 3, 5, 7, 7, 7, 7],
                   [5, 1, 6, 0, 2, 0, 1, 4],
                   [5, 4, 6, 3, 0, 1, 1, 1],
                   [1, 4, 4, 7, 0, 6, 2, 5],
                   [4, 0, 4, 4, 4, 7, 7, 1],
                   [3, 2, 3, 4, 2, 2, 5, 1],
                   [5, 5, 3, 3, 2, 4, 0, 7]])



if not use_superset_board:
    # create board with default size 8x8
    num_triples = 0
    while num_triples < 3:
        bd = Board()
        all_triple_sets = bd.get_triple_sets()
        num_triples = len(all_triple_sets)
    pprint(all_triple_sets)
else:
    bd = Board()
    bd.set_board(superset_board)
    all_triple_sets = bd.get_triple_sets()

raw_board = bd.get_board()
pprint(raw_board)
sparse_board = [[' ' for x in xrange(8)] for x in xrange(8)]
pprint(all_triple_sets)

# de-dupe all coordinates
all_triple_coord_pairs = set()
for triple_set in all_triple_sets:
    for coord_pair in triple_set:
        all_triple_coord_pairs.update( (coord_pair, ) )

pprint(all_triple_coord_pairs)

for coord_pair in all_triple_coord_pairs:
    x_coord, y_coord = coord_pair
    sparse_board[y_coord][x_coord] = str(raw_board[y_coord][x_coord])

pprint(sparse_board)