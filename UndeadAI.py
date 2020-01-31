
from tracePath import createPaths
   
def readBoard(file, numLines, dim):
    # Read the board from a text file
    grid = [[]] * dim
    with open(file) as f:
        strings = [f.readline()[0:-1] for x in range(numLines)]
    
    for s in strings:
        # take the number visible in each path and remove them from the string
        vis = list(map(int,(s[:(dim**2)])))
        s = s[(dim**2):]
        # create grid from string
        for i in range(0,dim):
            grid[i] = list(s[:dim])
            s = s[dim:]

    
    return grid, vis

def main():
    # define the dimentions of the board
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