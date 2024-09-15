# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:45:53 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
# In 100 số Fibonacci đầu tiên
for i in range(100):
  print(fibonacci(i))