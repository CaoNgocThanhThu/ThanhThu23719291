# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:39:35 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = 123456789
m = 0
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
    print("m=",m,"n=",n)