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
    
path = []
def trace_path(matrix, x, y, direction, numRows, numCols):
    #direction: 0 - North, 1 - East, 2 - South, 3 - West
    #matrix[y][x]
    if direction == 0:
        #iterate to upwards
        while(x < numCols and y < numRows and x >=0 and y>=0): #in the bounds of the matrix
            if matrix[y][x] != '\\' and matrix[y][x] != '/':
                #add the square to the path
                if matrix[y-1][x] is not None:
                    path.append(matrix[y][x])
                else: return path
            elif matrix[y][x] == '\\':
                # recursively call it with a direction to the left
                if matrix[y][x-1] is not None:
                    return path.append(trace_path(matrix,x-1,y,3,numRows, numCols))
                else:
                    return path
            elif matrix[y][x] == '/':
                if matrix[y][x+1] is not None:
                    return path.append(trace_path(matrix,x+1,y,1,numRows, numCols))
                else:
                    return path
            y-=1
            print(path)
        return path


        
    if direction == 1:
        #iterate to the right
        while(x < numCols and y < numRows and x >=0 and y>=0): #in the bounds of the matrix
            if matrix[y][x] != '\\' and matrix[y][x] != '/':
                #add the square to the path
                path.append(matrix[y][x])
            elif matrix[y][x] == '\\':
                # recursively call it with a direction downwards
                if matrix[y+1][x] is not None:
                    return path.append(trace_path(matrix,x,y+1,2,numRows, numCols))
                else: return path
            elif matrix[y][x] == '/':
                if matrix[y-1][x] is not None:
                    return path.append(trace_path(matrix,x,y-1,0,numRows, numCols))
                else: return path
            x+=1
            print(path)

        return path

        
    if direction == 2:
        #iterate downwards
        while(x < numCols and y < numRows and x >=0 and y>=0): #in the bounds of the matrix
            if matrix[y][x] != '\\' and matrix[y][x] != '/':
                #add the square to the path
                path.append(matrix[y][x])
            elif matrix[y][x] == '\\':
                # recursively call it with a direction to the right
                if matrix[y][x+1] is not None:
                    return path.append(trace_path(matrix,x+1,y,1,numRows, numCols))
                else: return path
            elif matrix[y][x] == '/':
                if matrix[y][x-1] is not None:
                    return path.append(trace_path(matrix,x-1,y,3,numRows, numCols))
                else: return path
            y+=1
            print(path)

        return path

    if direction == 3:
        #iterate to the left
        while(x < numCols and y < numRows and x >=0 and y>=0): #in the bounds of the matrix
            if matrix[y][x] != '\\' and matrix[y][x] != '/':
                #add the square to the path
                path.append(matrix[y][x])
            elif matrix[y][x] == '\\':
                # recursively call it with a direction upwards
                if matrix[y-1][x] is not None:
                    return path.append(trace_path(matrix,x,y-1,0,numRows, numCols))
                else: return path

            elif matrix[y][x] == '/':
                if matrix[y+1][x] is not None:
                    return path.append(trace_path(matrix,x,y+1,2,numRows, numCols))
                else: return path

            x-=1
            print( path)
        return path


def main():
    matrix = [[1,2,"\\",4],
              [5,6,7,8],
              [9,"\\",11,'\\'],
              ['\\',14,15,'/']]
    createPaths(matrix)
    numRows = len(matrix)
    numCols = len(matrix[0])
    print("final path: ", trace_path(matrix, 1, 0, 2, numRows, numCols))
    print(path)


if __name__ == "__main__":
    main()