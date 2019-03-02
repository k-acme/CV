# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:41:15 2019

@author: Shark
"""

import image_filtering as imagefilter
from PIL import Image as imagereader
import numpy


def display_image(imglist):
    newimage = imagereader.fromarray(numpy.asarray(imglist))
    #newimage.save(path+"temp.jpg")
    newimage.show()
    
    
path = "Image Reading/"

img = imagereader.open(path+"picture.jpg").convert("L")
filter = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
hor_filter = [[1,0,-1], [1,0,-1], [1,0,-1]]
ver_filter = [[1,1,1], [0,0,0], [-1,-1,-1]]
imgarr = numpy.array(img)


newimagearr = imagefilter.filter_image(imgarr, filter)
display_image(newimagearr)
horfilteredimagearr = imagefilter.filter_image(imgarr, hor_filter, 1)
display_image(horfilteredimagearr)
verfilteredimagearr = imagefilter.filter_image(imgarr, ver_filter, 1)
display_image(verfilteredimagearr)


newimagearr = imagefilter.grad_image(horfilteredimagearr, verfilteredimagearr)
display_image(newimagearr)



