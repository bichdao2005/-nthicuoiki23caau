# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:42:40 2024

@author: Bich Dao
"""

import random
def question_12()->bool:
    n= random.randint(1,1000)
    print(f"số ngẫu nhiên là {n}")
    if n<2:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True
print(question_12())