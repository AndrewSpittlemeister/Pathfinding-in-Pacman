from pacstructs import *
from PIL import Image
from pprint import pprint

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def init_grid(file):
    bc = Image.open(file)
    pix = bc.load()
    bc.close()

    cols = 19
    rows = 19
    cells = [[GridCell() for j in range(cols)] for i in range(rows)]

    # note in array[][] the first number stands for x val and second number
    # stands for the y value

    for x in range(19):
        for y in range(19):
            cells[x][y].gridloc = [x, y]
            cells[x][y].pixelloc = [x * 32, y * 32]
            if pix[x * 32, y * 32] == BLACK:
                cells[x][y].traversable = True
                cells[x][y].coin = True
    cells[8][9].coin = False
    cells[9][9].coin = False
    cells[10][9].coin = False
    cells[9][8].coin = False
    cells[0][7].coin = False
    cells[1][7].coin = False
    cells[2][7].coin = False
    cells[0][11].coin = False
    cells[1][11].coin = False
    cells[2][11].coin = False
    cells[16][7].coin = False
    cells[17][7].coin = False
    cells[18][7].coin = False
    cells[16][11].coin = False
    cells[17][11].coin = False
    cells[18][11].coin = False
    
    return cells
            
                
def colorTraversable(screen, cells):
    for x in range(19):
        for y in range(19):
            if cells[x][y].traversable == True:
                pygame.draw.rect(screen, RED, [x * 32, y * 32, 32, 32])
                
def checkCollissions(pacman, INKY, BLINKY, CLYDE):
    if pacman.gridloc == INKY.gridloc:
        return -1
    if pacman.gridloc == BLINKY.gridloc:
        return -1
    if pacman.gridloc == CLYDE.gridloc:
        return -1



def aStarGhost(ghost, pac, cells):
    # All costs for movement from one cell to an adjacent traversable cell is 1.
    # All costs for movement from one cell to an adjacent non-traversable
    #   cell is infinity.
    # Will be using the manhattan distance for heuristics
    
    inf = float("inf")
    Closed = []
    Open = []
    Open.append(SearchNode(ghost.gridloc))
    # open list now contains the start node
    
    goalNode = SearchNode(pac.gridloc)
    # goalNode is now a SearchNode object with the correct goal gridlocation field

    while len(Open) > 0:

        distance = 0
        index = 0
        expandingNode = Open[0]
        for i in range(len(Open)):
            if expandingNode.f > Open[i].f:
                expandingNode = Open[i]
                index = i

        Closed.append(Open.pop(index))

        #print(expandingNode.gridloc)
        if expandingNode.gridloc == goalNode.gridloc:
            # then we have found the goal node
            goalNode = expandingNode
            break
            
        expandingNodeX = expandingNode.gridloc[0]
        expandingNodeY = expandingNode.gridloc[1]

        # compute child node cost and f values
        
        left = SearchNode([expandingNodeX - 1,expandingNodeY], expandingNode)
        
        right = SearchNode([expandingNodeX + 1,expandingNodeY], expandingNode)
        
        up = SearchNode([expandingNodeX,expandingNodeY - 1], expandingNode)
        
        down = SearchNode([expandingNodeX,expandingNodeY + 1], expandingNode)

        rightbool = True
        leftbool = True
        upbool = True
        downbool = True
        for i in Closed:
            if i.gridloc == left.gridloc:
                leftbool = False
            if i.gridloc == right.gridloc:
                rightbool = False
            if i.gridloc == up.gridloc:
                upbool = False
            if i.gridloc == down.gridloc:
                downbool = False

        if rightbool:
            if cells[right.gridloc[0]][right.gridloc[1]].traversable == False:
                right.g = inf
                right.f = inf
            else:
                right.g = right.parent.g + 1
                distance = abs(goalNode.gridloc[0] - right.gridloc[0]) + abs(goalNode.gridloc[1] - right.gridloc[1])
                right.f = right.g + distance
            Open.append(right)
        if leftbool:
            if cells[left.gridloc[0]][left.gridloc[1]].traversable == False:
                left.g = inf
                left.f = inf
            else:
                left.g = left.parent.g + 1
                distance = abs(goalNode.gridloc[0] - left.gridloc[0]) + abs(goalNode.gridloc[1] - left.gridloc[1])
                left.f = left.g + distance
            Open.append(left)
        if upbool:
            if cells[up.gridloc[0]][up.gridloc[1]].traversable == False:
                up.g = inf
                up.f = inf
            else:
                up.g = up.parent.g + 1
                distance = abs(goalNode.gridloc[0] - up.gridloc[0]) + abs(goalNode.gridloc[1] - up.gridloc[1])
                up.f = up.g + distance
            Open.append(up)
        if downbool:
            if cells[down.gridloc[0]][down.gridloc[1]].traversable == False:
                down.g = inf
                down.f = inf
            else:
                down.g = down.parent.g + 1
                distance = abs(goalNode.gridloc[0] - down.gridloc[0]) + abs(goalNode.gridloc[1] - down.gridloc[1])
                down.f = down.g + distance
            Open.append(down)

    # now goal node should have parent node that is on the path.
    
    node1 = goalNode
    node2 = goalNode

    while node1.gridloc != ghost.gridloc:
        node2 = node1
        node1 = node1.parent

    return node2.gridloc, len(Closed), len(Closed) + len(Open)


