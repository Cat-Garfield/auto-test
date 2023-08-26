#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 19:48
# @Author  : wade
import time

import logging
from logging import handlers, Logger
import colorlog

from common.utils import root_path

LOGGER_NAME = 'simple'
LOG_FORMATTER = "[%(levelname)-8s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s"
LOG_LEVEL = logging.INFO


class LogHandler:
    """ 日志打印封装"""
    _logger = logging.getLogger(LOGGER_NAME)

    def __init__(self):
        formatter = self.log_color()
        # 设置日志格式
        format_str = logging.Formatter(LOG_FORMATTER)
        # 设置日志级别
        self._logger.setLevel(LOG_LEVEL)
        # 往屏幕上输出
        screen_output = logging.StreamHandler()
        # 设置屏幕上显示的格式
        screen_output.setFormatter(formatter)
        # 往文件里写入#指定间隔时间自动生成文件的处理器
        time_rotating = handlers.TimedRotatingFileHandler(
            filename=f'{root_path()}/{"logs/log.txt"}',
            when='D',
            backupCount=30,
            encoding='utf-8'
        )
        # 设置文件里写入的格式
        time_rotating.setFormatter(format_str)
        # 把对象加到logger里
        self._logger.addHandler(screen_output)
        self._logger.addHandler(time_rotating)
        pass

    @classmethod
    def log_color(cls):
        """ 设置日志颜色 """
        log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        }

        formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s',
            log_colors=log_colors_config
        )
        return formatter

    @classmethod
    def get_logger(cls) -> Logger:
        return cls._logger


log = LogHandler().get_logger()

if __name__ == '__main__':
    log.debug("测试")
    log.info("测试")
    log.error("测试")
    log.warning("测试")