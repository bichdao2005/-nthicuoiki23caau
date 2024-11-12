# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:30:02 2024
viết hàm nhập vào ds số nguyên  từ bàn phím, các số nguyên này được
 phân cách bằng khoảng trắng và trả về none nếu danh sách đó trống
@author: Bich Dao
s.split():

Phương thức split() được sử dụng để tách chuỗi s thành một danh sách các chuỗi 
con (substrings) dựa trên khoảng trắng. Ví dụ, nếu người dùng nhập "1 2 3", 
thì s.split() sẽ trả về ['1', '2', '3'].
map(int, s.split()):

* Hàm map(int, ...) sẽ áp dụng hàm int() lên mỗi phần tử của danh sách 
(mỗi phần tử là một chuỗi, ví dụ: '1', '2', '3').
* Hàm list() sẽ chuyển đối tượng map thành một danh sách. Ví dụ, đối với đầu vào "1 2 3", kết quả là [1, 2, 3].
"""
def question_10()->None:
    s=input("nhập vào danh sách số nguyên:")
    return list(map(int, s.split())) if s else  None
print(question_10())
