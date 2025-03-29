# -*- coding: utf-8 -*-
"""
@author: hanyanling
@date: 2025/2/10 17:38
@email:
---------
@summary:
"""
import hashlib
from datetime import datetime, timedelta

import pandas as pd


class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls(*args, **kwargs)
        return self._instance[self._cls]


class LazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


def get_cookies_from_str(cookie_str):
    """
    将cookie字符串解析为字典格式

    :param cookie_str: cookie字符串，格式为"key1=value1; key2=value2"
    :return: 返回解析后的字典，格式为{key1: value1, key2: value2}
    """
    cookies = {}
    for cookie in cookie_str.split(";"):
        cookie = cookie.strip()  # 去除前后空格
        if not cookie:  # 跳过空字符串
            continue
        key, value = cookie.split("=", 1)  # 以第一个等号分割key和value
        key = key.strip()  # 去除key的前后空格
        value = value.strip()  # 去除value的前后空格
        cookies[key] = value  # 将key-value对存入字典

    return cookies



def get_time_range(start_time_str, end_time_str, is_timestamp=False, time_format="%Y-%m-%d", **time_delta):
    """
    返回给定时间范围内的所有时间，包含开始时间和结束时间。

    :param start_time_str: 开始时间字符串
    :param end_time_str: 结束时间字符串
    :param is_timestamp: 布尔值，如果为True，返回10位时间戳；否则返回格式化的时间字符串
    :param time_format: 时间格式字符串，仅在is_timestamp为False时有效
    :param time_delta: 时间增量，用于计算时间范围
    :return: 时间日期列表，包含开始时间和结束时间
    """
    # 将字符串转换为datetime对象
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)

    # 确保开始时间早于结束时间
    if start_time > end_time:
        raise ValueError("开始时间不能晚于结束时间")
    time_delta = time_delta or dict(days=1)
    # 计算时间范围内的所有时间
    time_range = []
    current_time = start_time
    while current_time <= end_time:
        if is_timestamp:
            time_range.append(int(current_time.timestamp()))
        else:
            time_range.append(current_time.strftime(time_format))
        current_time += timedelta(time_delta)  # 每天一个时间点

    return time_range


def is_empty_data(data):
    """
    判断给定的数据是否为空。

    :param data: 给定的数据
    :return: 如果数据为空，则返回True；否则返回False
    """
    if type(data) is pd.DataFrame:
        return data.empty
    if type(data) is pd.Series:
        return data.empty
    if data is None:
        return True
    if type(data) is list:
        return len(data) == 0
    if type(data) is dict:
        return len(data) == 0
    if type(data) is str:
        return data.strip() == ""
    return False


def timestamp_to_date(timestamp, format_str="%Y-%m-%d %H:%M:%S"):
    """
    将10位或13位时间戳转换为日期字符串

    :param timestamp: 时间戳，可以是10位（秒级）或13位（毫秒级）
    :param format_str: 日期格式字符串，默认为"%Y-%m-%d %H:%M:%S"
    :return: 格式化后的日期字符串
    """
    # 如果是13位时间戳，先转换为10位
    if len(str(timestamp)) == 13:
        timestamp = int(timestamp) // 1000

    # 将时间戳转换为datetime对象
    return datetime.fromtimestamp(int(timestamp)).strftime(format_str)



def date_to_timestamp(date_str, format_str="%Y-%m-%d %H:%M:%S", milliseconds=False):
    """
    将日期字符串转换为时间戳

    :param date_str: 日期字符串
    :param format_str: 日期格式字符串，默认为"%Y-%m-%d %H:%M:%S"
    :param milliseconds: 是否返回13位时间戳，默认为False（返回10位时间戳）
    :return: 时间戳（10位或13位）
    """
    dt = datetime.strptime(date_str, format_str)
    timestamp = int(dt.timestamp())
    return timestamp * 1000 if milliseconds else timestamp


def md5_str(string):
    """
    计算字符串的MD5哈希值

    :param string: 需要计算MD5哈希值的字符串
    :return: 字符串的MD5哈希值
    """
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))
    return md5.hexdigest()




