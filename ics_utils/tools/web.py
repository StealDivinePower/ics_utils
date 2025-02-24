# -*- coding: utf-8 -*-
"""
@author: hanyanling
@date: 2025/2/24 14:05
@email:
---------
@summary:
"""
import re


def remove_comments(html_str):
    """
    去除HTML字符串中的注释
    :param html_str: 要处理的HTML字符串
    :return: 去除注释后的HTML字符串
    """
    return re.sub("<!--.*?(?:-->|$)", '', html_str, flags=re.DOTALL)







