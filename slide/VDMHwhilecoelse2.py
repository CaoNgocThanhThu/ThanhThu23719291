# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:39:02 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
count = 0 
n = int(input("Nhập vào số lần cần lặp: "))
while (count < n):
    print("Lần lặp thứ: ", count + 1, "\t Biến đếm: ", count)
    count = count + 1
else:
    print("\n Thực hiện lệnh trong else, do: ",
          "\n count = ", count, "\n n = ", n,
          "\n bool(count < n) = ", bool(count < n))