from tracePath import createPaths, checkConstraints
from random import seed
from random import randint
from copy import deepcopy
def bruteForce(solvedMatrix, vis, dim, numGhosts, numVampires,numZombies):
    seed(1)
    originalMatrix = deepcopy(solvedMatrix)
    while (checkConstraints(solvedMatrix, vis, numGhosts, numVampires,numZombies) == False):
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

    if checkConstraints(solvedMatrix, vis, numGhosts, numVampires,numZombies):
        print("solved!")
    else:
        print("Failed")
    
    return solvedMatrix