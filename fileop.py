# -*- coding: utf-8 -*-
"""
    Created on Thu Apr 25 20:03:57 2019
    @Project  : Python Memo
    @File     : fileop.py
    @Function : 文件操作
    @Author   : yehx
    @E-mail   : yehxian@163.com
"""

#保存到记事本
with open("test.txt","w") as f:
    f.write("string")

#读取记事本内容
with open("test.txt", "r") as f:
    while True:
        data = f.readline()
        print(data)
        if not data:
            break