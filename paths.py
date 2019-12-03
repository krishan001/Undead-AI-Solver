def leftRows(matrix, numRows, numCols):
    tmp = []
    paths = {}
    labels = ["L1", "L2", "L3", "L4"]
    
    for k in range(0,numRows):
        for j in range(0,numRows):
            if matrix[k][j] != '\\':
                tmp.append(matrix[k][j])
            else:# if it hits a backwards mirror
                for i in range(k,numCols):
                    if matrix[i][j] != '\\':
                        tmp.append( matrix[i][j])
                break
        paths[labels[k]] = tmp
        tmp = []
    return paths
    
def rightRows(matrix, numRows, numCols):
    tmp = []
    paths = {}    
    labels = ["R1", "R2", "R3", "R4"]
    for k in range(0,numRows):
        for j in range(numRows-1,-1,-1):
            if matrix[k][j] != '\\':
                tmp.append(matrix[k][j])
            else:# if it hits a backwards mirror
                for i in range(k,-1,-1):
                    if matrix[i][j] != '\\':
                        tmp.append( matrix[i][j])
                break
        paths[labels[k]] = tmp
        tmp = []
    return paths
  
def bottomCols(matrix, numRows, numCols):
    tmp = []
    paths = {}
    labels = ["B1", "B2", "B3", "B4"]
    for k in range(0,numCols):
        for i in range(numCols-1,-1,-1):
            if matrix[i][k] != '\\':
                tmp.append(matrix[i][k])
            else:# if it hits a backwards mirror
                for j in range(k,-1,-1):
                    if matrix[i][j] != '\\':
                        tmp.append(matrix[i][j])
                break
        paths[labels[k]] = tmp
        tmp = []
    
    return paths

def topCols(matrix, numRows, numCols):
    tmp = []
    paths = {}
    labels = ["T1", "T2", "T3", "T4"]
    for k in range(0,numCols):
        for i in range(0,numCols):
            if matrix[i][k] != '\\' and matrix[i][k] != '/':
                tmp.append(matrix[i][k])
            elif matrix[i][k] == '\\': # if it hits a backwards mirror
                for j in range(k,numRows):
                    if matrix[i][j] != '\\':
                        tmp.append(matrix[i][j])
                break
        paths[labels[k]] = tmp
        tmp = []

    return paths