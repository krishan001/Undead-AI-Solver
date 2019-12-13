
from tracePath import trace_path

def createPaths(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    rp = rightPaths(matrix, numRows, numCols)
    print("Right paths: ",rp,"\n")
    lp = leftPaths(matrix, numRows, numCols)
    print("Left paths: ",lp,"\n")
    up = upPaths(matrix, numRows, numCols)
    print("Upwards paths: ", up, "\n")
    dp = downPaths(matrix, numRows, numCols)
    print("Downwards paths: ", dp,"\n")

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
        paths[labels[i]] = trace_path(matrix, i, numRows -1, 0, numRows, numCols)
    return paths

def downPaths(matrix,numRows,numCols):
    paths = {}
    labels = ["D1", "D2", "D3", "D4"]
    for i in range(0,numRows):
        paths[labels[i]] = trace_path(matrix, i, 0, 2, numRows, numCols)
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
def readBoard(file, numLines):
    gridstring = []
    grid = [[]] * 4
    with open(file) as f:
        strings = [f.readline()[0:-1] for x in range(numLines)]
 
    for s in strings:
        for i in range(0,4):
            grid[i] = list(s[:4])
            s = s[4:]
    
    
    return grid
def main():
    # matrix = [[1    ,2    ,3    ,4],
    #           [5    ,6    ,7    ,8],
    #           [9    ,"\\" ,11   ,'\\'],
    #           ['\\' ,14   ,15   ,'/']]
    # print(matrix)
    matrix = readBoard("board.txt", 1)
    createPaths(matrix)
    testPath = ['z','g','v','\\','v', 'z','/','g']
    print("counting visible: ",count_vis(testPath))
    # print("reading board: ",readBoard("board.txt", 1))

if __name__ == "__main__":
    main()

# talk about 8 queens or 15 puzzle or knights priblem

'''
TODO:
* Read in board from text file
* Read in number visible
* Create test file
* fill in board with brute force
* check solved
* record time for solve
* then do depth first etc and record times
'''