def BFS(ghost, pac, cells):
    # All costs for movement from one cell to an adjacent traversable cell is 1.
    # All costs for movement from one cell to an adjacent non-traversable
    #   cell is infinity.
    # Will be using the manhattan distance for heuristics
    
    inf = float("inf")
    Closed = []
    Open = []
    Open.append(SearchNode(ghost.gridloc))
    # open list now contains the start node
    
    goalNode = SearchNode(pac.gridloc)
    # goalNode is now a SearchNode object with the correct goal gridlocation field

    while len(Open) > 0:

        distance = 0
        index = 0
        expandingNode = Open[0]
        for i in range(len(Open)):
            if expandingNode.f > Open[i].f:
                expandingNode = Open[i]
                index = i

        Closed.append(Open.pop(index))

        #print(expandingNode.gridloc)
        if expandingNode.gridloc == goalNode.gridloc:
            # then we have found the goal node
            goalNode = expandingNode
            break
            
        expandingNodeX = expandingNode.gridloc[0]
        expandingNodeY = expandingNode.gridloc[1]

        # compute child node cost and f values
        
        left = SearchNode([expandingNodeX - 1,expandingNodeY], expandingNode)
        
        right = SearchNode([expandingNodeX + 1,expandingNodeY], expandingNode)
        
        up = SearchNode([expandingNodeX,expandingNodeY - 1], expandingNode)
        
        down = SearchNode([expandingNodeX,expandingNodeY + 1], expandingNode)

        rightbool = True
        leftbool = True
        upbool = True
        downbool = True
        for i in Closed:
            if i.gridloc == left.gridloc:
                leftbool = False
            if i.gridloc == right.gridloc:
                rightbool = False
            if i.gridloc == up.gridloc:
                upbool = False
            if i.gridloc == down.gridloc:
                downbool = False

        if rightbool:
            if cells[right.gridloc[0]][right.gridloc[1]].traversable == False:
                right.g = inf
                right.f = inf
            else:
                right.g = right.parent.g + 1
                right.f = right.g
            Open.append(right)
        if leftbool:
            if cells[left.gridloc[0]][left.gridloc[1]].traversable == False:
                left.g = inf
                left.f = inf
            else:
                left.g = left.parent.g + 1
                left.f = left.g
            Open.append(left)
        if upbool:
            if cells[up.gridloc[0]][up.gridloc[1]].traversable == False:
                up.g = inf
                up.f = inf
            else:
                up.g = up.parent.g + 1
                up.f = up.g
            Open.append(up)
        if downbool:
            if cells[down.gridloc[0]][down.gridloc[1]].traversable == False:
                down.g = inf
                down.f = inf
            else:
                down.g = down.parent.g + 1
                down.f = down.g
            Open.append(down)

    # now goal node should have parent node that is on the path.
    
    node1 = goalNode
    node2 = goalNode

    while node1.gridloc != ghost.gridloc:
        node2 = node1
        node1 = node1.parent

    return node2.gridloc, len(Closed), len(Closed) + len(Open)


