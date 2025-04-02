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
from openpyxl.reader.excel import load_workbook
from pandas import DataFrame

from ics_utils import column_name_to_index, generate_excel_columns


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




def save_2_excel_with_template(data, template_file, output_file, sheet_name=None,
                               column_mapping=None, index=False, header=False, startrow=0, startcol=0):
    """
    保存DataFrame到Excel文件，使用模板格式。
    :param data: 要保存的DataFrame 或者 字典列表
    :param template_file: 模板文件路径
    :param output_file: 输出文件路径
    :param sheet_name: 工作表名称，默认为None,采用active sheet
    :param column_mapping: 列名映射字典，用于重命名DataFrame的列名，默认为None
    :param index: 是否保存索引，默认为False
    :param header: 是否保存列名，默认为False
    :param startrow: 开始写入数据的行号，默认为0
    :param startcol: 开始写入数据的列号，默认为0
    """

    if type(data) is not DataFrame:
        data = pd.DataFrame(data)

    # 使用 openpyxl 加载模板文件
    workbook = load_workbook(template_file)
    if not sheet_name:
        sheet = workbook.active
    else:
        sheet = workbook.sheet_name
    # 先将模板内容复制到新文件
    workbook.save(output_file)

    max_column = max([column_name_to_index(col) for col in column_mapping.values()])
    # 创建一个空的 DataFrame，包含所有可能的列
    empty_columns = generate_excel_columns(max_column)
    mapped_df = pd.DataFrame(columns=empty_columns)

    # 将原始数据映射到新 DataFrame 的指定列
    for df_col, excel_col in column_mapping.items():
        mapped_df[excel_col] = data[df_col]


    # 使用 to_excel 方法将数据写入模板
    with pd.ExcelWriter(output_file, engine="openpyxl", mode='a', if_sheet_exists='overlay') as writer:
        # # 将映射后的 DataFrame 写入指定位置
        mapped_df.to_excel(writer, startrow=startrow, startcol=startcol, index=index, header=header)

