# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:24:28 2019

@author: DA COSTA Paolo
"""
import cv2

img=cv2.imread('Zelda.jpg',1)
cv2.imshow('input',img)
cv2.waitKey()

def invert_colors(img_invert):
    
    
    
    print('image shape:',img_invert.shape)
    '''
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for cha in range(img.shape[2]):
                img[cha,col,row] = 255-img[cha,col,row]
     '''
    
    img_invert = 255-img_invert           
    cv2.imshow('inverted input',img_invert)
    cv2.waitKey()
    
    return img_invert

invert_colors(img)