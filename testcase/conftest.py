#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 20:26
# @Author  : wade

from common.log_hepler import log

"""
conftest.py 用来文件定义全局夹具
"""
import pytest


@pytest.fixture(scope="session")
def fixture_session():
    log.info('session start')
    yield
    log.info('session end')


@pytest.fixture(scope="module")
def fixture_module():
    log.info('module start')
    yield
    log.info('module end')


@pytest.fixture(scope="class")
def fixture_class():
    log.info('class start')
    yield
    log.info('class end')


@pytest.fixture(scope="function")
def fixture_function():
    log.info('function start')
    yield
    log.info('function end')