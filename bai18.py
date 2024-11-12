# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:27:11 2024
Viết một hàm để loại bỏ tất cả khoảng trắng thừa trong một chuỗi, bao gồm:
    Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
Loại bỏ các khoảng trắng dư thừa giữa các từ (chỉ giữ lại một khoảng trắng
                                              giữa các từ).

@author: Bich Dao
"""

def question_18(s:str)->str:
    return "".join(s.split())
print(question_18("Hello world"))