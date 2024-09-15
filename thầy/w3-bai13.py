# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:39:35 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
while True:
    n = input("Nhập giá trị của n: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương.")
    else:
        print("Vui lòng nhập một số nguyên hợp lệ.")
power_of_two = 1
while power_of_two <= n:
    print(power_of_two)
    power_of_two *= 2
