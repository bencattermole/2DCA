import pygame
import Grid
import Element
import PlanetGen
import random

'''
The rules for falling sands

If the cell below a sand grain is empty, the sand grain moves to the empty cell (see (a)).
If the cell below a sand grain is full but the cell at bottom left or the cell at bottom right is free, the sand grain moves there (see (b)). If both are free, choose one randomly.
In the other cases, the sand grain does not move.
'''

Screen_Size = 1024
block_size = 16
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((Screen_Size, Screen_Size))
pygame.display.set_caption("2D Planets")

clock = pygame.time.Clock()


class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((64, 64, 16, 16))
        self.color = (255, 255, 255)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and (self.rect.left > 0):
            self.rect.move_ip(-16, 0)
        if key[pygame.K_RIGHT] and (self.rect.right < Screen_Size):
            self.rect.move_ip(16, 0)
        if key[pygame.K_UP] and (self.rect.top > 0):
            self.rect.move_ip(0, -16)
        if key[pygame.K_DOWN] and (self.rect.bottom < Screen_Size):
            self.rect.move_ip(0, 16)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


pygame.init()

player = Player()

grid = Grid.Grid(Screen_Size, Screen_Size, 8)
grid.initiate_grid()

# makes a line of stone
'''
I am not going to add the stone to the element list that I need to update as I dont think that I need to?
'''
for i in range(0, 128, 1):
    stone = Element.Element('stone', i, 125, (112, 112, 112))
    grid.update_cell(i, 125, stone)

for i in range(0, 128, 1):
    stone = Element.Element('stone', i, 3, (112, 112, 112))
    grid.update_cell(i, 3, stone)

for j in range(0, 128, 1):
    stone = Element.Element('stone', 125, j, (112, 112, 112))
    grid.update_cell(125, j, stone)

for j in range(0, 128, 1):
    stone = Element.Element('stone', 3, j, (112, 112, 112))
    grid.update_cell(3, j, stone)

'''
Uncomment the following for region generaiton
'''

# grid = Grid.fill_random(grid)
# grid = Grid.regions(grid)

running = True

Begin = False
held_mouse = False
brush = 0

ElementList = []

drawing = 'sand'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            held_mouse = not held_mouse
        if event.type == pygame.MOUSEBUTTONUP:
            held_mouse = not held_mouse
        if held_mouse:
            if drawing == 'stone':
                pos = pygame.mouse.get_pos()
                stone = Element.Element('stone', int(pos[0] / 8), int(pos[1] / 8), (112, 112, 112))
                grid.update_cell(int(pos[0] / 8), int(pos[1] / 8), stone)
            if drawing == 'sand':
                pos = pygame.mouse.get_pos()
                sand = Element.Solid('sand', int(pos[0] / 8), int(pos[1] / 8), (237, 204, 111), 1, 1)
                grid.update_cell(int(pos[0] / 8), int(pos[1] / 8), sand)
                ElementList.append(sand)
            if drawing == 'water':
                pos = pygame.mouse.get_pos()
                water = Element.Liquid('water', int(pos[0] / 8), int(pos[1] / 8), (20, 104, 250), 1)
                grid.update_cell(int(pos[0] / 8), int(pos[1] / 8), water)
                ElementList.append(water)
            if drawing == 'zero':
                pos = pygame.mouse.get_pos()
                grid.update_cell(int(pos[0] / 8), int(pos[1] / 8), 1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                Begin = not Begin
            if event.key == pygame.K_q:
                drawing = 'stone'
            if event.key == pygame.K_w:
                drawing = 'sand'
            if event.key == pygame.K_e:
                drawing = 'water'
            if event.key == pygame.K_r:
                drawing = 'zero'

    screen.fill((0, 0, 0))

    '''
    Uncomment out the below to draw a perfect circle,
    it will constantly draw before the game of life loop effectively placing it in every iteration. this leads to some 
    interesting symmetries

    grid = PlanetGen.CircleDraw(64, 64, 19, grid)
    #grid = PlanetGen.CircleDraw(64, 64, 32, grid)


    if Begin:
        grid = Grid.game_of_life(grid, Screen_Size)
    
    '''

    '''
    Falling sands part below this comment
    '''

    if Begin:
        if random.uniform(0, 1) > 0.5:
            sand = Element.Solid('sand', 64, 20, (237, 204, 111), 1, 1)
            ElementList.append(sand)

        if random.uniform(0, 1) > 0.7:
            water = Element.Liquid('water', 80, 20, (20, 104, 250), 1)
            ElementList.append(water)

       # grid = Element.falling_sands_iteration(grid, ElementList, Screen_Size)

    grid = Element.falling_sands_iteration(grid, ElementList, Screen_Size)

    grid.render_grid(screen)

    player.draw()
    player.handle_keys()

    pygame.display.update()

    clock.tick(30)
