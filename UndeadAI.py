
from allPaths import Dfs
from bruteForce import randomBruteForce
import time
from displayGrid import printBoard
from zeroFill import zeroFill
def readBoard(file, numLines, dim):
    # Read the board from a text file
    grid = [[]] * dim
    with open(file) as f:
        strings = [f.readline()[0:-1] for x in range(numLines)]
    for s in strings:
        # take the number visible in each path and remove them from the string
        [numGhosts, numVampires,numZombies] = map(int,s[:3])
        s = s[3:]
        # get the numbers of visible monsters fro each path
        vis = list(map(int,(s[:(dim*4)])))
        s = s[(dim*4):]
        # create grid from string
        for i in range(0,dim):
            grid[i] = list(s[:dim])
            s = s[dim:]

    
    return grid, vis, numGhosts, numVampires,numZombies


numGhosts, numVampires,numZombies = 0,0,0
def main():
    global numGhosts, numVampires,numZombies
    # define the dimentions of the board
    dim = 5
    #read the board from a file
    matrix, vis, numGhosts, numVampires,numZombies = readBoard("board.txt", 1, dim)
    # Print original board
    printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
    # Fill in the paths that have 0 visible
    matrix = zeroFill(matrix,dim,vis)
    printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
    # printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
    
    ######################################################################################
    # Time the solver
    startTime = time.perf_counter()
    solvedMatrix = Dfs(matrix,vis, dim, numGhosts, numVampires,numZombies)
    # solvedMatrix = randomBruteForce(matrix,vis, dim, numGhosts, numVampires,numZombies)
    timeTaken = time.perf_counter() - startTime
    ######################################################################################

    # Print solved board
    printBoard(solvedMatrix,vis, dim, numGhosts, numVampires,numZombies)
    print("took  {0:.3f} seconds".format(timeTaken))
    
if __name__ == "__main__":
    main()



'''
TODO:
* Create test file
* Object for each square with value so can cross reference across paths
* fill in board with brute force
* check solved
* record time for solve
* then do depth first etc afillOnePathLeftmes
* Solve paths and if there is only one possible path then solve it.
* potentially zero sum
'''