# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:43:34 2024
Viết một hàm nhận vào một mảng các số nguyên nums . Di chuyển tất cả các số 0
 trong mảng về cuối mảng trong khi vẫn giữ nguyên thứ tự của các phần tử không
 phải số 0.
@author: Bich Dao
"""
def question_22(nums: list[int]) -> None:
    vi_tri = 0
    for i in nums:
        if i != 0:
            nums[vi_tri] = i
            vi_tri += 1
    while vi_tri < len(nums):
        nums[vi_tri] = 0
        vi_tri += 1
    return nums
print(question_22(nums = [0, 1, 0, 3, 12]))