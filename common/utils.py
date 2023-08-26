#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 19:54
# @Author  : wade

import os
def root_path():
    """ 获取 根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path