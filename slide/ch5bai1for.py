# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:45:29 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = int(input("Nhập n: "))
if n < 0:
    print("Vui lòng nhập số nguyên dương: ")
else:
    giaithua = 1
    for i in range(1, n + 1):
        giaithua *= i
    print(f"Kết quả của giai thừa {n}: ", giaithua)   