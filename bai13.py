# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:46:36 2024
viết một hàm để điếm số từ trong một chuỗi  một từ đươch định nghĩa 
là một chuỗi là các kí tự không phải khoảng trắng
@author: Bich Dao
"""

def question_13(s:str)->int:
    return len(s.split())
print(question_13("đinh thi bich dao"))