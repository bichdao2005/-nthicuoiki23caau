# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:49:01 2024

@author: Bich Dao
"""

import random
def question_7(n:int)->(float, float):
    lst=[random.random() for _ in range(n)]
    return max(lst) , min(lst)
print(question_7(5))