import math

def display_matrix(m):
    for i in range(len(m)):
        row = ""
        for j in range(len(m[i])):
            row += "{:4} ".format(m[i][j])
        print(row)

radius = 5
center = 5
dimension = {'width': 11, 'height': 11}

matrix = []
#creating matrix
for i in range(dimension['height']):
    row = []
    for j in range(dimension['width']):
        row.append(0)
    matrix.append(row)
    
#entering values
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        v = int(math.pow(i - center, 2) + math.pow(j - center, 2))
        if v == math.pow(radius, 2):
            v = 1
        matrix[i][j] = v;

display_matrix(matrix)
