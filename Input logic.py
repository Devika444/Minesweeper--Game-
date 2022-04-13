#python 3.7.1
def won_game(grid,list_nonzeros):
  count = 0
  while count != len(list_nonzeros):
    for pair in list_nonzeros:
      if grid[pair[0]][pair[1]] == user_grid[pair[0]][pair[1]]:
        count += 1 
  if count == len(list_nonzeros):
    print("congratulations ! you won the game")
  


def lose_game():
  for row in range(n):
    for col in range(n):
      if grid[row][col] == '*':
        print(user_grid[row][col])
  print("lose! u entered into a mine ")
        
        
def zero_valued_numbers(row,col): 
  if grid[row][col] == 0:
    print(user_grid[row][col])
    if row > 0:
      zero_valued_numbers(row - 1,col)
    if row < size - 1:
      zero_valued_numbers(row + 1,col)
    if col > 0:
      zero_valued_numbers(row,col - 1)
    if col < size - 1:
      zero_valued_numbers(row,col + 1)
      
    
 #3 types of inputs can be given
list_nonzeros = []


if user_grid[row][col] != '*' and user_grid[row][col] != 0:
  list_nonzeros.append([row,col])
if user_grid[row][col] == '*':
  lose_game()
if user_grid[row][col] == 0:
  zero_valued_numbers(row,col)
 
    
