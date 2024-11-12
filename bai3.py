# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:23:31 2024
đếm kí tự hoa và viết thường có bao nhiêu cữ viết hoa bn chữ viết thường trong chuỗi
@author: Bich Dao
"""

def question_3(s:str)->(int, int):
    hoa=0
    thuong=0
    for char  in s:
        if char.isupper():
            hoa+=1
        elif char.islower():
            thuong+=1
    return hoa, thuong
print(question_3("daoBiCh"))
        