# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14H20 2019

Paolo Da Costa

"""

"""

    Question 1 : What happens if Som initialization is forgotten ?
                - THe progam will work, but, the calcul will be random because Som will obtain a random number.
    Question 2 : What can you expect if all the values are below zero ?
                - The program will return an error, because they will have a division by zero.
"""

tab_List=[1,2,3,4,6,7]

import numpy as np #numpy 
import cv2
import pytest
#tab_zeros= np.zeros(12, dtype=np.int32)
tab_From_List=np.array(tab_List)
    

    
def max_value(tableau):
    """
    Functions who will do the average of an array
    """
    
    N = 0
    Som = 0
    
    if not(isinstance(tableau, list)):         
        raise ValueError('max_value expected a list as input')
      
    for id in range(len(tableau)):
         if tableau[id] >0:
             N+=1
             Som+=tableau[id]
    return Som/N     
 

print(max_value(tab_List)) 
#print(max_value(tab_From_List)) 
             
        #print('tab['+str(id)+']=' +str(tab_From_List[id]))
        #print('tab[{index}]={val}'.format(index=id, val=tab_From_List[id]))
   
           


def reverse_table(tableau_Reverse):
    """
    Function who will reverse a table
    """
    if not(isinstance(tableau_Reverse, list)):         
        raise ValueError('max_value expected a list as input')
        
    buffer = len(tableau_Reverse)
    turns = int(len(tableau_Reverse)/2)
    
    for i in range(0,turns):
        buffer = buffer-1
        tmp=tableau_Reverse[i]
        tableau_Reverse[i]=tableau_Reverse[buffer]
        tableau_Reverse[buffer]=tmp
        
    return tableau_Reverse
    
print(reverse_table(tab_List))   

def roi_bbox ():
    
    img=cv2.imread('pokeball.png',0)
    cv2.imshow('read image', img)
    cv2.waitKey()
    compteur = 0
    Coordonee_Haut = 0
    Coordonee_Droit = 0
    Coordonee_Gauche = 0
    Coordonee_Bas = 0
    
    for idrow in range (img.shape[0]):
        for idcol in range (img.shape[1]):
            pix_Val=img[idrow, idcol]
            if pix_Val != 0 and compteur == 0:
                compteur = 1
                print (idrow, idcol)
          
    
roi_bbox()
      
