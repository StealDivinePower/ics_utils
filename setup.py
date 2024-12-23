# -*- coding: utf-8 -*-
"""
@author: hanyanling
@date: 2024/5/21 下午5:38
@email:
---------
@summary:
"""


from setuptools import setup, find_packages

packages = find_packages()


def readme_file(param):
    # 读取文件内容
    return open(param, 'r').read()


setup(
    name='ics_utils',
    version='0.0.4',
    author='hanyanling',
    description="爬虫工具包",
    long_description=readme_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/StealDivinePower/ics_utils',
    packages=packages,
    python_requires='>=3.6',
    requires=[
        'requests',
    ]
)