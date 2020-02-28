
from itertools import product
from copy import deepcopy
from zeroFill import getLabelVisDict
from tracePath import countVis, createPaths, checkSolved, checkNumMonsters
from displayGrid import printBoard

def allPaths(label, path, unsolved, vis, dim):
    visDict = getLabelVisDict(vis,dim)
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
def possPaths(matrix, vis, dim):
    rp,lp,up,dp = createPaths(matrix)
    ap = mergeDicts(rp,lp,up,dp)
    possRight = allDirPaths(rp,vis,dim)
    possLeft = allDirPaths(lp,vis,dim)
    possUp = allDirPaths(up,vis,dim)
    possDown = allDirPaths(dp,vis,dim)
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

def allDirPaths(path, vis, dim):
    ap = {}
    for p in path:
        unsolved = numUnsolved(path[p])
        apVal = allPaths(p,path[p], unsolved, vis, dim)
        if len(apVal)!=0:
            ap[p] = apVal
    return ap

def fillPath(matrix, label, path, unfilledPath):
    # Actually fill the matrix with the path
    print("filling path: ", label)
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
    
def Dfs(matrix, vis, dim, totalNumGhosts, totalNumVampires,totalNumZombies):
    printBoard(matrix,vis, dim, totalNumGhosts, totalNumVampires,totalNumZombies)
    possPathsDict, ap = possPaths(matrix, vis, dim)
    matrix = fillOnePathLeft(matrix,possPathsDict, ap)
    temp = deepcopy(matrix)
    for k in possPathsDict:
        for p in possPathsDict.get(k):
            temp = fillPath(temp,k,p, ap.get(k))
            numG, numV, numZ = countNumMonsters(temp)
            if (numG <= totalNumGhosts and numV <= totalNumVampires and numZ <= totalNumZombies):
                return Dfs(temp,vis, dim, totalNumGhosts, totalNumVampires,totalNumZombies)
    matrix = deepcopy(temp)
    return matrix

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