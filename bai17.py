# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:36:30 2024
viết một hàm tạo ds gồn n số nguyên ngấu nhien  từ 1 đến 100 sau đó sắp xếp 
theo thứ tuej giảm dần bài 17
@author: Bich Dao
"""
import random
def question_17(n:int)->list:
    random_list= [random.randint(1,100) for _ in range(n)]
    random_list.sort(reverse=True)
    return random_list
print(question_17(5))

