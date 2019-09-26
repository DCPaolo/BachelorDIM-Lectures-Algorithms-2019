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

tab_list=[1,2,3,4,6,7]

import numpy as np #numpy 
#tab_zeros= np.zeros(12, dtype=np.int32)
tab_From_List=np.array(tab_list)
    

    
def max_value(tableau):
    """
    Functions who will do the average of an array
    """
    N = 0
    Som = 0

    for id in range(len(tableau)):
         if tableau[id] >0:
             N+=1
             Som+=tableau[id]
    return Som/N      

print(max_value(tab_From_List)) 
             
        #print('tab['+str(id)+']=' +str(tab_From_List[id]))
        #print('tab[{index}]={val}'.format(index=id, val=tab_From_List[id]))
    
       
           