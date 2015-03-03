
def getNextRow(grid, i, j):
    if j-1 >= 0:
        return grid[i+1][j-1:j+2:]
    elif j+2 >= len(grid[i]):
        return grid[i+1][j-1:j+1:]

grid = []
for line in open("./data/18.txt"):
    grid.append(map(lambda x: int(x), line.split(" ")))

print getNextRow(grid, 2,2)
