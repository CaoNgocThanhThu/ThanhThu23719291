# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:25:35 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = int(input("Nhập số lần in 'Hello': "))
if n <= 0 or n > 1000:
    print("Số lần lặp không hợp lệ. Vui lòng nhập số nguyên dương nhỏ hơn 1000.")
else:
    for _ in range(n):
      print("Hello")
