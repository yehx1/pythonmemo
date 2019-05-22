# -*- coding: utf-8 -*-
"""
    Created on Wed May 22 08:45:36 2019
    @Project  : Python Memo
    @File     : imageop.py
    @Function : 图像基本操作
    @Author   : yehx
    @E-mail   : yehxian@163.com
"""

import cv2
import numpy as np

#图片字节流转矩阵
with open ("image.jpg",'rb') as myimage:
    data=myimage.read()
    image = np.asarray(bytearray(data), dtype="uint8")
    img = cv2.imdecode(image,cv2.IMREAD_COLOR)