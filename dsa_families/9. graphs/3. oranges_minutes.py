# You get a grid. Each cell is empty (0), a fresh orange (1), or a rotten orange (2).
# Every minute, every rotten orange makes fresh oranges on its four edges rotten
# (up, down, left, right — not diagonal).
# Return how many minutes until there is no fresh orange left.
# If some fresh orange can never become rotten, return -1.



grid = [
    [2, 1, 1],
    [0, 0, 0],
    [1, 1, 2],
]
# expected: 2

def rotten_organe_time(grid):
    i = 0
    j = 0
    rows = len(grid)
    column = len(grid[0])
    minutes = 0
    to_be_rotten = []
    while j < column:
        while i < rows:
            if grid[i][j] == 2:
                to_be_rotten.append([i,j])
            i = i + 1
        i = 0
        j = j + 1
    while to_be_rotten:
        length = len(to_be_rotten)
        range_len = range(length)
        print("range:", range_len)
        for k in range(length):
            a = to_be_rotten[0][0]
            b = to_be_rotten[0][1]
            print("a:", a, "b:", b)
            grid[a][b] = 2
            #left
            if a-1 >= 0 and [a-1,b] not in to_be_rotten and grid[a-1][b] == 1:
                to_be_rotten.append([a-1,b])
            # right
            if a+1 < rows  and [a+1,b] not in to_be_rotten and grid[a+1][b] == 1:
                to_be_rotten.append([a+1,b])
            # up
            if b-1 >= 0 and [a,b-1] not in to_be_rotten and grid[a][b-1] == 1:
                to_be_rotten.append([a,b-1])
            # down
            if b+1 < column and [a,b+1] not in to_be_rotten and grid[a][b+1] == 1:
                to_be_rotten.append([a,b+1])

            to_be_rotten.pop(0)

        if len(to_be_rotten) > 0:
            minutes = minutes + 1
       
    i = 0
    j = 0
    while j < column:
        while i < rows:
            if grid[i][j] == 1:
                return -1
            i = i + 1
        i = 0
        j = j + 1    
    
    return minutes

print(rotten_organe_time(grid))