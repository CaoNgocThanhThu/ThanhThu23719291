# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:00:01 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
a = [num for num in range(2020, 3839) if num % 9 == 0]
print('\t'.join(map(str, a)))
