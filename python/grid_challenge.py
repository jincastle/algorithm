def gridChallenge(grid):
    # Write your code here
    res = 'YES'
    newgrid = []

    for row in grid:
        newgrid.append(sorted(row))

        # for row in newgrid:
        #    print(row)

        for ind in range(len(grid)):
            for jnd in range(ind, len(grid[0])):
                newgrid[ind][jnd], newgrid[jnd][ind] = newgrid[jnd][ind], newgrid[ind][jnd]

                for row in newgrid:
                    if row != sorted(row):
                        res = 'NO'
                        break

                    return res
