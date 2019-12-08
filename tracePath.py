mirrors = True

def trace_path(matrix, x, y, d, numRows, numCols, path = None):
    # 0 = up, 1 = right, 2 = down, 3 = left
    if path == None:
        path = []
    
    while(x < numCols and y < numRows and x >=0 and y>=0): # In the bounds of the matrix
        # if statements to figure out the new direction and x,y coords if the traversal hits a mirror
        # and call the recursive call

        # Turn to the right
        if (matrix[y][x] == "/" and d == 0) or (matrix[y][x] == "\\" and d == 2):
            if mirrors:
                path.append(matrix[y][x])
            d = 1
            x+=1
            return path.append(trace_path(matrix, x, y, d, numRows, numCols, path))

        # Turn upwards
        elif (matrix[y][x] == "/" and d == 1) or (matrix[y][x] == "\\" and d == 3):
            if mirrors:
                path.append(matrix[y][x])
            d = 0
            y-=1
            return path.append(trace_path(matrix, x, y, d, numRows, numCols, path))
        # Turn to the left
        elif (matrix[y][x] == "/" and d == 2) or (matrix[y][x] == "\\" and d == 0):
            if mirrors:
                path.append(matrix[y][x])
            d = 3
            x-=1
            return path.append(trace_path(matrix, x, y, d, numRows, numCols, path))
        # Turn downwards
        elif (matrix[y][x] == "/" and d == 3) or (matrix[y][x] == "\\" and d == 1):
            if mirrors:
                path.append(matrix[y][x])
            d = 2
            y+=1
            return path.append(trace_path(matrix, x, y, d, numRows, numCols, path))
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
    print("Path: ",path)
    return path
