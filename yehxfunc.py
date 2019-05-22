# -*- coding: utf-8 -*-
"""
    Created on Wed May 22 09:17:23 2019
    @Project  : Python Memo
    @File     : yehxfunc.py
    @Function : 自定义函数
    @Author   : yehx
    @E-mail   : yehxian@163.com
"""

import numpy as np
import cv2


###############################################################################
###############################################################################
#执行字符串语句，并获取变量的返回值
#expression为待执行表达式，其中所有的变量都需要放在variable_list名称的列表中
#res_list是表达式中结果变量的字符串名称列表
#varible_list是由expression右侧变量取值组成的列表
#res_list是由expression左侧变量字符串名称组成的列表
def exec_expression(expression, variable_list=[], res_list=[]):
    results = []
    loc = locals()
    exec(expression)
    for i in range(len(res_list)):
        results.append(loc[res_list[0]])
    return results

###############################################################################
###############################################################################
#图片字节流转矩阵
def byteImage2Array(byte_image):
    image = np.asarray(bytearray(byte_image), dtype="uint8")
    img = cv2.imdecode(image,cv2.IMREAD_COLOR)
    return img

if __name__ == "__main__": 
    
    #1. 字符串执行语句测试
    variable_list = [1, 2]
    res = exec_expression("result=variable_list[0]+variable_list[1]", variable_list, ["result"])
    print(res)
    
    #2. 图片字节流转矩阵测试
#    with open ("image.jpg",'rb') as myimage:
#        byte_image = myimage.read()
#        byteImage2Array(byte_image)