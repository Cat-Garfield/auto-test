#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 18:59
# @Author  : wade

import os

import pytest


if __name__ == '__main__':
    """
    参数说明：
        -s 表示输出调试信息，包括print打印信息
        -v 表示输出用例执行详细信息
        -q：输出简化信息，不输出环境信息
        -n 支持多线程或者分布式运行测试用例
        --reruns 失败用例重跑
        -x 只要存在失败用例则停止执行
        --maxfail 只要存在max个失败用例则停止执行
        -k 根据测试用例的部分字符串执行用例
    
    allure相关参数说明：
        --alluredir 生成allure报告的路径
        --clean-alluredir 清除报告
    """
    pytest.main([
        '-vs',
        '--alluredir=reports/allure',
        '--clean-alluredir'
    ])

    """ 
    测试完成后自动启动报告服务
    """
    os.system('allure serve reports/allure --clean')