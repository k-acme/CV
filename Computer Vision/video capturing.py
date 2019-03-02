# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:22:02 2019

@author: Shark
"""


import cv2
import image_filtering as imagefilter
import image_sampling as imagesampler
ver_filter = [[1,1,1], [0,0,0], [-1,-1,-1]]


def display_image(imglist):
    newimage = imagereader.fromarray(numpy.asarray(imglist))
    #newimage.save(path+"temp.jpg")
    newimage.show()
    

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ratio = 5
    gr_down_sampled = imagesampler.down_sample_2d(gr, len(gr)/ratio, len(gr[0])/ratio)
    verfilteredimagearr = imagefilter.filter_image(gr_down_sampled, ver_filter, 1)
    #display_image(verfilteredimagearr)
    cv2.imshow("frrame", gr_down_sampled)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        #out = cv2.imwrite('capture.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()