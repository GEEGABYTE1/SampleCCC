# Problem 3 

''' Mahima has been experimenting with a new style of art. She stands in front of a canvas and, using
her brush, flicks drops of paint onto the canvas. When she thinks she has created a masterpiece,
she uses her 3D printer to print a frame to surround the canvas.
Your job is to help Mahima by determining the coordinates of the smallest possible rectangular
frame such that each drop of paint lies inside the frame. Points on the frame are not considered
inside the frame. ''' 

number_of_cords = int(input(''))

lst = []
for i in range(number_of_cords):
    x_y_cord = str(input(''))
    x_y_cord_split = x_y_cord.split(',')
    x_value = x_y_cord_split[0].strip(' ')
    y_value = x_y_cord_split[-1].strip(' ')
    tup = (int(x_value), int(y_value))
    lst.append(tup)


def frame(cords):
    x_lst = []
    y_lst = []
    for coordinates in cords:
        x_val = coordinates[0]
        y_val = coordinates[-1]
        x_lst.append(x_val)
        y_lst.append(y_val)
    
    min_x_val = min(x_lst)
    min_y_val = min(y_lst)
    bottom_left_x = min_x_val - 1
    bottom_left_y = min_y_val - 1

    max_x_val = max(x_lst)
    max_y_val = max(y_lst)
    top_right_x = max_x_val + 1
    top_right_y = max_y_val + 1
    
    bottom_left_corner = '{x}, {y}'.format(x=bottom_left_x, y=bottom_left_y)
    top_right_corner = '{x}, {y}'.format(x=top_right_x, y=top_right_y)
    print(bottom_left_corner)
    print(top_right_corner)

print(frame(lst))