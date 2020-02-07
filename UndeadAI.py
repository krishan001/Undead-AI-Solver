
from tracePath import createPaths
from bruteForce import randomBruteForce
import time
from displayGrid import printBoard
   
def readBoard(file, numLines, dim):
    # Read the board from a text file
    grid = [[]] * dim
    with open(file) as f:
        strings = [f.readline()[0:-1] for x in range(numLines)]
    for s in strings:
        # take the number visible in each path and remove them from the string
        [numGhosts, numVampires,numZombies] = map(int,s[:3])
        s = s[3:]
        vis = list(map(int,(s[:(dim*4)])))
        s = s[(dim*4):]
        # create grid from string
        for i in range(0,dim):
            grid[i] = list(s[:dim])
            s = s[dim:]

    
    return grid, vis, numGhosts, numVampires,numZombies

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

def labelPaths(matrix, dim):
    alph = "ABCDEFGHI"
    digits = "123456789"
    alph = alph[:dim]
    digits = digits[:dim]
    squares = cross(alph,digits)
    for i in range(0,dim):
        for j in range(0,dim):
            if matrix[i][j] == ".":
                matrix[i][j] = squares[i * dim + j]

    return matrix

def getLabelVisDict(vis,dim):
    downLabels = ["D1","D2","D3","D4","D5","D6","D7","D8", "D9"]
    leftLabels = ["L1","L2","L3","L4","L5","L6","L7","L8", "L9"]
    upLabels = ["U1","U2","U3","U4", "U5","U6","U7","U8", "U9"]
    rightLabels = ["R1","R2","R3","R4", "R5","R6","R7","R8", "R9"]
    downLabels = downLabels[:dim]
    leftLabels = leftLabels[:dim]
    upLabels = upLabels[:dim]
    rightLabels = rightLabels[:dim]
    labels = downLabels + leftLabels + upLabels +rightLabels
    
    return  dict(zip(labels, vis))

def getZeroPaths(pathDict, allPaths):
    l = []
    zeroPaths = []
    for label, vis in pathDict.items():
        if vis == 0:
            l.append(label)
    for key, value in allPaths.items():
        for e in l:
            if e == key:
                zeroPaths.append(value)
    print(l)
    zeroPaths = getLabelsFromZeroPaths(zeroPaths)
    return zeroPaths, l

def getLabelsFromZeroPaths(zeroPaths):
    zeroPaths = [item for sublist in zeroPaths for item in sublist]
    zeroPaths = list(dict.fromkeys(zeroPaths))
    if 'g' in zeroPaths:
        zeroPaths.remove('g')
    if 'v' in zeroPaths:
        zeroPaths.remove('v')
    if 'z' in zeroPaths:
        zeroPaths.remove('z')
    if '\\' in zeroPaths:
        zeroPaths.remove('\\')
    if '/' in zeroPaths:
        zeroPaths.remove('/')
    
    return zeroPaths

def beforeMirror(cell, allPaths, l):
    for e in l:
        bMirror = True
        for value in allPaths[e]:
            if value == '\\' or value =='/':
                bMirror = False
            if value == cell:
                return bMirror
    return bMirror


        



def zeroFill(matrix, dim,vis):
    matrix = labelPaths(matrix,dim)
    rp,lp,up,dp = createPaths(matrix)
    allPaths = {**rp, **lp, **up, **dp}

    pathDict = getLabelVisDict(vis,dim)
    zeroPaths, l = getZeroPaths(pathDict, allPaths)
    
    for i in range(0,dim):
        for j in range(0,dim):
            if matrix[i][j] in zeroPaths:
                # check if before mirror or after
                
                if beforeMirror(matrix[i][j], allPaths, l):
                    matrix[i][j] = 'g'
                elif not beforeMirror(matrix[i][j], allPaths, l):

                    matrix[i][j] = 'v'
            

    return(matrix)


def main():
    # define the dimentions of the board
    dim = 4
    matrix, vis, numGhosts, numVampires,numZombies = readBoard("board.txt", 1, dim)

    # Print original board
    printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)

    # Fill in the paths that have 0 visible
    matrix = zeroFill(matrix,dim,vis)
    printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
    # Time the solver
    startTime = time.perf_counter()
    solvedMatrix = randomBruteForce(matrix,vis, dim, numGhosts, numVampires,numZombies)
    timeTaken = time.perf_counter() - startTime
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
* then do depth first etc and record times
'''