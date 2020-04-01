
# from allPaths import Dfs
from bruteForce import randomBruteForce
import time
from displayGrid import printBoard
# from tracePath import countVis, createPaths, checkSolved, checkNumMonsters
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
        [numGhosts, numVampires,numZombies] = map(int,s[:3])
        s = s[3:]
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
    # print("Paths view the correct number:", foundVis == vis)
    # if foundVis == vis:
        # print("Right paths: ",rp,"\n")
        # print("Left paths: ",lp,"\n")
        # print("Upwards paths: ", up, "\n")
        # print("D1 paths: ", dp["D1"],"\n")
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
    labels = ["L1", "L2", "L3", "L4", "L5"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix,dim-1, i, 3)
    return paths

def rightPaths(matrix):
    # Generate right paths and add to dictionary
    paths = {}
    labels = ["R1", "R2", "R3", "R4", "R5"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix, 0, i, 1)
    return paths

def upPaths(matrix):
    # Generate upwards paths and add to dictionary
    paths = {}
    labels = ["U1", "U2", "U3", "U4", "U5"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix, i, dim -1, 0)
    return paths

def downPaths(matrix):
    # Generate downwards paths and add to dictionary
    paths = {}
    labels = ["D1", "D2", "D3", "D4", "D5"]
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
    
def fillOnePathLeft(matrix, pathDict, allUnfilledPaths):
    for k in pathDict:
        if (len(pathDict[k]) == 1):
            matrix = fillPath(matrix,k,pathDict[k][0], allUnfilledPaths[k])
    return matrix

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
    # print("filling path: ", label)
    # print("matrix: ", matrix)
    # print("label: ", label)
    # print("path: ", path)
    # print("Unfilled: ", unfilledPath)
    if (len(unfilledPath) == len(path)):
        for i in range(0,len(path)):
            if unfilledPath[i] != path[i] and isBlank(unfilledPath[i]):
                matrix = insertIntoMatrix(path[i], unfilledPath[i], matrix)
                # print(matrix)
        
    else:
        print("The path lengths don't match")
        exit()
    # print("\n\n\n")
    return matrix

def insertIntoMatrix (monster, position, matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if matrix[i][j] == position:
                matrix[i][j] = monster
    
    return matrix
    
def Dfs(matrix):
    temp = deepcopy(matrix)
    changed = True
    while (changed == True):
        possPathsDict, ap = possPaths(matrix)
        
        pathKeys= [k for k in possPathsDict]
        pathKeys,samePaths = removeDuplicateKeys(pathKeys,ap, possPathsDict)
        pathValues =  getValues(possPathsDict, pathKeys, samePaths)
        # print("Path values: ", pathValues[2])

        # if path values has an element with 1 possibility, fill it in
        length = len(pathValues)
        i = 0
        while (i < length):
            if (pathValues[i] and len(pathValues[i]) == 1):
                changed = True
                matrix = fillPath(matrix, pathKeys[i], pathValues[i][0], ap.get(pathKeys[i]))
                pathKeys.remove(pathKeys[i])
                pathValues.remove(pathValues[i])
                length = len(pathKeys)
                i -=1
            else:
                changed = False
                i +=1

    ########################################
    temp = choosePaths(pathKeys, pathValues, matrix, ap)
    # print(checkSolved(temp))

    if temp == False:
        return matrix
    ########################################
    return temp

def removeDuplicateKeys(pathKeys, ap, possPathsDict):
    newKeys = []
    apKeys= [k for k in possPathsDict]
    for i in range(0, len(apKeys)):
        for j in range(0, len(apKeys)):
            if (apKeys[i] != apKeys[j]):
                newKeys.append([apKeys[i],apKeys[j]])
    seen = set()
    [x for x in newKeys if tuple(x[::-1]) not in seen and not seen.add(tuple(x))]
    l = [list(x) for x in list(seen)]
    samePaths = {}
    for k in l:
        if (ap[k[0]] == ap[k[1]][::-1]):
            samePaths[k[1]] = k[0]
            apKeys.remove(k[0])
    return apKeys,samePaths

def getValues(possPathsDict, pathKeys, samePaths):
    values = []
    temp = []
    for k in possPathsDict:
        if k in pathKeys:
            oppositeKey = samePaths[k]
            for v in possPathsDict[k]:
                if (v[::-1] in possPathsDict[oppositeKey]):
                    temp.append(v)
            values.append(temp)
            temp = []
    return values

def choosePaths(pathKeys, pathValues, matrix, ap):
    # print("\n\n")
    # print("keys",pathKeys)
    filled = deepcopy(matrix)

    if(checkSolved(matrix)):
        return filled

    elif pathValues == []:
        return False

    choices = pathValues[0]
    if len(choices) == 0:
        return False
    label = pathKeys[0]
    # print("length of choices:", label, len(choices))
    # print("choices", choices)
    i = 0
    while (i < (len(choices))):
        choice = choices[i]
        # print(label)
        filled = deepcopy(matrix)
        fits = canAddPath(choice, label, filled)
        # Check for the correct number of monsters
        tempFilled = fillPath(filled, label, choice, ap.get(label))
        # printBoard(tempFilled,vis,dim,numGhosts,numVampires, numZombies)
        numG, numV, numZ = countNumMonsters(tempFilled)

        if (numG > numGhosts or numV > numVampires or numZ > numZombies):
            # print("Too many monsters")
            fits = False

        if (fits and len(pathValues[0]) > 0):
            # print("filling:", choice, label)

            pathValues[0].remove(choice)
            filled = choosePaths(pathKeys[1:], pathValues[1:], tempFilled, ap)
            if i > 0:
                i-=1  
            
            if (filled != False):
                return filled
        else:
            # print(i)
            i+=1
            # print(choice, "Doesn't fit\n")

    if (filled != False):
        matrix = deepcopy(filled)
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
def main():
    global numGhosts, numVampires,numZombies, vis

    # define the dimentions of the board
    #read the board from a file
    l = readBoard("4x4.txt", 4)
    # print(l[0])

    # matrix, vis, numGhosts, numVampires,numZombies = l

    for i in range(0,len(l)):
        matrix = l[i][0]
        vis = l[i][1]
        numGhosts = l[i][2]
        numVampires = l[i][3]
        numZombies = l[i][4]
        # Print original board
        # printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
        # Fill in the paths that have 0 visible
        matrix = zeroFill(matrix)
        # printBoard(matrix,vis, dim, numGhosts, numVampires,numZombies)
        
        ######################################################################################
        # Time the solver
        startTime = time.perf_counter()

        solvedMatrix = Dfs(matrix)
        print(checkSolved(solvedMatrix))
    
        # solvedMatrix = randomBruteForce(matrix,vis, dim, numGhosts, numVampires,numZombies)
        timeTaken = time.perf_counter() - startTime
        ######################################################################################

        # Print solved board
        printBoard(solvedMatrix,vis, dim, numGhosts, numVampires,numZombies)
        print("took  {0:.5f} seconds\n\n".format(timeTaken))


    
if __name__ == "__main__":
    main()

