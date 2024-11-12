# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:16:44 2024

@author: Bich Dao viết hàm tìm x trong danh sách lst nếu tìm thấy trả về vị trí 
(chỉ số) nếu không trả về none
"""
def question_5(lst:list, x:int)->int or None:
    if  x in lst:
        return lst.index(x)# index tìm vị trí trong chuỗi
    return None
print(question_5([1,2,3,4,5],0))

