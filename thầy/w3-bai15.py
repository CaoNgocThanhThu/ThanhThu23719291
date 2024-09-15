# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:59:43 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = int(input("Nhập số nguyên n: "))
k = int(input("Nhập cơ số k (từ 2 đến 16): "))
if k < 2 or k > 16:
    print("Cơ số k phải nằm trong khoảng từ 2 đến 16.")
else:
    digits = "0123456789ABCDEF"
    result = ""
    if n == 0:
        result = "0"
    else:
        while n > 0:
            result = digits[n % k] + result
            n //= k
    print("Số trong cơ số {} là: {}".format(n, result))
