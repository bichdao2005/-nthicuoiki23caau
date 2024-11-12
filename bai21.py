# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:34:10 2024
Viết một hàm nhận vào một danh sách số nguyên ngẫu nhiên và một số nguyên
 dương. Hàm sẽ tìm trong danh sách hai số có tổng bằng với số nguyên dương
 kia và trả về cặp số đó.
@author: Bich Dao
"""

def question_21(nums:list[int],target: int):
    x={}
    for num in nums:
        y =target-num
        if y in x:
            return (y,num)
        x[num]=True
    return None
print(question_21([1,3,4,3,6],4))
print(question_21([1, 2, 3, 4, 5], 10))
