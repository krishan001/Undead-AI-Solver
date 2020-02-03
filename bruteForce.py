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
        
        # print(solvedMatrix)

    if checkSolved(solvedMatrix, vis, numGhosts, numVampires,numZombies):
        print("Solved!")
    else:
        print("Failed")
    
    return solvedMatrix



def setPossibilities(matrix, dim):
    for i in range(0,dim):
        for j in range(0,dim):
            if matrix[i][j] == ".":
                matrix[i][j] = "gvz"
    return matrix