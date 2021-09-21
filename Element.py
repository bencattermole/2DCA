import Grid
import random


class Element:
    def __init__(self, name, pos_x, pos_y, colour):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.colour = self.determine_colour(colour)
        self.is_falling = False

    def update(self, grid):
        pass

    def pos_swap(self, new_pos_x, new_pos_y):
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y

    def determine_colour(self, colour_base):
        if colour_base[0] <= 10 or colour_base[1] <= 10 or colour_base[2] <= 10:
            colour = colour_base
        else:
            colour_r = (colour_base[0] + random.randint(-10, 10))
            colour_g = (colour_base[1] + random.randint(-10, 10))
            colour_b = (colour_base[2] + random.randint(-10, 10))
            colour = (colour_r, colour_g, colour_b)
        return colour

    def flip_falling(self):
        new_val = self.is_falling
        self.is_falling = not new_val


class Liquid(Element):
    def __init__(self, name, pos_x, pos_y, color, disp_rate):
        super().__init__(name, pos_x, pos_y, color)
        self.dispersion_rate = disp_rate

    def update(self, grid):
        neighbors = grid.get_pos_of_neighbours_moore(self.pos_x, self.pos_y, 1)
        check_for_hoz_random = False
        check_for_random = False
        if neighbors[self.pos_x, self.pos_y + 1][2] == 0:
            grid.update_cell(self.pos_x, self.pos_y, 0)
            grid.update_cell(self.pos_x, self.pos_y + 1, self)
            self.pos_y += 1
        elif neighbors[self.pos_x - 1, self.pos_y + 1][2] == 0 and neighbors[self.pos_x + 1, self.pos_y + 1][2] == 0:
            check_for_hoz_random = True
            if random.uniform(0, 1) > 0.5:
                grid.update_cell(self.pos_x, self.pos_y, 0)
                grid.update_cell(self.pos_x - 1, self.pos_y + 1, self)
                self.pos_x -= 1
                self.pos_y += 1
            else:
                grid.update_cell(self.pos_x, self.pos_y, 0)
                grid.update_cell(self.pos_x + 1, self.pos_y + 1, self)
                self.pos_x += 1
                self.pos_y += 1
        elif neighbors[self.pos_x - 1, self.pos_y + 1][2] == 0 and not check_for_hoz_random:
            grid.update_cell(self.pos_x, self.pos_y, 0)
            grid.update_cell(self.pos_x - 1, self.pos_y + 1, self)
            self.pos_x -= 1
            self.pos_y += 1
        elif neighbors[self.pos_x + 1, self.pos_y + 1][2] == 0 and not check_for_hoz_random:
            grid.update_cell(self.pos_x, self.pos_y, 0)
            grid.update_cell(self.pos_x + 1, self.pos_y + 1, self)
            self.pos_x += 1
            self.pos_y += 1
        elif neighbors[self.pos_x - 1, self.pos_y][2] == 0 and neighbors[self.pos_x + 1, self.pos_y][2] == 0:
            check_for_random = True
            if random.uniform(0, 1) > 0.5:
                grid.update_cell(self.pos_x, self.pos_y, 0)
                grid.update_cell(self.pos_x - 1, self.pos_y, self)
                self.pos_x -= 1
            else:
                grid.update_cell(self.pos_x, self.pos_y, 0)
                grid.update_cell(self.pos_x + 1, self.pos_y, self)
                self.pos_x += 1
        elif neighbors[self.pos_x - 1, self.pos_y][2] == 0 and not check_for_random:
            grid.update_cell(self.pos_x, self.pos_y, 0)
            grid.update_cell(self.pos_x - 1, self.pos_y, self)
            self.pos_x -= 1
        elif not check_for_random and neighbors[self.pos_x + 1, self.pos_y][2] == 0:
            grid.update_cell(self.pos_x, self.pos_y, 0)
            grid.update_cell(self.pos_x + 1, self.pos_y, self)
            self.pos_x += 1
        else:
            grid.update_cell(self.pos_x, self.pos_y, self)
            if self.is_falling:
                self.flip_falling()

        return grid

    def determine_colour(self, colour_base):
        return colour_base


