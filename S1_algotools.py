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


import numpy as np #numpy 
import cv2
tab_zeros= np.zeros(12, dtype=np.int32)
#tab_From_List=np.array(tab_List)
tab_List=[1,2,3,4,6,7]
    
img=cv2.imread('pokeball.png',0)
cv2.imshow('read image', img)
cv2.waitKey()
    
def average_above_zero(tableau):
    """
    Functions who will do the average of an array of positives values (int)
    Args : Tableau : type array
    return the var Som divided by N
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
 

print(average_above_zero(tab_List)) 
           
def max_value(tableau):
    """
    Function that return the max value and his index
    Args: tableau: an Array:List value
    
    Returns the max value and his index
    """
    
    maxVal = 0
    index=0
    
    for id_tab in range(len(tableau)):
               
            if maxVal < tableau[id_tab] :
                maxVal =  tableau[id_tab]
                index = id_tab
    return (maxVal,index)            

print(max_value(tab_List))

def reverse_table(tableau_Reverse):
    """
    Function who will reverse a table
    Args : tableau_Reverse : an array : List Value
    Returns the reverse table
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
 

def roi_bbox (bounding_Box):
    #Function who will find the boundind box of an picture
    #Args : bouding_box : 2d array (pictures)
    Returns the bouding box of numpy array
    #
    
    Coordonee_Haut = 0
    Coordonee_Droit = 0
    Coordonee_Gauche = 0
    Coordonee_Bas = 0
    
    for idrow in range (bounding_Box.shape[0]):
        for idcol in range (bounding_Box.shape[1]):
            if (bounding_Box[idrow][idcol]!=0):       
                if Coordonee_Haut > idrow:
                    Coordonee_Haut = idrow
                if Coordonee_Bas < idrow:
                    Coordonee_Bas =idrow
                if Coordonee_Gauche < idcol:
                    Coordonee_Gauche = idcol
                if Coordonee_Droit > idcol:
                    Coordonee_Droit = idcol
    bounding_Box = [[Coordonee_Haut, Coordonee_Gauche], [Coordonee_Haut, Coordonee_Droit], [Coordonee_Bas, Coordonee_Gauche], [Coordonee_Bas, Coordonee_Gauche]]
    print (bounding_Box)
    return bounding_Box 
    
    
roi_bbox(img)
  