# -*- coding: utf-8 -*-
"""
@author: hanyanling
@date: 2025/2/10 17:38
@email:
---------
@summary:
"""


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
    cookies = {}
    for cookie in cookie_str.split(";"):
        cookie = cookie.strip()
        if not cookie:
            continue
        key, value = cookie.split("=", 1)
        key = key.strip()
        value = value.strip()
        cookies[key] = value

    return cookies


