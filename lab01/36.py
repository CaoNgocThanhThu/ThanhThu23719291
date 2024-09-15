# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:53:50 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
    S = sum(i**2 for i in range(1, n + 1))
    print(f"Tổng S từ 1^2 đến {n}^2 là: {S}")
else:
    print("Số nhập vào không phải là số nguyên dương.")

