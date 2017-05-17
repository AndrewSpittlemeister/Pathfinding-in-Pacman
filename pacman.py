import pygame
from pacstructs import *
from pacfuncs import *
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

score = 0

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (608, 608)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pac-Man")

#Format Background and init cells data structure
background = pygame.image.load("gridbackground.png").convert()
coin = pygame.image.load("nomdot.png").convert()
coin.set_colorkey(BLACK)
cells = init_grid("gridbackground.png")

# Format font for score:
font = pygame.font.SysFont('Calibri', 20, True, False)

# Initialize sprites
pacman = PacMan()
pacman.rect.x = 9 * 32
pacman.rect.y = 15 * 32

INKY = Ghost("green")
INKY.rect.x = 8 * 32
INKY.rect.y = 9 * 32
INKY.gridloc = [8,9]

BLINKY = Ghost("red")
BLINKY.rect.x = 9 * 32
BLINKY.rect.y = 9 * 32
BLINKY.gridloc = [9,9]

CLYDE = Ghost("orange")
CLYDE.rect.x = 10 * 32
CLYDE.rect.y = 9 * 32
CLYDE.gridloc = [10,9]

framecount = 0
    
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Start game timer
start = time.time()

# For use when button is held down
buttonState = 'n'

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = time.time()
            print("Thanks for playing!")
            print("Your score was: " + str(score))
            print("Your time was: " + str(end - start) + " seconds")
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (pacman.dir == 'u') | (pacman.dir == 'd'):
                    # cannot change direction in this case or will run through wall
                    pacman.dir = pacman.dir
                elif cells[pacman.gridloc[0] - 1][pacman.gridloc[1]].traversable == True:
                    pacman.goal_cell = [pacman.gridloc[0]-1, pacman.gridloc[1]]
                    pacman.dir = 'l'
                    buttonState = 'l'
            elif event.key == pygame.K_RIGHT:
                if (pacman.dir == 'u') | (pacman.dir == 'd'):
                    # cannot change direction in this case or will run through wall
                    pacman.dir = pacman.dir
                elif cells[pacman.gridloc[0] + 1][pacman.gridloc[1]].traversable == True:
                    pacman.goal_cell = [pacman.gridloc[0] + 1, pacman.gridloc[1]]
                    pacman.dir = 'r'
                    buttonState = 'r'
            elif event.key == pygame.K_UP:
                if (pacman.dir == 'l') | (pacman.dir == 'r'):
                    # cannot change direction in this case or will run through wall
                    pacman.dir = pacman.dir
                elif cells[pacman.gridloc[0]][pacman.gridloc[1] - 1].traversable == True:
                    pacman.goal_cell = [pacman.gridloc[0], pacman.gridloc[1]-1]
                    pacman.dir = 'u'
                    buttonState = 'u'
            elif event.key == pygame.K_DOWN:
                if (pacman.dir == 'r') | (pacman.dir == 'l'):
                    # cannot change direction in this case or will run through wall
                    pacman.dir = pacman.dir
                elif cells[pacman.gridloc[0]][pacman.gridloc[1] + 1].traversable == True:
                    pacman.goal_cell = [pacman.gridloc[0], pacman.gridloc[1]+1]
                    pacman.dir = 'd'
                    buttonState = 'd'
            elif event.key == pygame.K_ESCAPE:
                end = time.time()
                print("Thanks for playing!")
                print("Your score was: " + str(score))
                print("Your time was: " + str(end - start) + " seconds")
                done =  True

 
        

    # --- Game logic should go here

    # Update Pacman Location
    pacman.update()
   # print(pacman.gridloc)
   # print(score)

    # Check if we picked up a new coin and update score if needed
    if cells[pacman.gridloc[0]][pacman.gridloc[1]].coin == True:
        cells[pacman.gridloc[0]][pacman.gridloc[1]].coin = False
        score += 1

    # update and format scoreboard
    score_text = "Score: " + str(score)
    text = font.render(score_text, True, WHITE)

    if score == 164:
        end = time.time()
        print("Thanks for playing")
        print("You got all the nomdots!")
        print("Your time was: " + str(end - start) + " seconds")
        pygame.quit()


    numExpanded = 0
    totalNodes = 0
    # Update Ghost Locations
    if framecount == 0:
        compTimeStart = time.time()
        INKY.goal_cell,numExpanded,totalNodes = aStarGhost(INKY, pacman, cells)
        compTimeEnd = time.time()
        print("Astar number of expanded Nodes: ", numExpanded)
        print("Astar number of total Nodes: ", totalNodes)
        print("Astar computation time: ", compTimeEnd - compTimeStart)

        compTimeStart = time.time()
        BLINKY.goal_cell, numExpanded, totalNodes = subGoalAStar(BLINKY, pacman, cells)
        compTimeEnd = time.time()
        print("Subgoal Astar number of expanded Nodes: ", numExpanded)
        print("Subgoal Astar number of total Nodes: ", totalNodes)
        print("Subgoal Astar computation time: ", compTimeEnd - compTimeStart)

        compTimeStart = time.time()
        CLYDE.goal_cell, numExpanded, totalNodes = BFS(CLYDE, pacman, cells)
        compTimeEnd = time.time()
        print("BFS number of expanded Nodes: ", numExpanded)
        print("BFS number of total Nodes: ", totalNodes)
        print("BFS computation time: ", compTimeEnd - compTimeStart)
        
        end = time.time()
    
    if INKY.goal_cell[0] < INKY.gridloc[0]:
        INKY.dir = "l"
    elif INKY.goal_cell[0] > INKY.gridloc[0]:
        INKY.dir = "r"
    elif INKY.goal_cell[1] < INKY.gridloc[1]:
        INKY.dir = "u"
    elif INKY.goal_cell[1] > INKY.gridloc[1]:
        INKY.dir = "d"
    INKY.update()

    if BLINKY.goal_cell[0] < BLINKY.gridloc[0]:
        BLINKY.dir = "l"
    elif BLINKY.goal_cell[0] > BLINKY.gridloc[0]:
        BLINKY.dir = "r"
    elif BLINKY.goal_cell[1] < BLINKY.gridloc[1]:
        BLINKY.dir = "u"
    elif BLINKY.goal_cell[1] > BLINKY.gridloc[1]:
        BLINKY.dir = "d"

    if end - start > 2:
        BLINKY.update()

    if CLYDE.goal_cell[0] < CLYDE.gridloc[0]:
        CLYDE.dir = "l"
    elif CLYDE.goal_cell[0] > CLYDE.gridloc[0]:
        CLYDE.dir = "r"
    elif CLYDE.goal_cell[1] < CLYDE.gridloc[1]:
        CLYDE.dir = "u"
    elif CLYDE.goal_cell[1] > CLYDE.gridloc[1]:
        CLYDE.dir = "d"

    if end - start > 3:
        CLYDE.update()

    # Check for collision with ghosts
    if checkCollissions(pacman, INKY, BLINKY, CLYDE) == -1:
        end = time.time()
        print("Thanks for playing")
        print("You got ", score, "nomdots.")
        print("Your time was: " + str(end - start) + " seconds")
        pygame.quit()
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background, [0,0])
    
    # --- Drawing code should go here

    screen.blit(text, [267, 10 * 32])
    
    for i in range(19):
        for j in range(19):
            if cells[i][j].coin:
                screen.blit(coin, [i * 32, j * 32])
    pacman.draw(screen)
    INKY.draw(screen)
    BLINKY.draw(screen)
    CLYDE.draw(screen)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 64 frames per second
    framecount = (framecount + 1) % 32
    clock.tick(64)
 
# Close the window and quit.
pygame.quit()