def subGoalAStar(ghost, pac, cells):
    # All costs for movement from one cell to an adjacent traversable cell is 1.
    # All costs for movement from one cell to an adjacent non-traversable
    #   cell is infinity.
    # Will be using the manhattan distance for heuristics
    
    inf = float("inf")
    Closed = []
    Open = []
    Open.append(SearchNode(ghost.gridloc))
    # open list now contains the start node
    
    goalNode = SearchNode(pac.gridloc)
    # goalNode is now a SearchNode object with the correct goal gridlocation field

    counter = 0

    while len(Open) > 0:
        counter = counter + 1
        distance = 0
        index = 0
        expandingNode = Open[0]
        for i in range(len(Open)):
            if expandingNode.f > Open[i].f:
                expandingNode = Open[i]
                index = i

        Closed.append(Open.pop(index))

        #print(expandingNode.gridloc)
        if expandingNode.gridloc == goalNode.gridloc:
            # then we have found the goal node
            goalNode = expandingNode
            break
        elif counter == 39:
            goalNode = expandingNode
            break
                    
                
        expandingNodeX = expandingNode.gridloc[0]
        expandingNodeY = expandingNode.gridloc[1]

        # compute child node cost and f values
        
        left = SearchNode([expandingNodeX - 1,expandingNodeY], expandingNode)
        
        right = SearchNode([expandingNodeX + 1,expandingNodeY], expandingNode)
        
        up = SearchNode([expandingNodeX,expandingNodeY - 1], expandingNode)
        
        down = SearchNode([expandingNodeX,expandingNodeY + 1], expandingNode)

        rightbool = True
        leftbool = True
        upbool = True
        downbool = True
        for i in Closed:
            if i.gridloc == left.gridloc:
                leftbool = False
            if i.gridloc == right.gridloc:
                rightbool = False
            if i.gridloc == up.gridloc:
                upbool = False
            if i.gridloc == down.gridloc:
                downbool = False

        if rightbool:
            if cells[right.gridloc[0]][right.gridloc[1]].traversable == False:
                right.g = inf
                right.f = inf
            else:
                right.g = right.parent.g + 1
                distance = abs(goalNode.gridloc[0] - right.gridloc[0]) + abs(goalNode.gridloc[1] - right.gridloc[1])
                right.f = right.g + distance
            Open.append(right)
        if leftbool:
            if cells[left.gridloc[0]][left.gridloc[1]].traversable == False:
                left.g = inf
                left.f = inf
            else:
                left.g = left.parent.g + 1
                distance = abs(goalNode.gridloc[0] - left.gridloc[0]) + abs(goalNode.gridloc[1] - left.gridloc[1])
                left.f = left.g + distance
            Open.append(left)
        if upbool:
            if cells[up.gridloc[0]][up.gridloc[1]].traversable == False:
                up.g = inf
                up.f = inf
            else:
                up.g = up.parent.g + 1
                distance = abs(goalNode.gridloc[0] - up.gridloc[0]) + abs(goalNode.gridloc[1] - up.gridloc[1])
                up.f = up.g + distance
            Open.append(up)
        if downbool:
            if cells[down.gridloc[0]][down.gridloc[1]].traversable == False:
                down.g = inf
                down.f = inf
            else:
                down.g = down.parent.g + 1
                distance = abs(goalNode.gridloc[0] - down.gridloc[0]) + abs(goalNode.gridloc[1] - down.gridloc[1])
                down.f = down.g + distance
            Open.append(down)

    # now goal node should have parent node that is on the path.
    
    node1 = goalNode
    node2 = goalNode

    while node1.gridloc != ghost.gridloc:
        node2 = node1
        node1 = node1.parent

    return node2.gridloc, len(Closed), len(Closed) + len(Open)


        
        
    
            
        
    
    
