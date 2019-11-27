# -*- coding:utf-8 -*-
# @Time   : 2019-11-27 17:06
# @Author : liuqian
import base64

def get_base64(path):
    f = open(path, 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()
    print(ls_f)

if __name__ == '__main__':
    path = '/opt/core/picture/ES_Framework.png'
    get_base64(path)