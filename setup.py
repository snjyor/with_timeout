# -*- coding: utf8 -*-
from setuptools import setup
from os import path
import io
abs_path = path.abspath(path.dirname(__file__))
with io.open(path.join(abs_path, 'README.md'), encoding='utf-8') as f:
    longdesc = f.read()

setup(
    name='with_timeout',
    py_modules=['with_timeout'],
    version='0.1.7',
    description='Conservatively convert html to markdown',
    author='David Lönnhager',
    author_email='dv.lnh.d@gmail.com',
    url='https://github.com/dlon/html2markdown',
    install_requires=[
        'beautifulsoup4'
    ],
    long_description=longdesc,
    long_description_content_type='text/x-rst',
)