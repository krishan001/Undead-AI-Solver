def leftRows(matrix, numRows, numCols):
    tmp = []
    paths = []
    for k in range(0,numRows):
        for j in range(0,numRows):
            if matrix[k][j] != '\\':
                tmp.append(matrix[k][j])
            else:# if it hits a backwards mirror
                for i in range(k,numCols):
                    if matrix[i][j] != '\\':
                        tmp.append( matrix[i][j])
                break
        paths.append(tmp)
        tmp = []
    return paths
    
def rightRows(matrix, numRows, numCols):
    tmp = []
    paths = []
    for k in range(0,numRows):
        for j in range(numRows-1,-1,-1):
            if matrix[k][j] != '\\':
                tmp.append(matrix[k][j])
            else:# if it hits a backwards mirror
                for i in range(k,-1,-1):
                    if matrix[i][j] != '\\':
                        tmp.append( matrix[i][j])
                break
        paths.append(tmp)
        tmp = []
    return paths
  
def bottomCols(matrix, numRows, numCols):
    tmp = []
    paths = []
    for k in range(0,numCols):
        for i in range(numCols-1,-1,-1):
            if matrix[i][k] != '\\':
                tmp.append(matrix[i][k])
            else:# if it hits a backwards mirror
                for j in range(k,-1,-1):
                    if matrix[i][j] != '\\':
                        tmp.append(matrix[i][j])
                break
        paths.append(tmp)
        tmp = []
    
    return paths

def topCols(matrix, numRows, numCols):
    tmp = []
    paths = []
    for k in range(0,numCols):
        for i in range(0,numCols):
            if matrix[i][k] != '\\':
                tmp.append(matrix[i][k])
            else: # if it hits a backwards mirror
                for j in range(k,numRows):
                    if matrix[i][j] != '\\':
                        tmp.append(matrix[i][j])
                break
        paths.append(tmp)
        tmp = []
    return paths


def createPaths(matrix):
    
    pass

def main():
    matrix = [[1,2,"\\",4],
              [5,6,7,8],
              [9,"\\",11,12],
              [13,14,15,16]]
    numRows = len(matrix)
    numCols = len(matrix[0])
    topPaths = topCols(matrix, numRows, numCols)
    bottomPaths = bottomCols(matrix,numRows,numCols)
    leftPaths = leftRows(matrix, numRows, numCols)
    rightPaths = rightRows(matrix,numRows,numCols)
    print("top paths: ", topPaths)
    print("Bottom paths: ", bottomPaths)
    print("Left paths: ",leftPaths)
    print("Right paths: ",rightPaths)


if __name__ == "__main__":
    main()