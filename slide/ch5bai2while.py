# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:33:51 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
while True:
  try:
    a = float(input("Nhập vào một số thực: "))
    if a.is_integer():
      print("Vui lòng nhập số thực, không phải số nguyên.")
    elif -89.9 <= a <= 88.8:
      print("Số bạn nhập đã hợp lệ.")
      break
    else:
      print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
  except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại.")
