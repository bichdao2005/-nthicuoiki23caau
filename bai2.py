# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:22:12 2024

@author: Bich Dao tạo n số nguyên ngẫu nhiên từ 1 đến 100 và tính tổng , trung bình 
"""

import random 

def question_2(n: int) -> (int, float):
   
    ds = []
    for i in range(n):
        number = random.randint(1, 100) 
        ds.append(number) 

    tong = sum(ds)
    trungbinh = tong / n 
    return tong, trungbinh

print(question_2(5))  
print(question_2(10))