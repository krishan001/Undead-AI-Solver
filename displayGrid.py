def uni(s):
    return chr(int(s,16))

def fancy_grid_line(start,norm,lcross,hcross,end):
      start,norm,lcross,hcross,end = ( uni(start),uni(norm), uni(lcross),uni(hcross),uni(end))
      return ( start + ((norm*4 + lcross)
                   + norm*4 + hcross)
                   + (norm*4 + lcross)*2
                   + norm*4  + end )

TOP_LINE       = fancy_grid_line( '2554', '2550', '2566', '2566', '2557' )
MID_LINE  = fancy_grid_line( '2560', '2550', '256c', '256c', '2563' )
BOTTOM_LINE    = fancy_grid_line( '255a', '2550', '2569', '2569', '255d' )

def printBoard(grid, vis, dim, numGhosts, numVampires,numZombies):
    # vertical bar
    dvbar = uni('2551')
    indent = "   "
    halfIndent = "  "
    print("Number of Ghosts: {} \nNumber of Vampires: {}\nNumber of Zombies: {}\n".format(numGhosts, numVampires, numZombies))
    print(indent, end="")
    # Print the number of visible monsters on the top
    for i in range(0,dim):
        print(halfIndent +str(vis[i])+ " ", end = "")
    print( "\n"+ indent + TOP_LINE )
    count = 0
    for row in grid:
        count +=1
        # Print the number of visible monsters on the left
        print( str(vis[count-1+dim*3])+ halfIndent + dvbar, end ="")
        for c in row:
            print(" " +c + " " + dvbar, end="")
        # Print the number of visible monsters on the right
        if count == dim:
            print(" " +str(vis[count-1+dim])+"\n" + indent+BOTTOM_LINE)
        else:
            print(" "+ str(vis[count-1+dim])+"\n" +indent+MID_LINE)
    print(indent, end = "")
    for i in range(0,dim):
        # Print the number of visible monsters on the bottom
        print(halfIndent +str(vis[i+dim*2])+ " ", end = "")
    print("\n")