# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:02:00 2024
kiển tra chuỗi có phải là cuối palindrome hay không
@author: Bich Dao
"""
def question_9(s:str)->bool:
 a= "".join([i for i in s if i.isalnum()]).lower()
 return a==a[::-1]
print(question_9("bich"))