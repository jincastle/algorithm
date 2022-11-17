def gridChallenge(grid):
    # Write your code here
    res = 'YES'
    newgrid = []

    for row in grid:
        newgrid.append(sorted(row))

        for ind in range(len(grid)):
            for jnd in range(ind, len(grid[0])):
                newgrid[ind][jnd], newgrid[jnd][ind] = newgrid[jnd][ind], newgrid[ind][jnd]

                for row in newgrid:
                    if row != sorted(row):
                        res = 'NO'
                        break

                    return res


#좀더 좋은 코드
def gridChallenge(grid):
    # Write your code here
    grid =[list(row) for row in grid]
    r = len(grid)
    c = len(grid[0])
    for i in range(r):
        grid[i].sort()
        
    for j in range(c):
        for i in range(1,r):
            if not grid[i-1][j] <= grid[i][j]:
                return "NO"
    return "YES"
