from paths import *
from tracePath import trace_path
def createPaths(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    topPaths = topCols(matrix, numRows, numCols)
    bottomPaths = bottomCols(matrix,numRows,numCols)
    leftPaths = leftRows(matrix, numRows, numCols)
    rightPaths = rightRows(matrix,numRows,numCols)
    print("Top paths: ", topPaths, "\n")
    print("Bottom paths: ", bottomPaths,"\n")
    print("Left paths: ",leftPaths,"\n")
    print("Right paths: ",rightPaths,"\n")
    

def main():
    matrix = [[1    ,2    ,"\\" ,4],
              [5    ,6    ,7    ,8],
              [9    ,"\\" ,11   ,'\\'],
              ['\\' ,14   ,15   ,'/']]
    # createPaths(matrix)
    numRows = len(matrix)
    numCols = len(matrix[0])
    #print all downwards paths
    for i in range(0,4):
        p = trace_path(matrix, 0, i, 1, numRows, numCols)
        print("p: ",p)


if __name__ == "__main__":
    main()