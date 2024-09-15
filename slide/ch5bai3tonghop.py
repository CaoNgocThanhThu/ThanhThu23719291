# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:18:52 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
import re

def check_login(username, password):
# Kiểm tra username
  if not re.match(r"^[a-zA-Z0-9]{6,24}$", username):
    return False
# Kiểm tra password
  if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,24}$", password):
    return False
  return True
# Ví dụ sử dụng hàm
username = "admin123"
password = "Pass@123"
if check_login(username, password):
  print("Đăng nhập thành công!")
else:
  print("Đăng nhập thất bại. Vui lòng kiểm tra lại thông tin.")