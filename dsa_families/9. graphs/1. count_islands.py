# You get a grid of cells. Each cell is land ('1') or water ('0').
# An island is a group of land cells that touch on an edge (up, down, left, right — not diagonal).
# Return how many islands there are (one number).

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

# expected: 3

def count_islands_v1(grid: list[list]):
    row = 0
    column = 0
    islands = 0
    used = set()
    pile = []
    rows = len(grid)
    if rows == 0:
        return 0
    columns = len(grid[0])
    while row < rows:
        while column < columns:
            if grid[row][column] == "1" and (row, column) not in used:
                islands = islands + 1
                used.add((row, column))
                pile.append((row, column))
                while pile:
                    r, c = pile.pop(0)
                    # left 
                    if c - 1 >= 0:
                        if grid[r][c-1] == "1" and (r, c-1) not in used:
                            used.add((r, c-1))
                            pile.append((r, c-1))
                    # right
                    if c + 1 < columns:
                        if grid[r][c+1] == "1" and (r, c+1) not in used:
                            used.add((r, c+1))
                            pile.append((r, c+1))
                    # up
                    if r - 1 >= 0:
                        if grid[r-1][c] == "1" and (r-1, c) not in used:
                            used.add((r-1, c))
                            pile.append((r-1, c))
                    # down
                    if r + 1 < rows:
                        if grid[r+1][c] == "1" and (r+1, c) not in used:
                            used.add((r + 1, c))
                            pile.append((r+1, c))
            column = column + 1
        row = row + 1
        column = 0
    return islands

print(count_islands_v1(grid))


# Question to interviewer: May I change the grid, or must it stay as given?
# Answer: you can change the grid.
# v2 stamps land to "0" instead of used. This destroys the input.

def count_islands_v2(grid: list[list]):
    row = 0
    column = 0
    islands = 0
    pile = []
    rows = len(grid)
    if rows == 0:
        return 0
    columns = len(grid[0])
    while row < rows:
        while column < columns:
            if grid[row][column] == "1":
                islands = islands + 1
                grid[row][column] = "0"
                pile.append((row, column))
                while pile:
                    r, c = pile.pop(0)
                    if c - 1 >= 0:
                        if grid[r][c - 1] == "1":
                            grid[r][c - 1] = "0"
                            pile.append((r, c - 1))
                    if c + 1 < columns:
                        if grid[r][c + 1] == "1":
                            grid[r][c + 1] = "0"
                            pile.append((r, c + 1))
                    if r - 1 >= 0:
                        if grid[r - 1][c] == "1":
                            grid[r - 1][c] = "0"
                            pile.append((r - 1, c))
                    if r + 1 < rows:
                        if grid[r + 1][c] == "1":
                            grid[r + 1][c] = "0"
                            pile.append((r + 1, c))
            column = column + 1
        row = row + 1
        column = 0
    return islands

grid_for_v2 = [line[:] for line in grid]
print(count_islands_v2(grid_for_v2))
