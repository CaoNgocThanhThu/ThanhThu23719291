# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:15:15 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
import random
a = random.randint(20,30)
b = [random.uniform(18,99)**2 for i in range(a)]
print(f"Số lượng phần tử được chọn ngẫu nhiên: {a}")
print("Các giá trị bình phương được chọn ngẫu nhiên: ")
for i in b:
    print(f"{i:.2f}")
