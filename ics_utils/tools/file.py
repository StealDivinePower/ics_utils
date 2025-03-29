# -*- coding: utf-8 -*-
"""
@author: hanyanling
@date: 2025/2/22 11:27
@email:
---------
@summary:
"""
import csv

import pandas as pd


def xlsx_to_csv(xlsx_file, csv_file, outputencoding="utf-8", sheetid=1, sheetname=None):
    """
    将XLSX文件转换为CSV文件。适用于xlsx文件的xml异常等特殊情况。
    ValueError: Value must be one of {'mediumDashDot', 'thick', 'mediumDashed', 'dashDotDot', 'thin', 'mediumDashDotDot', 'hair', 'dashDot', 'double', 'slantDashDot', 'dotted', 'dashed', 'medium'}

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
        ......
        ......
    ValueError: Unable to read workbook: could not read stylesheet from xx.xlsx.
    This is most probably because the workbook source files contain some invalid XML.
    Please see the exception for more details.

    :param xlsx_file: 要转换的Excel文件路径
    :param csv_file: 转换后的CSV文件路径
    :param outputencoding: 输出CSV文件的编码，默认为"utf-8"
    :param sheetid: 要转换的Excel工作表的ID，默认为1
    :param sheetname: 要转换的Excel工作表的名称，默认为None
    """
    import xlsx2csv
    xlsx2csv.Xlsx2csv(xlsx_file, outputencoding=outputencoding).convert(csv_file, sheetid=sheetid, sheetname=sheetname)


def read_csv(csv_file, skip_line=0, encoding="utf-8-sig", iterable=False):
    """
    读取CSV文件，返回一个字典列表。
    :param csv_file: 要读取的CSV文件路径
    :param skip_line: 要跳过的行数，默认为0
    :param encoding: 文件编码，默认为"utf-8"
    :param iterable: 是否返回可迭代对象，默认为False
    :return: 一个字典列表，每个字典代表CSV文件中的一行数据
    """
    encoding__readlines = open(csv_file, encoding=encoding).readlines()
    if skip_line > 0:
        encoding__readlines = encoding__readlines[skip_line:]

    csv_dict_reader = csv.DictReader(encoding__readlines)
    if iterable:
        return csv_dict_reader
    else:
        return list(csv_dict_reader)[skip_line:]


