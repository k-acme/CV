import math

def up_sample_1d(image):
    new_image = []
    
def down_sample_1d(image, new_image_width):
    image_width = len(image)
    if image_width <= new_image_width:
        print("Invalid arguments")
        return -1
    
    new_image = []
    #getting ratio of how many pixels to skip
    ratio = image_width/new_image_width
    ratio = round(ratio)
    index = 0
    while index < image_width and len(new_image) < new_image_width:
        new_image.append(image[index])
        #skipping pixels
        for i in range(ratio):
            index += 1
    
    while len(new_image) < new_image_width:
        #missing = 1
        missing = new_image_width - len(new_image)
        new_image.append(image[image_width-missing])
    return new_image


def down_sample_2d(image, new_image_width, new_image_height):
    image_height = len(image)
    image_width = len(image[image_height-1])
    
    if image_height <= new_image_height or image_width <= new_image_width:
        print("Invalid arguments!")
        return -1
    
    new_image = []
    
    ratio_width = round(image_width/new_image_width)
    ratio_height = round(image_height/new_image_height)
    index = 0
    while index < image_height and len(new_image) < new_image_height:
        row = down_sample_1d(image[index], new_image_width)
        if row == -1:
            return row
        
        new_image.append(row)
        
        #skipping rows
        for i in range(ratio_height):
            index += 1
    
    return new_image
        
            
    
    
def up_sample_2d(image):
    new_image = []
    

    
    
    
    
    
    
    
    
image = [1,2,3,4,5,6,7,8,9,10]
for i in range(2, len(image)):
    print(down_sample_1d(image, i))
    
    
image = [[1,2,3,4,5]
         , [4,5,6,7,8]
         , [2,3,4,5,6]
         , [9,8,7,6,4]]
print(down_sample_2d(image, 2, 3))
