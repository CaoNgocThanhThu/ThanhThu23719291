# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:07:19 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
def tinh_tong(n):
  tong = 0
  for i in range(n+1):
    mau = 2*i + 1
    tong += 1 / mau
  return tong
n = int(input("Nhập số lượng số hạng n: "))
ket_qua = tinh_tong(n)
print("Tổng của dãy số là:", ket_qua)