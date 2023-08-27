#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 20:36
# @Author  : wade
import allure

from common.log_hepler import log

@allure.feature('Reg')
class TestCheckReg:

    @allure.story('reg-1')
    def test_check1(self, fixture_session):
        log.info('reg1 succ')
        assert True

    @allure.story('reg-2')
    def test_check2(self):
        log.info('reg2 fail')
        assert False


@allure.feature('Switcher')
class TestCheckSwitcher:

    @allure.step('1.check')
    def test_switcher1(self):
        log.info('switcher1 succ')
        assert True

    @allure.step('2.open')
    def test_switcher2(self):
        log.info('switcher2 fail')
        assert False

    @allure.step('3.close')
    def test_switcher3(self):
        log.info('switcher3 fail')
        assert False

    @allure.step('4.read')
    def test_switcher4(self):
        log.info('switcher4 fail')
        assert False