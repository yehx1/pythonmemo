# -*- coding: utf-8 -*-

"""
    Created on Wed May  8 10:08:27 2019
    @Project  : Python Memo
    @File     : memo.py
    @Function : 常用操作
    @Author   : yehx
    @E-mail   : yehxian@163.com
"""


#执行字符串语句，并获取变量的返回值
loc = locals()
exec("result = function(paras)")
result = loc["result"]


#读取mat文件
from scipy.io import loadmat
m = loadmat("wider_face_test.mat")
print(len(m)) 
print(m.keys())
print(m["file_list"])


#数字前面自动补零
number = "12"
number = number.zfill(5)
print(number)