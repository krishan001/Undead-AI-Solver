
from tracePath import createPaths
from bruteForce import randomBruteForce
import time
   
def readBoard(file, numLines, dim):
    # Read the board from a text file
    grid = [[]] * dim
    with open(file) as f:
        strings = [f.readline()[0:-1] for x in range(numLines)]
    for s in strings:
        # take the number visible in each path and remove them from the string
        [numGhosts, numVampires,numZombies] = map(int,s[:3])
        s = s[3:]

        vis = list(map(int,(s[:(dim**2)])))
        s = s[(dim**2):]
        # create grid from string
        for i in range(0,dim):
            grid[i] = list(s[:dim])
            s = s[dim:]

    
    return grid, vis, numGhosts, numVampires,numZombies
def uni(s):
    return chr(int(s,16))

def fancy_grid_line(start,norm,lcross,hcross,end):
      start,norm,lcross,hcross,end = ( uni(start),uni(norm), uni(lcross),uni(hcross),uni(end))
      return ( start + ((norm*3 + lcross)
                   + norm*3 + hcross)
                   + (norm*3 + lcross)
                   + norm*3  + end )

TOP_LINE       = fancy_grid_line( '2554', '2550', '2566', '2566', '2557' )
MID_LINE  = fancy_grid_line( '2560', '2550', '256c', '256c', '2563' )
BOTTOM_LINE    = fancy_grid_line( '255a', '2550', '2569', '2569', '255d' )

def printBoard(grid, vis, dim, numGhosts, numVampires,numZombies):
    # vertical bar
    dvbar = uni('2551')
    
    indent = "   "
    halfIndent = "  "
    print("Number of Ghosts: {} \nNumber of Vampires: {}\nNumber of Zombies: {}\n".format(numGhosts, numVampires, numZombies))
    print(indent, end="")
    # Print the number of visible monsters on the top
    for i in range(0,dim):
        print(halfIndent +str(vis[i])+ " ", end = "")
    print( "\n"+ indent + TOP_LINE )
    count = 0
    for row in grid:
        count +=1
        # Print the number of visible monsters on the left
        print( str(vis[count-1+dim*3])+ halfIndent + dvbar, end ="")
        for c in row:
            print(" " +c + " " + dvbar, end="")
        # Print the number of visible monsters on the right
        if count == 4:
            print(" " +str(vis[count-1+dim])+"\n" + indent+BOTTOM_LINE)
        else:
            print(" "+ str(vis[count-1+dim])+"\n" +indent+MID_LINE)
    print(indent, end = "")
    for i in range(0,dim):
        # Print the number of visible monsters on the bottom
        print(halfIndent +str(vis[i+dim*2])+ " ", end = "")
    print("\n")


def main():
    # define the dimentions of the board
    dim = 4
    matrix, vis, numGhosts, numVampires,numZombies = readBoard("board.txt", 1, dim)
    printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
    startTime = time.perf_counter()
    solvedMatrix = randomBruteForce(matrix,vis, dim, numGhosts, numVampires,numZombies)
    timeTaken = time.perf_counter() - startTime
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
* then do depth first etc and record times
'''