from tracePath import createPaths, checkConstraints
# from UndeadAI import checkConstraints
# def checkConstraints(matrix, vis, numGhosts, numVampires,numZombies):
#     solvedGhosts, solvedVamps, solvedZombies = 0,0,0
#     for row in matrix:
#         for c in row:
#             if c == "g":
#                 solvedGhosts += 1
#             if c == "v":
#                 solvedVamps += 1
#             if c == "z":
#                 solvedZombies += 1

#     return createPaths(matrix, vis) and solvedGhosts == numGhosts and solvedVamps == numVampires and solvedZombies == numZombies

def bruteForce(solvedMatrix, vis, dim, numGhosts, numVampires,numZombies):
    if checkConstraints(solvedMatrix, vis, numGhosts, numVampires,numZombies):
        print("solved!")
    else:
        print("Failed")
    
    return solvedMatrix