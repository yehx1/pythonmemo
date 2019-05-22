# -*- coding: utf-8 -*-
"""
    Created on Fri Apr 26 20:25:21 2019
    @Project  : Python Memo
    @File     : encodeop.py
    @Function : 编解码操作
    @Author   : yehx
    @E-mail   : yehxian@163.com
"""


import numpy as np
import cv2

#字节流转字符串
byte_str = b"\xe5\x8f\xb6\xe6\xb1\x87\xe8\xb4\xa4"
print(byte_str.decode("utf8"))

#图片字节流转矩阵
with open ("image.jpg",'rb') as myimage:
    data=myimage.read()
    image = np.asarray(bytearray(data), dtype="uint8")
    img = cv2.imdecode(image,cv2.IMREAD_COLOR)