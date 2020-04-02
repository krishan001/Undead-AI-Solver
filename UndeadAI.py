
from bruteForce import randomBruteForce
import time
from displayGrid import printBoard
from itertools import product
from copy import deepcopy

def readBoard(file, numLines):
    # Read the board from a text file
    l = []
    grid = [[]] * dim
    with open(file) as f:
        strings = [f.readline()[0:-1] for x in range(numLines)]


    for s in strings:
        # take the number visible in each path and remove them from the string
        monsters = s.split(",")
        numGhosts = int(monsters[0])
        numVampires = int(monsters[1])
        numZombies = int(monsters[2])
        s = monsters[3]
        # get the numbers of visible monsters fro each path
        vis = list(map(int,(s[:(dim*4)])))
        s = s[(dim*4):]
        # create grid from string
        for i in range(0,dim):
            grid[i] = list(s[:dim])
            s = s[dim:]
        l.append([grid, vis, numGhosts, numVampires,numZombies])

        grid = [[]] * dim
    # return newgrid, vis, numGhosts, numVampires,numZombies
    return l


def isSquare (matrix): #Check that it is a square matrix
    return all (len (row) == len (matrix) for row in matrix)

def createPaths(matrix):
    if isSquare(matrix): 
        dim = len(matrix)
    else:
        print("matrix is not square therefore invalid")
        exit()
    # Generate paths for all directions
    rp = rightPaths(matrix)
    lp = leftPaths(matrix)
    up = upPaths(matrix)
    dp = downPaths(matrix)

    return rp,lp,up,dp

def checkVisible(rp,lp,up,dp):
    foundVis = []
    for x in dp.values():
        foundVis.append(countVis(x))
    for x in lp.values():
        foundVis.append(countVis(x))
    for x in up.values():
        foundVis.append(countVis(x))
    for x in rp.values():
        foundVis.append(countVis(x))

    return foundVis == vis

def countVis(path):
    # Given a path, figure out how many monsters you can see
    pastMirror = False
    numVis = 0
    for x in path:
        if x == '/' or x == '\\':
            pastMirror = True
        if pastMirror == False and (x == 'v' or x == 'z'):
            numVis += 1
        if pastMirror == True and (x == 'g' or x == 'z'):
            numVis += 1
    
    return numVis

def leftPaths(matrix):
    # Generate left paths and add to dictionary
    paths = {}
    labels = ["L1", "L2", "L3", "L4", "L5","L6","L7"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix,dim-1, i, 3)
    return paths

def rightPaths(matrix):
    # Generate right paths and add to dictionary
    paths = {}
    labels = ["R1", "R2", "R3", "R4", "R5","R6","R7"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix, 0, i, 1)
    return paths

def upPaths(matrix):
    # Generate upwards paths and add to dictionary
    paths = {}
    labels = ["U1", "U2", "U3", "U4", "U5","U6","U7"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix, i, dim -1, 0)
    return paths

def downPaths(matrix):
    # Generate downwards paths and add to dictionary
    paths = {}
    labels = ["D1", "D2", "D3", "D4", "D5","D6","D7"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix, i, 0, 2)
    return paths

def tracePath(matrix, x, y, d):
    # For d: 0 = up, 1 = right, 2 = down, 3 = left
    path = []
    
    while(x < dim and y < dim and x >=0 and y>=0): # In the bounds of the matrix
        # if statements to figure out the new direction and x,y coords if the traversal hits a mirror
        # and call the recursive call

        # Turn to the right
        if (matrix[y][x] == "/" and d == 0) or (matrix[y][x] == "\\" and d == 2):
            
            path.append(matrix[y][x])
            d = 1
            x+=1
            path.extend(tracePath(matrix, x, y, d))
            return path

        # Turn upwards
        elif (matrix[y][x] == "/" and d == 1) or (matrix[y][x] == "\\" and d == 3):
            
            path.append(matrix[y][x])
            d = 0
            y-=1
            
            path.extend(tracePath(matrix, x, y, d))
            return path
        # Turn to the left
        elif (matrix[y][x] == "/" and d == 2) or (matrix[y][x] == "\\" and d == 0):
            
            path.append(matrix[y][x])
            d = 3
            x-=1
            path.extend(tracePath(matrix, x, y, d))
            return path
        # Turn downwards
        elif (matrix[y][x] == "/" and d == 3) or (matrix[y][x] == "\\" and d == 1):
            
            path.append(matrix[y][x])
            d = 2
            y+=1
            path.extend(tracePath(matrix, x, y, d))
            return path
        else:
            # If it doesn't hit a mirror then add it to the path
            path.append(matrix[y][x])
            if d == 0:
                y-=1
            if d == 1:
                x+=1
            if d == 2:
                y+=1
            if d == 3:
                x-=1
    return path

