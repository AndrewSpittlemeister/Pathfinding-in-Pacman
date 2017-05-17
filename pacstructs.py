import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class SearchNode():
    """ This isa clas that holds info of a node of a state-space. """
    def __init__(self, location = None, parent = None):
        self.gridloc = location
        self.f = 0
        self.g = 0
        self.parent = parent

class GridCell():
    """ This is a class that holds info of a cell in the map. """
    def __init__(self):
        self.gridloc = [0,0]
        self.pixelloc = [0,0]
        self.traversable = False
        self.coin = False
        

class PacMan(pygame.sprite.Sprite):
    """ This is a class that holds info on the Pac-Man Sprite. """
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pacmanright.png").convert()

        # below we map a rectangle to this sprite to use for movement control
        # we can move the sprite by setting PacMan.rect.x adn PacmMan.rect.y
        self.rect = self.image.get_rect()

        # coins represents how many coins have been collected by pacman
        self.coins = 0

        # this is the location of pacman on the grid
        self.gridloc = [0,0]

        # used to set the goal grid location and to check if there
        self.goal_cell = [9, 15]

        # used to define current direction of pacman
        # 'r' = right
        # 'l' = left
        # 'u' = up
        # 'd' = down
        # 'n' = no movement at this time
        self.dir = "n"

    def update(self):

        if self.dir == 'r':
            self.rect.x += 1
        elif self.dir == 'l':
            self.rect.x += -1
        elif self.dir == 'u':
            self.rect.y += -1
        elif self.dir == 'd':
            self.rect.y += 1

        # now need to check if we have hit our goal grid location
        if (self.goal_cell[0] * 32 == self.rect.x) & (self.goal_cell[1] * 32 == self.rect.y):
            # if we have met this criteria we can
            # turn off movement until user press arrow key again
            self.dir = 'n'

            # update current grid location
            self.gridloc = self.goal_cell

    def draw(self, screen):
        if self.dir == 'r': # moving right
            self.image = pygame.image.load("pacmanright.png").convert()
        elif self.dir == 'l': # moving left
            self.image = pygame.image.load("pacmanleft.png").convert()
        elif self.dir == 'd': # moving down
            self.image = pygame.image.load("pacmandown.png").convert()
        elif self.dir == 'u': # moving up
            self.image = pygame.image.load("pacmanup.png").convert()
        screen.blit(self.image, [self.rect.x, self.rect.y])
        

class Ghost(pygame.sprite.Sprite):
    """ This is a class that holds info on a Ghost Sprite. """


    def __init__(self, color):
        super().__init__()
        if color == "orange":
            self.image = pygame.image.load("OrangeGhost.png").convert()
            self.image.set_colorkey(WHITE)
        elif color == "red":
            self.image = pygame.image.load("RedGhost.png").convert()
            self.image.set_colorkey(WHITE)
        elif color == "green":
            self.image = pygame.image.load("GreenGhost.png").convert()
            self.image.set_colorkey(WHITE)
            
        self.rect = self.image.get_rect()

        # is the current location of the ghost on the grid.
        self.gridloc = [0,0]

        # used to set the goal grid location and to check if there
        self.goal_cell = [9, 15]

        # used to define current direction of the Ghost.
        # 'r' = right
        # 'l' = left
        # 'u' = up
        # 'd' = down
        # 'n' = no movement at this time
        self.dir = "n"


    def update(self):
        if self.dir == 'r':
            self.rect.x += 1
        elif self.dir == 'l':
            self.rect.x += -1
        elif self.dir == 'u':
            self.rect.y += -1
        elif self.dir == 'd':
            self.rect.y += 1

        # now need to check if we have hit our goal grid location
        if (self.goal_cell[0] * 32 == self.rect.x) & (self.goal_cell[1] * 32 == self.rect.y):
            # if we have met this criteria we can
            # turn off movement until user press arrow key again
            self.dir = 'n'

            # update current grid location
            self.gridloc = self.goal_cell
            
    def draw(self, screen):
        screen.blit(self.image, [self.rect.x, self.rect.y])      
