
from tracePath import createPaths
from bruteForce import bruteForce
   
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
def uni(s):
    return chr(int(s,16))

def fancy_grid_line(start,norm,lcross,hcross,end):
      start,norm,lcross,hcross,end = ( uni(start),uni(norm),
                                       uni(lcross),uni(hcross),uni(end))
      return ( start +
               ((norm*3 + lcross)
                   + norm*3 + hcross)
                   + (norm*3 + lcross)
                   + norm*3  + end )

TOP_LINE       = fancy_grid_line( '2554', '2550', '2564', '2566', '2557' )
THIN_MID_LINE  = fancy_grid_line( '255f', '2500', '253c', '256b', '2562' )
BOTTOM_LINE    = fancy_grid_line( '255a', '2550', '2567', '2569', '255d' )

def printBoard(grid, vis,dim):
    dvbar = uni('2551')
    indent = "   "
    halfIndent = "  "
    print(indent, end="")
    for i in range(0,dim):
        print(halfIndent +str(vis[i])+ " ", end = "")
    print( "\n"+ indent + TOP_LINE )
    count = 0
    for row in grid:
        count +=1
        print( str(vis[count-1+dim*3])+ halfIndent + dvbar, end ="")
        for c in row:
            print(" " +c + " " + dvbar, end="")
        if count == 4:
            print(" " +str(vis[count-1+dim])+"\n" + indent+BOTTOM_LINE)
        else:
            print(" "+ str(vis[count-1+dim])+"\n" +indent+THIN_MID_LINE)
    print(indent, end = "")
    for i in range(0,dim):
        print(halfIndent +str(vis[i+dim*2])+ " ", end = "")
    print("\n")
def main():
    # define the dimentions of the board
    dim = 4
    matrix, vis = readBoard("board.txt", 1, dim)
    # printBoard(matrix,vis, dim)
    bruteForce(matrix,dim, vis)
    # createPaths(matrix,vis)


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