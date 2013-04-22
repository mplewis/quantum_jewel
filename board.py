from random import randint

class Board:
    def __init__(self, board_height=8, board_width=8, num_gem_types=8):
        self.height = board_height
        self.width = board_width
        self.board = [[randint(0, num_gem_types - 1) for x in xrange(self.width)] for x in xrange(self.height)]
    def get_matched_gems(self):
        '''Finds all gems that match and will be scored.'''
        # gems_to_break holds all gems that have been matched and will be broken on board update
        gems_to_break = set()
        # get all horizontal matches by iterating over x inside y
        for y_coord in xrange(0, self.height):
            for x_coord in xrange(0, self.width):
                # single_triple_list holds the gem (x, y) and same-colored gems that are adjacent
                single_triple_list = []
                single_point_coord = (x_coord, y_coord)
                single_triple_list.append(single_point_coord)
                # adjacent_match_length is the number of same-colored gems adjacent to one another
                adjacent_match_length = 1
                # iterate through the next gems in the current y-row
                for next_x_coord in xrange(x_coord + 1, self.width):
                    # get the gem values off the board to see if they're identical
                    gem_1 = self.board[y_coord][x_coord]
                    gem_2 = self.board[y_coord][next_x_coord]
                    # check if gem 1 matches the gem to the right (gem 2)
                    if gem_1 == gem_2:
                        # gems match, add the coord to the triple set and increment the count
                        single_point_coord = (next_x_coord, y_coord)
                        single_triple_list.append(single_point_coord)
                        adjacent_match_length += 1
                    else:
                        # gems don't match, break out of the adjacent-check loop
                        break
                # if there are 3 or more identical gems adjacent to one another...
                if adjacent_match_length >= 3:
                    # ...add all gem coords to the set of all gems to break
                    gems_to_break.update(single_triple_list)
        # get all vertical matches by iterating over y inside x
        for x_coord in xrange(0, self.height):
            for y_coord in xrange(0, self.width):
                # single_triple_list holds the gem (x, y) and same-colored gems that are adjacent
                single_triple_list = []
                single_point_coord = (x_coord, y_coord)
                single_triple_list.append(single_point_coord)
                # adjacent_match_length is the number of same-colored gems adjacent to one another
                adjacent_match_length = 1
                # iterate through the next gems in the current y-row
                for next_y_coord in xrange(y_coord + 1, self.width):
                    # get the gem values off the board to see if they're identical
                    gem_1 = self.board[y_coord][x_coord]
                    gem_2 = self.board[next_y_coord][x_coord]
                    # check if gem 1 matches the gem below (gem 2)
                    if gem_1 == gem_2:
                        # gems match, add the coord to the triple set and increment the count
                        single_point_coord = (x_coord, next_y_coord)
                        single_triple_list.append(single_point_coord)
                        adjacent_match_length += 1
                    else:
                        # gems don't match, break out of the adjacent-check loop
                        break
                # if there are 3 or more identical gems adjacent to one another...
                if adjacent_match_length >= 3:
                    # ...add all gem coords to the set of all gems to break
                    gems_to_break.update(single_triple_list)
        return gems_to_break
    def __get_gems_with_bounds(self):
        t_match_bases = set()
        gem_list = []
        for gem_coord in self.get_matched_gems():
            x_base, y_base = gem_coord
            lower_bound_x = x_base - 2
            upper_bound_x = x_base + 2
            lower_bound_y = y_base - 2
            upper_bound_y = y_base + 2
            if lower_bound_x < 0:
                lower_bound_x = 0
            if upper_bound_x > self.width - 1:
                upper_bound_x = self.width - 1
            if lower_bound_y < 0:
                lower_bound_y = 0
            if upper_bound_y > self.height - 1:
                upper_bound_y = self.height - 1
            gem_data = {"gem_coord": gem_coord,
                        "lower_bound_x": lower_bound_x,
                        "upper_bound_x": upper_bound_x,
                        "lower_bound_y": lower_bound_y,
                        "upper_bound_y": upper_bound_y}
            gem_list.append(gem_data)
        return gem_list
    def get_matches_t_l(self):
        '''Finds all T-shaped and L-shaped matches.'''
        gems_and_bounds = self.__get_gems_with_bounds()
        l_bases = set()
        for gem_data in gems_and_bounds:
            base_gem_x, base_gem_y = gem_data["gem_coord"]
            this_gem_color = self.board[base_gem_y][base_gem_x]
            first_adj_gem_found = False
            adjacent_match_length = 0
            for x_coord in xrange(gem_data["lower_bound_x"], gem_data["upper_bound_x"] + 1):
                next_gem_color = self.board[base_gem_y][x_coord]
                if not first_adj_gem_found:
                    if this_gem_color == next_gem_color:
                        first_adj_gem_found = True
                        adjacent_match_length += 1
                else:
                    if this_gem_color == next_gem_color:
                        adjacent_match_length += 1
                    else:
                        break
            if adjacent_match_length >= 3:
                first_adj_gem_found = False
                adjacent_match_length = 0
                for y_coord in xrange(gem_data["lower_bound_y"], gem_data["upper_bound_y"] + 1):
                    next_gem_color = self.board[y_coord][base_gem_x]
                    if not first_adj_gem_found:
                        if this_gem_color == next_gem_color:
                            first_adj_gem_found = True
                            adjacent_match_length += 1
                    else:
                        if this_gem_color == next_gem_color:
                            adjacent_match_length += 1
                        else:
                            break
                if adjacent_match_length >= 3:
                    print (base_gem_x, base_gem_y)
    def get_board(self):
        '''Returns a 2D matrix of the gems on the board.'''
        return self.board
    def set_board(self, to_set):
        '''Sets the board to an arbitrary 2D matrix of gems.'''
        self.board = to_set