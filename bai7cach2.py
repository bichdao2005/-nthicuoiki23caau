# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:32:54 2024
tạo ds n số thực ngẫu nhiên trong khoảng từ 0 đến 1 . sau đó tìm số lớn nhất nhỏ nhất
trong ds
@author: Bich Dao
"""
import random
def question_7(n:int)-> (float, float):
    lst=[]
    for i in range (n):
        lst.append(random.random())
    return max(lst), min(lst)
print(question_7(5))   
