
from tracePath import trace_path
# def createPaths(matrix):
#     numRows = len(matrix)
#     numCols = len(matrix[0])
#     topPaths = topCols(matrix, numRows, numCols)
#     bottomPaths = bottomCols(matrix,numRows,numCols)
#     leftPaths = leftRows(matrix, numRows, numCols)
#     rightPaths = rightRows(matrix,numRows,numCols)
#     print("Top paths: ", topPaths, "\n")
#     print("Bottom paths: ", bottomPaths,"\n")
#     print("Left paths: ",leftPaths,"\n")
#     print("Right paths: ",rightPaths,"\n")
    
def createPaths2(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    lp = leftPaths(matrix, numRows, numCols)
    print("Left paths: ",lp,"\n")
    rp = rightPaths(matrix, numRows, numCols)
    print("Right paths: ",rp,"\n")
    up = upPaths(matrix, numRows, numCols)
    print("Top paths: ", up, "\n")
    dp = downPaths(matrix, numRows, numCols)
    print("Bottom paths: ", dp,"\n")

def leftPaths(matrix, numRows, numCols):
    paths = {}
    labels = ["L1", "L2", "L3", "L4"]
    for i in range(0,numCols):
        paths[labels[i]] = trace_path(matrix,numCols-1, i, 3, numRows, numCols)
    return paths

def rightPaths(matrix,numRows,numCols):
    paths = {}
    labels = ["R1", "R2", "R3", "R4"]
    for i in range(0,numCols):
        paths[labels[i]] = trace_path(matrix, 0, i, 1, numRows, numCols)
    return paths

def upPaths(matrix, numRows, numCols):
    paths = {}
    labels = ["U1", "U2", "U3", "U4"]
    for i in range(0,numRows):
        paths[labels[i]] = trace_path(matrix, numRows-1, 0, 0, numRows, numCols)
    return paths

def downPaths(matrix,numRows,numCols):
    paths = {}
    labels = ["D1", "D2", "D3", "D4"]
    for i in range(0,numRows):
        paths[labels[i]] = trace_path(matrix, i, 0, 2, numRows, numCols)
    return paths

def main():
    matrix = [[1    ,2    ,"\\" ,4],
              [5    ,6    ,7    ,8],
              [9    ,"\\" ,11   ,'\\'],
              ['\\' ,14   ,15   ,'/']]
    createPaths2(matrix)


if __name__ == "__main__":
    main()