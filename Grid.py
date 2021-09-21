import pygame
import random
import Element

class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid_actives = {}

    def initiate_grid(self):
        for i in range(0, int(self.width/self.cell_size), 1):
            for j in range(0, int(self.height/self.cell_size), 1):
                self.grid_actives[(i, j)] = 0

    def get_sum_of_neighbours_moore(self, pos_x, pos_y, view_dist):
        num_of_neighbours = 0

        if 1 <= pos_x <= 126 and 1 <= pos_y <= 126:
            if self.grid_actives[(pos_x, pos_y - 1)] != 0:
                num_of_neighbours += 1
            if self.grid_actives[(pos_x, pos_y + 1)] != 0:
                num_of_neighbours += 1
            if self.grid_actives[(pos_x + 1, pos_y)] != 0:
                num_of_neighbours += 1
            if self.grid_actives[(pos_x - 1, pos_y)] != 0:
                num_of_neighbours += 1
            if self.grid_actives[(pos_x - 1, pos_y - 1)] != 0:
                num_of_neighbours += 1
            if self.grid_actives[(pos_x + 1, pos_y + 1)] != 0:
                num_of_neighbours += 1
            if self.grid_actives[(pos_x + 1, pos_y - 1)] != 0:
                num_of_neighbours += 1
            if self.grid_actives[(pos_x - 1, pos_y + 1)] != 0:
                num_of_neighbours += 1
        else:
            num_of_neighbours = 0

        return num_of_neighbours

    def get_pos_of_neighbours_moore(self, pos_x, pos_y, view_dist):
        neighbors = {}

        if 1 <= pos_x <= 124 and 1 <= pos_y <= 124:
            neighbors[(pos_x, pos_y - 1)] = (pos_x, pos_y - 1, self.grid_actives[(pos_x, pos_y - 1)])
            neighbors[(pos_x, pos_y + 1)] = (pos_x, pos_y + 1, self.grid_actives[(pos_x, pos_y + 1)])
            neighbors[(pos_x + 1, pos_y)] = (pos_x + 1, pos_y, self.grid_actives[(pos_x + 1, pos_y)])
            neighbors[(pos_x - 1, pos_y)] = (pos_x - 1, pos_y, self.grid_actives[(pos_x - 1, pos_y)])
            neighbors[(pos_x - 1, pos_y - 1)] = (pos_x - 1, pos_y - 1, self.grid_actives[(pos_x - 1, pos_y - 1)])
            neighbors[(pos_x + 1, pos_y + 1)] = (pos_x + 1, pos_y + 1, self.grid_actives[(pos_x + 1, pos_y + 1)])
            neighbors[(pos_x + 1, pos_y - 1)] = (pos_x + 1, pos_y - 1, self.grid_actives[(pos_x + 1, pos_y - 1)])
            neighbors[(pos_x - 1, pos_y + 1)] = (pos_x - 1, pos_y + 1, self.grid_actives[(pos_x - 1, pos_y + 1)])
        else:
            neighbors[(pos_x, pos_y - 1)] = (0, 0, 0)
            neighbors[(pos_x, pos_y + 1)] = (0, 0, 0)
            neighbors[(pos_x + 1, pos_y)] = (0, 0, 0)
            neighbors[(pos_x - 1, pos_y)] = (0, 0, 0)
            neighbors[(pos_x - 1, pos_y - 1)] = (0, 0, 0)
            neighbors[(pos_x + 1, pos_y + 1)] = (0, 0, 0)
            neighbors[(pos_x + 1, pos_y - 1)] = (0, 0, 0)
            neighbors[(pos_x - 1, pos_y + 1)] = (0, 0, 0)

        return neighbors

    def get_sum_of_neighbours_von(self, pos_x, pos_y, view_dist):
        num_of_neighbours = 0

        if 1 <= pos_x <= 124 and 1 <= pos_y <= 124:
            if self.grid_actives[(pos_x, pos_y - 1)] != 0:
                num_of_neighbours += 1
            elif self.grid_actives[(pos_x, pos_y + 1)] != 0:
                num_of_neighbours += 1
            elif self.grid_actives[(pos_x + 1, pos_y)] != 0:
                num_of_neighbours += 1
            elif self.grid_actives[(pos_x - 1, pos_y)] != 0:
                num_of_neighbours += 1
        else:
            num_of_neighbours = 0

        return num_of_neighbours

    def get_pos_of_neighbours_von(self, pos_x, pos_y, view_dist):
        neighbors = {}

        if 1 <= pos_x <= 62 and 1 <= pos_y <= 62:
            neighbors[(pos_x, pos_y - 1)] = (pos_x, pos_y - 1, self.grid_actives[(pos_x, pos_y - 1)])
            neighbors[(pos_x, pos_y + 1)] = (pos_x, pos_y + 1, self.grid_actives[(pos_x, pos_y + 1)])
            neighbors[(pos_x + 1, pos_y)] = (pos_x + 1, pos_y, self.grid_actives[(pos_x + 1, pos_y)])
            neighbors[(pos_x - 1, pos_y)] = (pos_x - 1, pos_y, self.grid_actives[(pos_x - 1, pos_y)])
        else:
            neighbors[(0, 0)] = (0, 0, 0)
            neighbors[(0, 0)] = (0, 0, 0)
            neighbors[(0, 0)] = (0, 0, 0)
            neighbors[(0, 0)] = (0, 0, 0)

        return neighbors

    def update_cell(self, pos_x, pos_y, new_val):
        self.grid_actives.update({(pos_x, pos_y): new_val})

    def render_grid(self, screen):
        for i in range(0, int(self.width/self.cell_size), 1):
            for j in range(0, int(self.height/self.cell_size), 1):
                if self.grid_actives[(i, j)] == 1:
                    pygame.draw.rect(screen, (200, 200, 200), (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))
                elif isinstance(self.grid_actives[(i, j)], Element.Element):
                    pygame.draw.rect(screen, self.grid_actives[(i, j)].colour, (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))



