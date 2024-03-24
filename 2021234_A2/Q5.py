def scale_shape(cx, cy):
    
    shape = []
    num_points = int(input("Enter the number of points in the shape: "))
    for i in range(num_points):
        x = int(input("Enter x coordinate of point " + str(i+1) + ": "))
        y = int(input("Enter y coordinate of point " + str(i+1) + ": "))
        shape.append((x, y))
    
    
    scaling_matrix = [[cx, 0, 0], [0, cy, 0], [0, 0, 1]]
    
    
    shape_matrix = [[x[0], x[1], 1] for x in shape]
    
    
    result_matrix = []
    for i in range(len(shape_matrix)):
        row = shape_matrix[i]
        new_row = [0, 0, 0]
        for j in range(3):
            for k in range(3):
                new_row[j] += row[k] * scaling_matrix[k][j]
        result_matrix.append(new_row)
    
    
    new_shape = [(x[0], x[1]) for x in result_matrix]
    
    return new_shape


cx = int(input("Enter the scaling factor for x-direction: "))
cy = int(input("Enter the scaling factor for y-direction: "))
new_shape = scale_shape(cx, cy)
print("New shape:", new_shape)










