
from itertools import product
from copy import deepcopy
from zeroFill import getLabelVisDict
from tracePath import countVis, createPaths


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
        if countVis(path) == visDict[label] and changed:
            possPaths.append(path)

    return possPaths

# return if the square is blank
def isBlank(x):
    return x!= "g" and x!= "v" and  x != "z" and x != "\\" and x != "/"


def possPaths(matrix, vis, dim):
    rp,lp,up,dp = createPaths(matrix)
    possRight = allDirPaths(rp,vis,dim)
    possLeft = allDirPaths(lp,vis,dim)
    possUp = allDirPaths(up,vis,dim)
    possDown = allDirPaths(dp,vis,dim)
    # print(possRight)
    # Try and fill all possible right paths
    for label, paths in possRight.items():
        if len(paths) != 0:
            matrix = fillPath(matrix, label, paths[0], rp[label])
            # print(path)
    # Try and fill all possible left paths
    # for label, path in possLeft.items():
    #     if len(path) != 0:
    #         fillPath(matrix, label, path)
    #         # print(path)
    # # Try and fill all possible up paths
    # for label, path in possUp.items():
    #     if len(path) != 0:
    #         fillPath(matrix, label, path)
    #         # print(path)
    # # Try and fill all possible down paths
    # for label, path in possDown.items():
    #     if len(path) != 0:
    #         fillPath(matrix, label, path)
    #         # print(path)
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

def fillPath(matrix, label, path, pathToFill):
    # Actually fill the matrix with the path
    print("filling path ", label)
    print("matrix", matrix)
    print("label", label)
    print("path", path)
    print("rp", pathToFill)
    if (len(pathToFill) == len(path)):
        for i in range(0,len(path)):
            if pathToFill[i] != path[i] and isBlank(pathToFill[i]):
                tempMatrix = insertIntoMatrix(path[i], pathToFill[i], matrix)
                print(matrix)
        
    else:
        print("The path lengths don't match")
        exit()
    print("\n\n\n")
    return matrix

def insertIntoMatrix (monster, position, matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if matrix[i][j] == position:
                matrix[i][j] = monster
    
    return matrix
    
