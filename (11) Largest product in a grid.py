# What is the greatest product of four adjacent numbers in
# the same direction (up, down, left, right, or diagonally) in the 20x20 grid?

def calculateProductFromPoint(i, j, grid):
    maxProduct = 0;
    if i + 4 < 20:
        product = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        if product > maxProduct:
            maxProduct = product

        if j + 4 < 20:
            product = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if product > maxProduct:
                maxProduct = product

        if j - 4 > 0:
            product = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
            if product > maxProduct:
                maxProduct = product

    if i - 4 > 0:
        product = grid[i][j]*grid[i-1][j]*grid[i-2][j]*grid[i-3][j]
        if product > maxProduct:
            maxProduct = product

        if j + 4 < 20:
            product = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
            if product > maxProduct:
                maxProduct = product

        if j - 4 > 0:
            product = grid[i][j]*grid[i-1][j-1]*grid[i-2][j-2]*grid[i-3][j-3]
            if product > maxProduct:
                maxProduct = product

    if j + 4 < 20:
        product = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if product > maxProduct:
            maxProduct = product

    if j - 4 > 0:
        product = grid[i][j]*grid[i][j-1]*grid[i][j-2]*grid[i][j-3]
        if product > maxProduct:
            maxProduct = product

    return maxProduct


grid = []
for line in open("./data/11.txt"):
    grid.append(map(lambda x: int(x), line.split(" ")))

i,j,maxProduct = 0,0,0
while i < len(grid):
    j = 0
    while j < len(grid[0]):
        product = calculateProductFromPoint(i, j, grid)
        if product > maxProduct:
            maxProduct = product
        j += 1
    i += 1

print maxProduct