def checkSolved(matrix):
    rp,lp,up,dp = createPaths(matrix)
    solved = checkVisible(rp,lp,up,dp) and checkNumMonsters(matrix)
    # print(solved)
    return solved

def checkNumMonsters(matrix):
    solvedGhosts, solvedVamps, solvedZombies = countNumMonsters(matrix)
    return  solvedGhosts == numGhosts and solvedVamps == numVampires and solvedZombies == numZombies

def countNumMonsters(matrix):
    numG, numV, numZ = 0,0,0
    for row in matrix:
        for c in row:
            if c == "g":
                numG += 1
            if c == "v":
                numV += 1
            if c == "z":
                numZ += 1
    return numG, numV, numZ

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

def zeroFill(matrix):
    matrix = labelPaths(matrix)
    rp,lp,up,dp = createPaths(matrix)
    # merge all the dictionaries together
    allPaths = mergeDicts(rp,lp,up,dp)

    pathDict = getLabelVisDict()
    zeroPaths, l = getZeroPaths(pathDict, allPaths)
    for i in range(0,dim):
        for j in range(0,dim):
            if matrix[i][j] in zeroPaths:
                # check if before mirror or after
                if beforeMirror(matrix[i][j], allPaths, l) and matrix[i][j]!="\\" and matrix[i][j] != "/":
                    matrix[i][j] = 'g'
                elif not beforeMirror(matrix[i][j], allPaths, l)and matrix[i][j]!="\\" and matrix[i][j] != "/":
                    matrix[i][j] = 'v'
    return matrix

def beforeMirror(cell, allPaths, l):
    for e in l:
        bMirror = True
        for value in allPaths[e]:
            if value == '\\' or value =='/':
                bMirror = False
            if value == cell:
                return bMirror
    return bMirror

def labelPaths(matrix):
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

def getLabelVisDict():
    rightLabels, leftLabels, upLabels, downLabels = getLabels()
    labels = downLabels + leftLabels + upLabels +rightLabels
    return  dict(zip(labels, vis))

def getLabels():
    downLabels = ["D1","D2","D3","D4","D5","D6","D7"]
    leftLabels = ["L1","L2","L3","L4","L5","L6","L7"]
    upLabels = ["U1","U2","U3","U4", "U5","U6","U7"]
    rightLabels = ["R1","R2","R3","R4", "R5","R6","R7"]
    downLabels = downLabels[:dim]
    leftLabels = leftLabels[:dim]
    upLabels = upLabels[:dim]
    rightLabels = rightLabels[:dim]

    return rightLabels, leftLabels, upLabels, downLabels

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
    zeroPaths = getLabelsFromZeroPaths(zeroPaths)
    return zeroPaths, l

def getLabelsFromZeroPaths(zeroPaths):
    # flatten a 2D list into a 1D list
    zeroPaths = [item for sublist in zeroPaths for item in sublist]
    # get rid of repetitions
    zeroPaths = list(dict.fromkeys(zeroPaths))
    remove = ['g','v','z','\\','/']
    # remove pre filled squares
    for e in zeroPaths:
        if e in remove:
            zeroPaths.remove(e)
    return zeroPaths

def allPaths(label, path, unsolved):
    visDict = getLabelVisDict()
    # flag for loops
    loop = True
    # flag for if the value of a square is changed
    changed = False
    possible = ['g', 'v', 'z']
    possPaths = []
    ogPath = deepcopy(path)
    # get every combination of monsters for the number of unsolved squares in the path
    allPoss = list(set(product(list(set(possible)),repeat = unsolved)))
    # Find all the possible paths for a particular path
    for i in range(0,len(allPoss)):
        path = deepcopy(ogPath)
        for j in allPoss[i]:
            loop = True
            for k in range(0,len(path)):
                if isBlank(path[k]) and loop:
                    path[k] = j
                    changed = True
                    loop = False
                    break
        # Checks that the number visible is correct
        if countVis(path) == visDict[label] and changed:
            possPaths.append(path)

    return possPaths

