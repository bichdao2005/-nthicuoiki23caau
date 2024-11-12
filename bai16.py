# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:21:39 2024
tính trung bình cộng của nhiều số tham gia
@author: Bich Dao
"""
def question_16(*arg)-> float:
    if not arg:
        return None
    return sum(arg)/len(arg)
print(question_16(1,2,3,4,5))
print(question_16())