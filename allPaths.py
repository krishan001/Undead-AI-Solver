
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
    
def Dfs(matrix, vis, dim, totalNumGhosts, totalNumVampires,totalNumZombies):
    # printBoard(matrix,vis, dim, totalNumGhosts, totalNumVampires,totalNumZombies)
    temp = deepcopy(matrix)
    changed = True
    while (changed == True):
        possPathsDict, ap = possPaths(matrix, vis, dim)
        
        pathKeys= [k for k in possPathsDict]
        pathKeys,samePaths = removeDuplicateKeys(pathKeys,ap, possPathsDict)
        pathValues =  getValues(possPathsDict, pathKeys, samePaths)#

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

    loop = True
    # while (loop):
    #     temp = choosePaths(pathKeys, pathValues, matrix, vis, dim, ap, totalNumGhosts, totalNumVampires,totalNumZombies)
    #     if (temp != False):
    #         if (checkSolved(temp, vis, totalNumGhosts, totalNumVampires,totalNumZombies)):
    #             print(checkSolved(temp, vis, totalNumGhosts, totalNumVampires,totalNumZombies))
    #             loop = False
    #             return temp
    #         else:
    #             temp = deepcopy(matrix)
    ########################################
    temp = choosePaths(pathKeys, pathValues, matrix, vis, dim, ap, totalNumGhosts, totalNumVampires,totalNumZombies)

    ########################################
    # print("No solution found")
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

def choosePaths(pathKeys, pathValues, matrix, vis, dim, ap, totalNumGhosts, totalNumVampires,totalNumZombies):
    printBoard(matrix,vis, dim, totalNumGhosts, totalNumVampires,totalNumZombies)
    print("\n\n")
    print("keys",pathKeys)
    filled = deepcopy(matrix)

    if (pathValues == [] or checkSolved(matrix, vis, totalNumGhosts, totalNumVampires,totalNumZombies)):
        print("====================================")
        printBoard(matrix,vis, dim, totalNumGhosts, totalNumVampires,totalNumZombies)
        print("====================================")
        
        return filled

    choices = pathValues[0]
    if len(choices) == 0:
        return False
    print("length of choices:", pathKeys[0], len(choices))
    label = pathKeys[0]
    i = 0
    while (i < len(choices)):
        choice = choices[i]
        filled = deepcopy(matrix)
        fits = canAddPath(choice, label, filled, vis, dim)
        if (fits and len(pathValues[0]) > 0):
            if i > 0:
                i-=1
            print("filling:", choice, label)
            filled = fillPath(filled, label, choice, ap.get(label))
            pathValues[0].remove(choice)
            filled = choosePaths(pathKeys[1:], pathValues[1:], filled, vis, dim, ap, totalNumGhosts, totalNumVampires,totalNumZombies)
            if (filled != False):
                return filled
        else:
            i+=1
            print(choice, "Doesn't fit\n")
    if (filled != False):
        matrix = deepcopy(filled)
    return False

def canAddPath(choice, key, matrix, vis, dim):
    possPathsDict, _ = possPaths(matrix, vis, dim)
    if possPathsDict.get(key) != None and choice in possPathsDict.get(key):
        return True
    else:
        return False
    
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