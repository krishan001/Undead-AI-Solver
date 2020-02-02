from tracePath import createPaths, checkSolved
from random import seed
from random import randint
from copy import deepcopy
def randomBruteForce(solvedMatrix, vis, dim, numGhosts, numVampires,numZombies):
    seed(1)
    originalMatrix = deepcopy(solvedMatrix)
    while (checkSolved(solvedMatrix, vis, numGhosts, numVampires,numZombies) == False):
        solvedMatrix = deepcopy(originalMatrix)
        for i in range(0,dim):
            for j in range(0,dim):
                if solvedMatrix[i][j] == ".":
                    value = randint(1,3)
                    if value == 1:
                        solvedMatrix[i][j] = "g"
                    if value == 2:
                        solvedMatrix[i][j] = "v"
                    if value == 3:
                        solvedMatrix[i][j] = "z"
        
        print(solvedMatrix)

    if checkSolved(solvedMatrix, vis, numGhosts, numVampires,numZombies):
        print("Solved!")
    else:
        print("Failed")
    
    return solvedMatrix

def bruteForce(solvedMatrix, vis, dim, numGhosts, numVampires,numZombies):
    originalMatrix = deepcopy(solvedMatrix)
    while (checkSolved(solvedMatrix, vis, numGhosts, numVampires,numZombies) == False):
        solvedMatrix = deepcopy(originalMatrix)
        for i in range(0,dim):
            for j in range(0,dim):
                for k in range(1,4):
                    if solvedMatrix[i][j] == "." or solvedMatrix[i][j] == "g" or solvedMatrix[i][j] == "v" or solvedMatrix[i][j] == "z" :
                        if k == 1:
                            solvedMatrix[i][j] = "g"
                            if checkSolved(solvedMatrix, vis, numGhosts, numVampires,numZombies):
                                break
                        if k == 2:
                            solvedMatrix[i][j] = "v"
                            if checkSolved(solvedMatrix, vis, numGhosts, numVampires,numZombies):
                                break
                        if k == 3:
                            solvedMatrix[i][j] = "z"
                            if checkSolved(solvedMatrix, vis, numGhosts, numVampires,numZombies):
                                break
        print(solvedMatrix)

    return solvedMatrix


def setPossibilities(matrix, dim):
    for i in range(0,dim):
        for j in range(0,dim):
            if matrix[i][j] == ".":
                matrix[i][j] = "gvz"
    return matrix