# coding: utf-8
"""
@Author: Robby
@Module name: setup.py
@Create date: 2020-06-06
@Function: 
"""

import os
from setuptools import setup

def package_data(pkg, roots=tuple()):
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                print(os.path.relpath(os.path.join(dirname, fname), pkg))
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))
    return {pkg: data}

with open("README.md", "r") as f:
  long_description = f.read()

setup(
    name = 'influxdb-async',
    author = 'Robby',
    author_email = 'yinhuanyicn@gmail.com',
    url = 'https://github.com/yinhuanyi/zabbix-feishu-alert',
    license = "MIT",
    version = '1.0.0',
    description = 'async data to influxdb',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = [
        'influxdb_async',
    ],
    install_requires = [
        'influxdb',
    ],
    dependency_links = [],
    package_data = package_data("influxdb_async",),
)