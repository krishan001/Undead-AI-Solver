from tracePath import createPaths

def checkConstraints(matrix, vis):
    return createPaths(matrix, vis)

def bruteForce(solvedMatrix, dim, vis):
    if checkConstraints(solvedMatrix,vis):
        print("solved!")
    else:
        print("Failed")
    
    return solvedMatrix