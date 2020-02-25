from tracePath import createPaths
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

def zeroFill(matrix, dim,vis):
    matrix = labelPaths(matrix,dim)
    rp,lp,up,dp = createPaths(matrix)
    allPaths = {}
    # merge all the dictionaries together
    allPaths.update(rp)
    allPaths.update(lp)
    allPaths.update(up)
    allPaths.update(dp)
    

    pathDict = getLabelVisDict(vis,dim)
    zeroPaths, l = getZeroPaths(pathDict, allPaths)
    for i in range(0,dim):
        for j in range(0,dim):
            if matrix[i][j] in zeroPaths:
                # check if before mirror or after
                if beforeMirror(matrix[i][j], allPaths, l):
                    matrix[i][j] = 'g'
                elif not beforeMirror(matrix[i][j], allPaths, l):
                    matrix[i][j] = 'v'
    return matrix

def beforeMirror(cell, allPaths, l):
    for e in l:
        bMirror = True
        for value in allPaths[e]:
            if value == '\\' or value =='/':
                bMirror = False
            if value == cell:
                return bMirror
    return bMirror

def labelPaths(matrix, dim):
    alph = "ABCDEFGHI"
    digits = "123456789"
    alph = alph[:dim]
    digits = digits[:dim]
    squares = cross(alph,digits)
    for i in range(0,dim):
        for j in range(0,dim):
            if matrix[i][j] == ".":
                matrix[i][j] = squares[i * dim + j]

    return matrix

def getLabelVisDict(vis,dim):
    rightLabels, leftLabels, upLabels, downLabels = getLabels(dim)
    labels = downLabels + leftLabels + upLabels +rightLabels
    return  dict(zip(labels, vis))


def getLabels(dim):
    downLabels = ["D1","D2","D3","D4","D5","D6","D7"]
    leftLabels = ["L1","L2","L3","L4","L5","L6","L7"]
    upLabels = ["U1","U2","U3","U4", "U5","U6","U7"]
    rightLabels = ["R1","R2","R3","R4", "R5","R6","R7"]
    downLabels = downLabels[:dim]
    leftLabels = leftLabels[:dim]
    upLabels = upLabels[:dim]
    rightLabels = rightLabels[:dim]

    return rightLabels, leftLabels, upLabels, downLabels
def getZeroPaths(pathDict, allPaths):
    l = []
    zeroPaths = []
    for label, vis in pathDict.items():
        if vis == 0:
            l.append(label)
    for key, value in allPaths.items():
        for e in l:
            if e == key:
                zeroPaths.append(value)
    zeroPaths = getLabelsFromZeroPaths(zeroPaths)
    return zeroPaths, l

def getLabelsFromZeroPaths(zeroPaths):
    # flatten a 2D list into a 1D list
    zeroPaths = [item for sublist in zeroPaths for item in sublist]
    # get rid of repetitions
    zeroPaths = list(dict.fromkeys(zeroPaths))
    remove = ['g','v','z','\\','/']
    # remove pre filled squares
    for e in zeroPaths:
        if e in remove:
            zeroPaths.remove(e)
    return zeroPaths