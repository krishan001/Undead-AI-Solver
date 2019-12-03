from paths import *

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
    matrix = [[1,2,"\\",4],
              [5,6,7,8],
              [9,"\\",11,12],
              [13,14,15,16]]
    createPaths(matrix)


if __name__ == "__main__":
    main()