# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:33:51 2024

@author: Bich Dao kểm tra số nguyên tố
"""

def question_1(n:int)-> bool:
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(question_1(12))