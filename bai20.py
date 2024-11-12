# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:32:58 2024
Viết một hàm yêu cầu người dùng nhập một giá trị từ bàn phím. Nếu người
 dùng không nhập bất kỳ giá trị nào từ bàn phím (chỉ nhấn Enter),
 hàm sẽ trả về None .
@author: Bich Dao
"""
def question_20():
    nhap=input("nhập vào gì đó:")
    if nhap=="":
        return None
    return nhap
print(question_20())

