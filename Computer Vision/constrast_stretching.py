def display_matrix(matrix):
    for i in matrix:
        print(i)
    print()

def get_pixels_array_with_count(img):
    pixels = []
    for i in range(max_2d(img) + 1):
        pixels.append(0)
    
    image_height = len(img)
    image_width = len(img[image_height - 1])
    
    for i in range(image_height):
        for j in range(image_width):
            pix = img[i][j]
            pixels[pix] += 1
    return pixels
    
def display_histogram(img, width = 10):
    image_height = len(img)
    image_width = len(img[image_height - 1])
    total_pixels = image_height*image_width
    pixel_count = get_pixels_array_with_count(img)
    #print(pixel_count)
    for i in range(len(pixel_count)):
        if pixel_count[i] > 0:
            prop = (pixel_count[i]/total_pixels)
            stars = "*"*(int(prop*width))
            print("{:3} {:3} {}".format(i, pixel_count[i], stars))
    print()
    
def max_2d(matrix):
    matrix_height = len(matrix)
    matrix_width = len(matrix[matrix_height - 1])
    _max = matrix[matrix_height - 1][matrix_width - 1]
    for i in range(matrix_height):
        for j in range(matrix_width):
            if _max < matrix[i][j]:
                _max = matrix[i][j]
                
    return _max

def min_2d(matrix):
    matrix_height = len(matrix)
    matrix_width = len(matrix[matrix_height - 1])
    _min = matrix[matrix_height - 1][matrix_width - 1]
    for i in range(matrix_height):
        for j in range(matrix_width):
            if _min > matrix[i][j]:
                _min = matrix[i][j]
                
    return _min
            
def constrast_stretching_2d(_range, img):
    _max = max_2d(img)
    _min = min_2d(img)
    
    matrix_height = len(img)
    matrix_width = len(img[matrix_height - 1])
    new_image = []
    for i in range(matrix_height):
        row = []
        for j in range(matrix_width):
            row.append(int((_range*(img[i][j] - _min))/(_max - _min)))
        new_image.append(row)
    return new_image    
        

img = []
for i in range(7):
    line = []
    for j in range(3):
        line.append(5)
    line.append(70)
    for j in range(3):
        line.append(150)
    img.append(line)

a16 = constrast_stretching_2d(16, img)
display_matrix(a16)
a32 = constrast_stretching_2d(32, img)
display_matrix(a32)
a255 = constrast_stretching_2d(255, img)
display_matrix(a255)

display_histogram(img, 20)
display_histogram(a16, 20)
display_histogram(a32, 20)
display_histogram(a255, 20)