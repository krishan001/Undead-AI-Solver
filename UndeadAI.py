
from tracePath import createPaths
   
def readBoard(file, numLines, dim):
    # Read the board from a text file
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



'''
TODO:
* Create test file
* Object for each square with value so can cross reference across paths
* fill in board with brute force
* check solved
* record time for solve
* then do depth first etc and record times
'''