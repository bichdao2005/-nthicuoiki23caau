# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:22:18 2024

@author: Bich Dao cho 1 chuỗi s chỉ gồm các chữ cái thường và viết hoa.
viết một hàm đêm trả về độ dài của chuỗi palindrome dài nhất tạo ra từ các chữ cái đó
.các chữ cái có phân biệt chữ hoa và chữ thường

"""

import collections

def question_26(s: str) -> int:
    char_count = collections.Counter(s)
    length = 0

    for count in char_count.values():
        length += count // 2 * 2
        
        if count % 2 == 1:
            length += 1
    
    return length

print(question_26("abccccdd")) 
print(question_26("a"))          
print(question_26("bbb"))