# return if the square is blank
def isBlank(x):
    return x!= "g" and x!= "v" and  x != "z" and x != "\\" and x != "/"

# merge 4 dictionaries into one
def mergeDicts(d1,d2,d3,d4):
    mergedDict = {}
    mergedDict.update(d1)
    mergedDict.update(d2)
    mergedDict.update(d3)
    mergedDict.update(d4)
    return mergedDict

# get a dictionary of all the possible paths that could be in the grid
def possPaths(matrix):
    rp,lp,up,dp = createPaths(matrix)
    ap = mergeDicts(rp,lp,up,dp)
    possRight = allDirPaths(rp)
    possLeft = allDirPaths(lp)
    possUp = allDirPaths(up)
    possDown = allDirPaths(dp)
    allPossPathsDict = mergeDicts(possRight, possDown, possLeft,possUp)
    sortedDict = {}
    # Sort the keys of the dictionary by the length of the possible paths in ascending order
    tempDict = sorted(allPossPathsDict, key = lambda k: len(allPossPathsDict[k]))

    # add the keys and the values to a new sorted dictionary 
    for i in range(0,len(tempDict)):
        sortedDict[tempDict[i]] = allPossPathsDict[tempDict[i]]
    
    
    return sortedDict, ap


def numUnsolved(path):
    i = 0
    for e in path:
        if isBlank(e):
            i+=1
    return i

def allDirPaths(path):
    ap = {}
    for p in path:
        unsolved = numUnsolved(path[p])
        apVal = allPaths(p,path[p], unsolved)
        if len(apVal)!=0:
            ap[p] = apVal
    return ap

def fillPath(matrix, label, path, unfilledPath):
    # Actually fill the matrix with the path
    if (len(unfilledPath) == len(path)):
        for i in range(0,len(path)):
            if unfilledPath[i] != path[i] and isBlank(unfilledPath[i]):
                matrix = insertIntoMatrix(path[i], unfilledPath[i], matrix)
                # print(matrix)
        
    else:
        print("The path lengths don't match")
        exit()
    return matrix

