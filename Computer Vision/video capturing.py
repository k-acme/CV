# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:22:02 2019

@author: Shark
"""


import cv2
import numpy

from PIL import Image as imagereader

import image_filtering as imagefilter
import image_sampling as imagesampler
ver_filter = [[1,1,1], [0,0,0], [-1,-1,-1]]



cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ratio = 10
    gr_down_sampled = imagesampler.down_sample_2d(gr, len(gr[0])/ratio, len(gr)/ratio)
    verfilteredimagearr = imagefilter.filter_image(gr_down_sampled, ver_filter, 1)
    framex = cv2.UMat(numpy.array(imagereader.fromarray(numpy.asarray(verfilteredimagearr)), dtype=numpy.uint8))
    #framex = cv2.UMat(numpy.asarray(verfilteredimagearr))
    cv2.imshow("IMAGE: ", framex)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        #out = cv2.imwrite('capture.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()