from random import randint

class Board:
    def __init__(self, board_height=8, board_width=8, num_gem_types=8):
        self.height = board_height
        self.width = board_width
        self.board = [[randint(0, num_gem_types - 1) for x in xrange(self.width)] for x in xrange(self.height)]
    def get_triple_sets(self):
        all_triple_sets = set()
        # get all horizontal matches by iterating over x inside y
        for y_coord in xrange(0, self.height):
            for x_coord in xrange(0, self.width):
                single_triple_set = set()
                # set.update(iterable) adds the items in the iterable to
                # the set, so we have to make an iterable tuple with one
                # coord pair to add to the set
                single_triple_set.update( ((x_coord, y_coord), ) )
                # adjacent_match_length is the number of same gems adjacent to one another
                adjacent_match_length = 1
                # iterate through the next gems in the current y-row
                for next_x_coord in xrange(x_coord + 1, self.width):
                    # get the gem values off the board to see if they're identical
                    gem_1 = self.board[y_coord][x_coord]
                    gem_2 = self.board[y_coord][next_x_coord]
                    # check if gem 1 matches the gem to the right of this gem (gem 2)
                    if gem_1 == gem_2:
                        # gems match, add the coord to the triple set
                        adjacent_match_length += 1
                        single_point_coord = (next_x_coord, y_coord)
                        # again, create an iterable with one item, or
                        # the set will iterate over the single point
                        single_triple_set.update( (single_point_coord, ) )
                    else:
                        # gems don't match, break out of the adjacent-check loop
                        break
                # if there are 3 or more identical gems adjacent to one another...
                if adjacent_match_length >= 3:
                    # again, create an iterable with one set, or all_triple_sets
                    # will try to iterate over all items in the set.
                    # we must use frozenset because sets are mutable and the set
                    # all_triple_sets will refuse to contain a mutable;
                    # frozenset is not mutable and can be hashed into a set
                    all_triple_sets.update((frozenset(single_triple_set), ))
        # filter duplicate subsets of larger supersets (4-longs containing 3-longs)
        num_triple_sets = len(all_triple_sets)
        # we turn all_triple_sets into a list so we can reliably iterate over its
        # items in a known order so that we don't compare one set to itself
        all_triple_sets_list = list(all_triple_sets)
        for point_1 in xrange(0, num_triple_sets):
            for point_2 in xrange(point_1 + 1, num_triple_sets):
                set_points_1 = all_triple_sets_list[point_1]
                set_points_2 = all_triple_sets_list[point_2]
                if set_points_1 >= set_points_2:
                    # as usual, use a tuple to foil the iteration that set likes to do
                    # set_points_1 is a proper superset of set_points_2, so remove set_points_2
                    all_triple_sets.difference_update( (set_points_2, ) )
                elif set_points_2 >= set_points_1:
                    # set_points_2 is a proper superset of set_points_1, so remove set_points_1
                    all_triple_sets.difference_update( (set_points_1, ) )
        return all_triple_sets
    def get_board(self):
        return self.board
    def set_board(self, to_set):
        self.board = to_set