def insertIntoMatrix (monster, position, matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if matrix[i][j] == position:
                matrix[i][j] = monster
    
    return matrix

    NODES_EXPANDED = 0

def getKeys(ap, possPathsDict):
    newKeys = []
    # get all of the path keys
    apKeys= [k for k in possPathsDict]
    # get a list of every combination of keys
    for i in range(0, len(apKeys)):
        for j in range(0, len(apKeys)):
            if (apKeys[i] != apKeys[j]):
                newKeys.append([apKeys[i],apKeys[j]])
    seen = set()

    # remove combinations if they are the same but in reverse
    [x for x in newKeys if tuple(x[::-1]) not in seen and not seen.add(tuple(x))]
    l = [list(x) for x in list(seen)]

    # create a dictionary of the keys that start and end the same paths
    samePaths = {}
    for k in l:
        if (ap[k[0]] == ap[k[1]][::-1]):
            samePaths[k[1]] = k[0]
            apKeys.remove(k[0])
    return apKeys,samePaths

def getValues(possPathsDict, pathKeys, samePaths):
    values = []
    temp = []
    # get the paths that for each label
    for k in possPathsDict:
        if k in pathKeys:
            oppositeKey = samePaths[k]
            for v in possPathsDict[k]:
                if (v[::-1] in possPathsDict[oppositeKey]):
                    temp.append(v)
            values.append(temp)
            temp = []
    return values

def fillOnePathLeft(matrix, pathLabels, pathValues, changed, ap):
    # if path values has an element with 1 possibility, fill it in
    length = len(pathValues)
    i = 0
    while (i < length):
        if (pathValues[i] and len(pathValues[i]) == 1):
            changed = True
            matrix = fillPath(matrix, pathLabels[i], pathValues[i][0], ap.get(pathLabels[i]))
            pathLabels.remove(pathLabels[i])
            pathValues.remove(pathValues[i])
            length = len(pathLabels)
            i -=1
        else:
            changed = False
            i +=1
    return matrix, pathLabels, pathValues, changed


NODES_EXPANDED = 0

def Dfs(matrix, node_limit = 100):
    if not ZF:
        matrix = labelPaths(matrix)
    changed = True
    while (changed == True):
        possPathsDict, ap = possPaths(matrix)
        pathLabels,samePaths = getKeys(ap, possPathsDict)
        pathValues =  getValues(possPathsDict, pathLabels, samePaths)
        # if there is only one possible path then fill it in
        matrix,pathLabels, pathValues, changed = fillOnePathLeft(matrix,pathLabels, pathValues, changed,ap)

    temp = deepcopy(matrix)
    ########################################
    temp = choosePaths(pathLabels, pathValues, matrix, ap, node_limit)

    # print(checkSolved(temp))

    if temp == False:
        print("Solution could not be found")
        return matrix
    ########################################
    return temp


def choosePaths(pathLabels, pathValues, matrix, ap, node_limit):
    global NODES_EXPANDED

    if NODES_EXPANDED == node_limit:
        return False
    NODES_EXPANDED += 1
    filled = deepcopy(matrix)

    #if the matrix is solved then return it
    if checkSolved(filled):
       return filled
    
    # if it is not solved but there are no more values to check, return false
    elif pathValues == [] or len(pathValues[0]) == 0:
        return False

    choices = pathValues[0]
    label = pathLabels[0]
    i = 0
    while (i < (len(choices))):
        choice = choices[i]        
        # reset filled in case it is False
        filled = deepcopy(matrix)

        # check if the path can be added
        fits = canAddPath(choice, label, filled)

        # Check for the correct number of monsters
        tempFilled = fillPath(filled, label, choice, ap.get(label))
        numG, numV, numZ = countNumMonsters(tempFilled)
        if (numG > numGhosts or numV > numVampires or numZ > numZombies):
            fits = False
        
        # if it is a valid path
        if fits and len(pathValues[0]) > 0:
            # remove the current choice
            pathValues[0].remove(choice)
            
            # make the recursive call
            filled = choosePaths(pathLabels[1:], pathValues[1:], tempFilled, ap, node_limit)
            if i > 0:
                i-=1 
            if (filled != False):
                return filled
            
        else:
            i+=1
    return False


def canAddPath(choice, key, matrix):
    possPathsDict, _ = possPaths(matrix)
    if possPathsDict.get(key) != None and choice in possPathsDict.get(key):
        return True
    else:
        return False
    

def fullBoard(matrix):
    full = True
    for i in range (0,len(matrix)):
        for j in range(0,len(matrix)):
            if isBlank(matrix[i][j]):
                full = False
                break
    return full

numGhosts, numVampires,numZombies = 0,0,0
dim = 4
vis = []
ZF = True

def main():
    global numGhosts, numVampires,numZombies, vis

    # define the dimentions of the board
    #read the board from a file
    try:
        l = readBoard("4x4Easy.txt", 10)
    except:
        print("Invalid file")
        exit()


    for i in range(0,len(l)):
        print("\n")
        matrix, vis,numGhosts,numVampires,numZombies = l[i]
   
        # Print original board
        # printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
        # Fill in the paths that have 0 visible
        if ZF:
            matrix = zeroFill(matrix)
            # printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
        
        ######################################################################################
        # Time the solver
        startTime = time.perf_counter()
        # solvedMatrix = Dfs(matrix)
        try:
            solvedMatrix = Dfs(matrix)
            
        except:
            print("Invalid Board")
            exit()
            
        print(i+1, checkSolved(solvedMatrix))
    
        # solvedMatrix = randomBruteForce(matrix,vis, dim, numGhosts, numVampires,numZombies)
        timeTaken = time.perf_counter() - startTime
        ######################################################################################

        # Print solved board
        # printBoard(solvedMatrix,vis, dim, numGhosts, numVampires,numZombies)
        print("took  {0:.5f} seconds\n\n".format(timeTaken))


    
if __name__ == "__main__":
    main()

