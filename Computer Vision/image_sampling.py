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
    ratio = math.floor(image_width/new_image_width)
    print("Ratio: " + str(ratio))
    index = 0
    while index < image_width and len(new_image) < new_image_width:
        new_image.append(image[index])
        #skipping pixels
        for i in range(ratio):
            index += 1
            
    
    while len(new_image) < new_image_width:
        new_image.append(image[image_width-1])
    return new_image


def down_sample_2d(image, new_image_width, new_image_height):
    image_height = len(image)
    image_width = leng(image[image_height-1])
    
    
    
def up_sample_2d(image):
    new_image = []

    
    
    
    
    
    
    
    
image = [1,2,3,4,5,6,7,8,9,10]
print(down_sample_1d(image, 4))