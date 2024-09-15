# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:28:30 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
while True:
  a = int(input("Nhập vào một số nguyên: "))
  if -99 <= a <= 99:
    print("Số bạn nhập đã hợp lệ.")
    break
  else:
    print("Số bạn nhập không hợp lệ! Vui lòng nhập lại.")
