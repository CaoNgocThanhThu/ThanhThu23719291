# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:37:00 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
x = float(input("Nhập x = "))
while x < 0:
    x = float(input("Nhập lại x = "))
else:
    print("Giá trị đã nhập: ", x)