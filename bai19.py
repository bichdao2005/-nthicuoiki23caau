# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:30:11 2024
Viết một hàm để kiểm tra xem một số nguyên nhập vào có lớn hơn một số nguyên 
cho trước n hay không.
@author: Bich Dao
"""
def question_19(x:int,n:int)->bool:
    if x>n:
        return True
    else:
        return False
print(question_19(5,1))
print(question_19(5,112))
