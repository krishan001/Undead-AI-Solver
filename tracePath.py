
mirrors = True

def isSquare (matrix): #Check that it is a square matrix
    return all (len (row) == len (matrix) for row in matrix)

def createPaths(matrix, vis):
    if isSquare(matrix): 
        dim = len(matrix)
    else:
        print("matrix is not square therefore invalid")
        exit()
    # Generate paths for all directions
    rp = rightPaths(matrix, dim)
    lp = leftPaths(matrix, dim)
    up = upPaths(matrix, dim)
    dp = downPaths(matrix, dim)

    # print("Right paths: ",rp,"\n")
    # print("Left paths: ",lp,"\n")
    # print("Upwards paths: ", up, "\n")
    # print("D1 paths: ", dp["D1"],"\n")

    # Check that the number visible constraint is satisfied
    return checkVisible(rp,lp,up,dp,vis)

def checkVisible(rp,lp,up,dp,vis):
    foundVis = []
    for x in dp.values():
        foundVis.append(countVis(x))
    for x in lp.values():
        foundVis.append(countVis(x))
    for x in up.values():
        foundVis.append(countVis(x))
    for x in rp.values():
        foundVis.append(countVis(x))
    # print("Paths view the correct number:", foundVis == vis)
    return foundVis == vis

def countVis(path):
    # Given a path, figure out how many monsters you can see
    pastMirror = False
    numVis = 0
    for x in path:
        if x == '/' or x == '\\':
            pastMirror = True
        if pastMirror == False and (x == 'v' or x == 'z'):
            numVis += 1
        if pastMirror == True and (x == 'g' or x == 'z'):
            numVis += 1
    
    return numVis

def leftPaths(matrix, dim):
    # Generate left paths and add to dictionary
    paths = {}
    labels = ["L1", "L2", "L3", "L4", "L5"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix,dim-1, i, 3, dim)
    return paths

def rightPaths(matrix,dim):
    # Generate right paths and add to dictionary
    paths = {}
    labels = ["R1", "R2", "R3", "R4", "R5"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix, 0, i, 1, dim)
    return paths

def upPaths(matrix, dim):
    # Generate upwards paths and add to dictionary
    paths = {}
    labels = ["U1", "U2", "U3", "U4", "U5"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix, i, dim -1, 0, dim)
    return paths

def downPaths(matrix,dim):
    # Generate downwards paths and add to dictionary
    paths = {}
    labels = ["D1", "D2", "D3", "D4", "D5"]
    for i in range(0,dim):
        paths[labels[i]] = tracePath(matrix, i, 0, 2, dim)
    return paths

def tracePath(matrix, x, y, d, dim):
    # 0 = up, 1 = right, 2 = down, 3 = left
    path = []
    
    while(x < dim and y < dim and x >=0 and y>=0): # In the bounds of the matrix
        # if statements to figure out the new direction and x,y coords if the traversal hits a mirror
        # and call the recursive call

        # Turn to the right
        if (matrix[y][x] == "/" and d == 0) or (matrix[y][x] == "\\" and d == 2):
            if mirrors:
                path.append(matrix[y][x])
            d = 1
            x+=1
            path.extend(tracePath(matrix, x, y, d, dim))
            return path

        # Turn upwards
        elif (matrix[y][x] == "/" and d == 1) or (matrix[y][x] == "\\" and d == 3):
            if mirrors:
                path.append(matrix[y][x])
            d = 0
            y-=1
            
            path.extend(tracePath(matrix, x, y, d, dim))
            return path
        # Turn to the left
        elif (matrix[y][x] == "/" and d == 2) or (matrix[y][x] == "\\" and d == 0):
            if mirrors:
                path.append(matrix[y][x])
            d = 3
            x-=1
            path.extend(tracePath(matrix, x, y, d, dim))
            return path
        # Turn downwards
        elif (matrix[y][x] == "/" and d == 3) or (matrix[y][x] == "\\" and d == 1):
            if mirrors:
                path.append(matrix[y][x])
            d = 2
            y+=1
            path.extend(tracePath(matrix, x, y, d, dim))
            return path
        else:
            # If it doesn't hit a mirror then add it to the path
            path.append(matrix[y][x])
            if d == 0:
                y-=1
            if d == 1:
                x+=1
            if d == 2:
                y+=1
            if d == 3:
                x-=1
    return path

def checkConstraints(matrix, vis, numGhosts, numVampires,numZombies):
    solvedGhosts, solvedVamps, solvedZombies = 0,0,0
    for row in matrix:
        for c in row:
            if c == "g":
                solvedGhosts += 1
            if c == "v":
                solvedVamps += 1
            if c == "z":
                solvedZombies += 1

    return createPaths(matrix, vis) and solvedGhosts == numGhosts and solvedVamps == numVampires and solvedZombies == numZombies