class Solid(Element):
    def __init__(self, name, pos_x, pos_y, color, resist, inert_resist):
        super().__init__(name, pos_x, pos_y, color)
        self.resist = resist
        self.inert_resist = inert_resist

    '''
            if isinstance(neighbors[self.pos_x, self.pos_y + 1][2], Liquid):
                grid.update_cell(self.pos_x, self.pos_y, 0)
                grid.update_cell(self.pos_x, self.pos_y + 1, self)
                self.pos_y += 1
    '''

    def update(self, grid):
        neighbors = grid.get_pos_of_neighbours_moore(self.pos_x, self.pos_y, 1)
        check_for_hoz_random = False
        #print(f'f{neighbors}')
        if neighbors[self.pos_x, self.pos_y + 1][2] == 0:
            grid.update_cell(self.pos_x, self.pos_y, 0)
            grid.update_cell(self.pos_x, self.pos_y + 1, self)
            self.pos_y += 1
        elif isinstance(neighbors[self.pos_x, self.pos_y + 1][2], Liquid):
            grid.update_cell(self.pos_x, self.pos_y, neighbors[self.pos_x, self.pos_y + 1][2])
            neighbors[self.pos_x, self.pos_y + 1][2].pos_swap(self.pos_x, self.pos_y)
            grid.update_cell(self.pos_x, self.pos_y + 1, self)
            self.pos_y += 1

        elif neighbors[self.pos_x - 1, self.pos_y + 1][2] == 0 and neighbors[self.pos_x + 1, self.pos_y + 1][2] == 0:
            check_for_hoz_random = True
            if random.uniform(0, 1) > 0.5:
                grid.update_cell(self.pos_x, self.pos_y, 0)
                grid.update_cell(self.pos_x - 1, self.pos_y + 1, self)
                self.pos_x -= 1
                self.pos_y += 1
            else:
                grid.update_cell(self.pos_x, self.pos_y, 0)
                grid.update_cell(self.pos_x + 1, self.pos_y + 1, self)
                self.pos_x += 1
                self.pos_y += 1
        elif neighbors[self.pos_x - 1, self.pos_y + 1][2] == 0 and not check_for_hoz_random:
            grid.update_cell(self.pos_x, self.pos_y, 0)
            grid.update_cell(self.pos_x - 1, self.pos_y + 1, self)
            self.pos_x -= 1
            self.pos_y += 1
        elif isinstance(neighbors[self.pos_x - 1, self.pos_y + 1][2], Liquid):
            grid.update_cell(self.pos_x, self.pos_y, neighbors[self.pos_x - 1, self.pos_y + 1][2])
            neighbors[self.pos_x - 1, self.pos_y + 1][2].pos_swap(self.pos_x, self.pos_y)
            grid.update_cell(self.pos_x - 1, self.pos_y + 1, self)
            self.pos_x -= 1
            self.pos_y += 1
        elif neighbors[self.pos_x + 1, self.pos_y + 1][2] == 0 and not check_for_hoz_random:
            grid.update_cell(self.pos_x, self.pos_y, 0)
            grid.update_cell(self.pos_x + 1, self.pos_y + 1, self)
            self.pos_x += 1
            self.pos_y += 1
        elif isinstance(neighbors[self.pos_x + 1, self.pos_y + 1][2], Liquid):
            grid.update_cell(self.pos_x, self.pos_y, neighbors[self.pos_x + 1, self.pos_y + 1][2])
            neighbors[self.pos_x + 1, self.pos_y + 1][2].pos_swap(self.pos_x, self.pos_y)
            grid.update_cell(self.pos_x + 1, self.pos_y + 1, self)
            self.pos_x += 1
            self.pos_y += 1
        else:
            grid.update_cell(self.pos_x, self.pos_y, self)
            if self.is_falling:
                self.flip_falling()

        return grid


def falling_sands_iteration(grid, element_list, Screen_Size):

    for element in element_list:
        grid = element.update(grid)

    return grid
