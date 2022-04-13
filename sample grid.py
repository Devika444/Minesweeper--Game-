def empty_grid():
    global n
    grid = []
    for row in range(n):
        A = []
        for col in range(n):
            A.append(0)
        grid.append(A)

#for printing the grid
    for row in range(n):
        for col in range(n):
            print(grid[row][col], end = " ")
        print()

if __name__ == "__main__":
    n = 5
    empty_grid()
