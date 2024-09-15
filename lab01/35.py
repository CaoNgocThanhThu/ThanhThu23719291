# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:29:32 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
    S = sum(range(1, n + 1))
    print(f"Tổng S từ 1 đến {n} là: {S}")
else:
    print("Số nhập vào không phải là số nguyên dương.")