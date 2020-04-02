def choosePaths(pathLabels, pathValues, matrix, ap):
    # print("\n\n")
    # print("keys",pathKeys)
    filled = deepcopy(matrix)

    if(checkSolved(matrix)):
        return filled

    elif pathValues == [] or len(pathValues[0]) == 0:
        return False

    choices = pathValues[0]
    label = pathLabels[0]
    # print("length of choices:", label, len(choices))
    # print("choices", choices)
    i = 0
    while (i < (len(choices))):
        choice = choices[i]
        # print(label)
        filled = deepcopy(matrix)
        fits = canAddPath(choice, label, filled)
        # Check for the correct number of monsters
        tempFilled = fillPath(filled, label, choice, ap.get(label))
        # printBoard(tempFilled,vis,dim,numGhosts,numVampires, numZombies)
        numG, numV, numZ = countNumMonsters(tempFilled)

        if (numG > numGhosts or numV > numVampires or numZ > numZombies):
            # print("Too many monsters")
            fits = False

        if (fits and len(pathValues[0]) > 0):
            # print("filling:", choice, label)

            pathValues[0].remove(choice)
            filled = choosePaths(pathLabels[1:], pathValues[1:], tempFilled, ap)
            if i > 0:
                i-=1  
            
            if (filled != False):
                return filled
        else:
            # print(i)
            i+=1
            # print(choice, "Doesn't fit\n")


    return False
