# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:33:01 2019

@author: Paolo Da Costa
"""

import S1_algotools.py as s1_test
import pytest
import cv2

def inc(x):
    return x+1

def test_inc():
    assert inc(3)==4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
    

"""
Test for average_above_zero
"""

def test_average_above_zero_working():
	tab_list=[1,2,3,-4,6,-9]
	test, lastID=s1_test.average_above_zero(tab_list)
	assert test==3

def test_average_above_zero_divideZero():
	tab_list=[-1,-2,-3,-4,-6,-9]
	with pytest.raises(ZeroDivisionError):
		s1_test.average_above_zero(tab_list)
        
def  test_average_above_zero_is_not_number_list():
    with pytest.raises(ValueError):
        s1_test.average_above_zero(["D","r","a","c"])
    
def test_average_above_zero_empty_list():
    with pytest.raises(ValueError):
        s1_test.average_above_zero([])
        
"""
Test for max value
"""

def test_max_value_working():
    assert s1_test.max_value([1,8,5,-4,6,3])==(8,2)

def test_max_value_table_empty():
    with pytest.raises(ValueError):
        s1_test.max_value([])
        
def  test_max_value_is_not_number_list():
    with pytest.raises(ValueError):
        s1_test.max_value(["D","r","a","c"])
    
def test_max_value_empty_list():
    with pytest.raises(ValueError):
        s1_test.max_value([])
        
"""
Test for reverse table
"""

def test_reverse_table_working():
    assert s1_test.reverse_table([1,2,3,-4,6,-9]) == [-9,6,-4,3,2,1]

def test_reverse_table_empty():
    with pytest.raises(ValueError):
        s1_test.reverse_table([])
        
def  test_reverse_table_is_not_number_list():
    with pytest.raises(ValueError):
        s1_test.reverse_table(["D","r","a","c"])
    
def test_reverse_table_empty_list():
    with pytest.raises(ValueError):
        s1_test.reverse_table([])


"""
Test for roi bbox
"""

def test_roi_bbox_expected_ndarray():
    with pytest.raises(ValueError):
        s1_test.roi_bbox(0)

def test_roi_bbox_working():
    img=cv2.imread("pokeball.png",0)
    assert s1_test.roi_bbox(img)

