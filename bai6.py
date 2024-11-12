# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:25:46 2024

@author: Bich Dao tính giai thừa của một số nguyên dương n
"""
def question_6(n:int)->int:
    if n==0 or n==1:
        return 1
    else:
        kq=n
        for i in range(2,n):
            kq*=i
        return kq
    
print(question_6(4))