
from itertools import product
from copy import deepcopy
from zeroFill import getLabelVisDict
from tracePath import countVis, createPaths
def allPaths(label, path, unsolved, vis, dim):
    visDict = getLabelVisDict(vis,dim)
    loop = True
    changed = False
    possible = ['g', 'v', 'z']
    possPaths = []
    ogPath = deepcopy(path)
    allPoss = list(set(product(list(set(possible)),repeat = unsolved)))
    for i in range(0,len(allPoss)):
        path = deepcopy(ogPath)
        for j in allPoss[i]:
            loop = True
            for k in range(0,len(path)):
                if path[k]!= "g" and path[k] != "v" and  path[k] != "z" and path[k] != "\\" and path[k] != "/" and loop:
                    path[k] = j
                    changed = True
                    loop = False
                    break
        if countVis(path) == visDict[label] and changed:
            possPaths.append(path)

    return possPaths


def possPaths(matrix, vis, dim):
    rp,lp,up,dp = createPaths(matrix)
    possRight = allDirPaths(rp,vis,dim)
    possLeft = allDirPaths(lp,vis,dim)
    possUp = allDirPaths(up,vis,dim)
    possDown = allDirPaths(dp,vis,dim)
    print(possRight)
    for label, path in possRight.items():
        if len(path) != 0:
            fillPath(matrix, label, path)
            print(path)
    for label, path in possLeft.items():
        if len(path) != 0:
            fillPath(matrix, label, path)
            print(path)
    for label, path in possUp.items():
        if len(path) != 0:
            fillPath(matrix, label, path)
            print(path)
    for label, path in possDown.items():
        if len(path) != 0:
            fillPath(matrix, label, path)
            print(path)
def numUnsolved(path):
    i = 0
    for e in path:
        if e != "g" and e != "v" and  e != "z" and e != "\\" and e != "/":
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

def fillPath(matrix, label, path):
    print("filling path ", label)
