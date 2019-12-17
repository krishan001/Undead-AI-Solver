
from tracePath import trace_path

def isSquare (matrix): 
    return all (len (row) == len (matrix) for row in matrix)

def createPaths(matrix, vis):
    if isSquare(matrix): # this doesn't work because only checking the first column
        dim = len(matrix)
    else:
        print("matrix is not square therefore invalid")
        exit()
    
    rp = rightPaths(matrix, dim)
    lp = leftPaths(matrix, dim)
    up = upPaths(matrix, dim)
    dp = downPaths(matrix, dim)

    print("Right paths: ",rp,"\n")
    print("Left paths: ",lp,"\n")
    print("Upwards paths: ", up, "\n")
    print("D1 paths: ", dp["D1"],"\n")

    checkVisible(rp,lp,up,dp,vis)

def checkVisible(rp,lp,up,dp,vis):
    foundVis = []
    for x in dp.values():
        foundVis.append(count_vis(x))
    for x in lp.values():
        foundVis.append(count_vis(x))
    for x in up.values():
        foundVis.append(count_vis(x))
    for x in rp.values():
        foundVis.append(count_vis(x))

    print("If the paths view the correct number:", foundVis == vis)

def leftPaths(matrix, dim):
    paths = {}
    labels = ["L1", "L2", "L3", "L4"]
    for i in range(0,dim):
        paths[labels[i]] = trace_path(matrix,dim-1, i, 3, dim)
    return paths

def rightPaths(matrix,dim):
    paths = {}
    labels = ["R1", "R2", "R3", "R4"]
    for i in range(0,dim):
        paths[labels[i]] = trace_path(matrix, 0, i, 1, dim)
    return paths

def upPaths(matrix, dim):
    paths = {}
    labels = ["U1", "U2", "U3", "U4"]
    for i in range(0,dim):
        paths[labels[i]] = trace_path(matrix, i, dim -1, 0, dim)
    return paths

def downPaths(matrix,dim):
    paths = {}
    labels = ["D1", "D2", "D3", "D4"]
    for i in range(0,dim):
        paths[labels[i]] = trace_path(matrix, i, 0, 2, dim)
    return paths

def count_vis(path):
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
def readBoard(file, numLines, dim):
    grid = [[]] * dim
    # l = ["D1", "D2", "D3", "D4", "L1", "L2", "L3", "L4", "U1", "U2", "U3", "U4", "R1", "R2", "R3", "R4"]
    with open(file) as f:
        strings = [f.readline()[0:-1] for x in range(numLines)]
 
    for s in strings:
        vis = list(map(int,(s[:(dim**2)])))
        s = s[(dim**2):]
        for i in range(0,dim):
            grid[i] = list(s[:dim])
            s = s[dim:]
    # visDict = dict(zip(l,vis))
    # print(vis, "\n")
    
    
    return grid, vis
def main():
    dim = 4
    matrix, vis = readBoard("board.txt", 1, dim)
    createPaths(matrix,vis)


if __name__ == "__main__":
    main()

# talk about 8 queens or 15 puzzle or knights priblem

'''
TODO:
* Read in board from text file --
* Read in number visible
* Create test file
* fill in board with brute force
* check solved
* record time for solve
* then do depth first etc and record times
'''