def display_mines():
	global display_mines
	global numbers
	global n

	  for row in range(n):
	  	for col in range(n):
	  		if numbers[row] [col] == -1:
	  		     mine_values[row] [col] = '*'
	for row in numbers:
		print("".join(str(cell) for cell in row))