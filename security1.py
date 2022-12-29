# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:14:44 2022

@author: watson
"""

#加密 MD5 最簡單的加密 

import hashlib  

def MD5(str):
    md = hashlib.md5() # 建立一個 md5 物件
    md.update(str.encode(encoding='utf-8'))
    return md.hexdigest() # 加密動作


if __name__ == "__main__":
    pwd = "lcc12345"
    password = MD5(pwd)
    
    print("加密後：",password)

