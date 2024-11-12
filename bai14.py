# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:52:37 2024()
viết một hàm để kiểm tra 1chuỗi có phải là chữ số hay không(chuỗi được coi
 là chứ số nếu tất cả các kí tuwjtrong chuỗi là số và không có kí tự nào khác)
@author: Bich Dao
"""
def question_14(s:str)->bool:
   for chuoi in s:
       if chuoi<"0" or chuoi>"9":
           return False
       return True
print(question_14("345678"))