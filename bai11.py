# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:23:30 2024
viết một hàm question_11 để trả về số Fibonacci thứ n
@author: Bich Dao
"""
def question_11(n:int)->int:
    a,b=0,1 
    for _ in range(n):
        a,b=b,a+b
    return a
print(question_11(10))

