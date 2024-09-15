# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:05:05 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
#a
print("a")
j = 0
for i in range(0, 10):
    j += i
print(j)
#b
print()
print("b")
j = 1
for i in range(0, 10):
    j += j
    print(j)
#c
print()
print("c")
for j in range(0, 10):
    j += j
    print(j)

