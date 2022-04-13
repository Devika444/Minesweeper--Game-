#python 3.7.1

def lose_game():
  for row in range(n):
    for col in range(n):
      if grid[row][col] == '*':
        print(grid[row][col])
        
        
def zero_valued_numbers(row,col): 
  if grid[row][col] == 0:
    print(grid[row][col])
    if row > 0:
      zero_valued_numbers(row - 1,col)
    if row < size - 1:
      zero_valued_numbers(row + 1,col)
    if col > 0:
      zero_valued_numbers(row,col - 1)
    if col < size - 1:
      zero_valued_numbers(row,col + 1)
      
