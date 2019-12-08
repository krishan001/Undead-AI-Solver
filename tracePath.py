def trace_path(matrix, x, y, d, numRows, numCols, path = None):
    if path == None:
        path = []
    while(x < numCols and y < numRows and x >=0 and y>=0): #in the bounds of the matrix
        #check square is not a mirror
        print(path)
        if (matrix[y][x] == "/" and d == 0) or (matrix[y][x] == "\\" and d == 2):
            d = 1
            x+=1
            return path.append(trace_path(matrix, x, y, d, numRows, numCols, path))

        elif (matrix[y][x] == "/" and d == 1) or (matrix[y][x] == "\\" and d == 3):
            d = 0
            y-=1
            return path.append(trace_path(matrix, x, y, d, numRows, numCols, path))

        elif (matrix[y][x] == "/" and d == 2) or (matrix[y][x] == "\\" and d == 0):
            d = 3
            x-=1
            return path.append(trace_path(matrix, x, y, d, numRows, numCols, path))

        elif (matrix[y][x] == "/" and d == 3) or (matrix[y][x] == "\\" and d == 1):
            d = 2
            y+=1
            return path.append(trace_path(matrix, x, y, d, numRows, numCols, path))
        else:
            path.append(matrix[y][x])
            if d == 0:
                y-=1
            if d == 1:
                x+=1
            if d == 2:
                y+=1
            if d == 3:
                x-=1
    print("Path: ",path)
    return path
