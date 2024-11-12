# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:47:10 2024
Viết một hàm nhận vào một mảng các số nguyên nums . Trả về True nếu có bất kỳ
 giá trị nào xuất hiện ít nhất hai lần trong mảng, và trả về False nếu tất cả
 các phần tử trong mảng đều khác nhau.
@author: Bich Dao
"""

def question_23(nums: list[int]) -> bool:
    chuoi = set()  
    for i in nums:
        if i in chuoi: 
            return True  
        chuoi.add(i)    
    return False  
print(question_23([1, 2, 3, 1]))  
print(question_23([1, 2, 3, 4])) 
print(question_23([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
