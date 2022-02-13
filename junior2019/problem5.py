# M * N GRid 
# 1, 2, 3, 4, ... M = Rows 
# 1, 2, ..., N = Cols
# (r, c) = row, column
# x = (a * b)

# First Line = M
# Second Line = N 
# Remaining Inputs = Cells of Rooms 

# Start at (1, 1) and end (3, 4)

m = int(input(''))
n = int(input(''))
inputs = str(input(''))
values = inputs.split(' ')

def matrix(m, n, values):
    grid = [[0 for j in range(n)] for k in range(m)]
    
    for row in grid:
        for elm in range(len(row)):
            value = int(values.pop(0).strip(' '))
            row[elm] = value
    
    x_cord_counter = 0
    y_cord_counter = 0
    starting_val = grid[0][0]
    
    while True:
        multiples = possibility(starting_val)
        for possible_cord in multiples:
            x_cord_counter = possible_cord[0] - 1
            y_cord_counter = possible_cord[-1] - 1
            if x_cord_counter >= m or y_cord_counter >= n:
                continue 
            else:
                new_val = grid[x_cord_counter][y_cord_counter]
                
                next_x_cord = x_cord_counter + 1
                next_y_cord = y_cord_counter + 1
                
                if next_x_cord > m or next_y_cord > n:
                    return 'no'
                elif next_x_cord == m and next_y_cord == n:
                    return 'yes'
                else:
                    continue
        starting_val = new_val 
            

            
def possibility(starting_val):
    multiples = []
    for i in range(1, starting_val):
        if starting_val % i == 0:
            quotient = starting_val // i
            multiples.append((i, quotient))
    return multiples



print(matrix(m, n, values))