def fill_random(grid):
    for i in range(0, 64, 1):
        for j in range(0, 64, 1):
            if random.uniform(0, 1) > 0.5:
                grid.update_cell(i, j, 1)

    return grid


def game_of_life(grid, Screen_Size):
    new_grid = Grid(Screen_Size, Screen_Size, 8)
    new_grid.initiate_grid()

    '''
    I had an interesting bug when I just set new_grid equal to a copy of the grid being passed in, not sure what was 
    happening, but it filled the screen very quickly with maze like patterns, i suspect it was the same memory issue as
    with the 1D implementation 
    '''

    for i in range(0, 128, 1):
        for j in range(0, 128, 1):
            if grid.grid_actives[i, j] == 1:
                num_of_neighbours = grid.get_sum_of_neighbours_moore(i, j, 1)

                if num_of_neighbours == 2 or num_of_neighbours == 3:
                    new_grid.update_cell(i, j, 1)
                else:
                    new_grid.update_cell(i, j, 0)
            else:
                num_of_neighbours = grid.get_sum_of_neighbours_moore(i, j, 1)
                if num_of_neighbours == 3:
                    new_grid.update_cell(i, j, 1)
                pass

    return new_grid


def regions(grid):
    checked_coords = {}

    for i in range(0, 64, 1):
        for j in range(0, 64, 1):
            if (i, j) in checked_coords:
                pass
            elif grid.grid_actives[i, j] == 1:
                # new_group = {}

                color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                grid.update_cell(i, j, color)

                neighbors = grid.get_pos_of_neighbours_von(i, j, 1)
                checked_coords[(i, j)] = 'checked'
                queue = []

                for key in neighbors:
                    queue.append((neighbors[key][0], neighbors[key][1]))

                while len(queue) > 0:
                    if queue[0] in checked_coords:
                        pass
                    elif grid.grid_actives[queue[0]] == 0:
                        checked_coords[queue[0]] = 'checked'
                    else:
                        grid.update_cell(queue[0][0], queue[0][1], color)

                        neighbors = grid.get_pos_of_neighbours_von(queue[0][0], queue[0][1], 1)
                        checked_coords[queue[0]] = 'checked'

                        for key in neighbors:
                            queue.append((neighbors[key][0], neighbors[key][1]))

                    queue.pop(0)

            else:
                checked_coords[(i, j)] = 'checked'

    return grid
