def uni(s):
    return chr(int(s,16))

def fancy_grid_line(start,norm,lcross,hcross,end, dim):
      start,norm,lcross,hcross,end = ( uni(start),uni(norm), uni(lcross),uni(hcross),uni(end))
      print(dim)
      return ( start + ((norm*(dim-1) + lcross)
                   + norm*(dim-1) + hcross)
                   + (norm*(dim-1) + lcross) *(dim-3)
                   + norm*(dim-1)  + end )


def printBoard(grid, vis, dim, numGhosts, numVampires,numZombies):
    TOP_LINE       = fancy_grid_line( '2554', '2550', '2566', '2566', '2557', dim )
    MID_LINE  = fancy_grid_line( '2560', '2550', '256c', '256c', '2563', dim )
    BOTTOM_LINE    = fancy_grid_line( '255a', '2550', '2569', '2569', '255d', dim )
    # vertical bar
    dvbar = uni('2551')
    indent = "   "
    halfIndent = "  "
    if dim == 4:
        padding = " "
    elif dim == 5:
        padding = halfIndent
    elif dim == 7:
        padding = "   "
    print("Number of Ghosts: {} \nNumber of Vampires: {}\nNumber of Zombies: {}\n".format(numGhosts, numVampires, numZombies))
    print(indent, end="")
    # Print the number of visible monsters on the top
    for i in range(0,dim):
        print(halfIndent +str(vis[i])+ padding, end = "")
    print( "\n"+ indent + TOP_LINE )
    count = 0
    for row in grid:
        count +=1
        # Print the number of visible monsters on the left
        print( str(vis[count-1+dim*3])+ halfIndent + dvbar, end ="")
        for c in row:
            print(" " +c + padding + dvbar, end="")
        # Print the number of visible monsters on the right
        if count == dim:
            print(" " +str(vis[count-1+dim])+"\n" + indent+BOTTOM_LINE)
        else:
            print(" "+ str(vis[count-1+dim])+"\n" +indent+MID_LINE)
    print(indent, end = "")
    for i in range(0,dim):
        # Print the number of visible monsters on the bottom
        print(halfIndent +str(vis[i+dim*2])+ padding, end = "")
    print("\n")