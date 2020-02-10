
from itertools import product
from copy import deepcopy
from zeroFill import getLabelVisDict
from tracePath import countVis
def allPaths(label, path, unsolved, vis, dim):
    visDict = getLabelVisDict(vis,dim)
    loop = True
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
                    loop = False
                    break
        if countVis(path) == visDict[label]:
            possPaths.append(path)

    return possPaths
# path = ['.', '.', 'g', '/', '\\', 'v', 'z', '.']
# allPaths(path)

