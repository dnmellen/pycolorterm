#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pycolorterm',
    version='0.1.1',
    description='PyColorTerm allows you to write colored and styled lines out in the terminal from Python and in a pythonic way',
    long_description=readme + '\n\n' + history,
    author='Diego Navarro Mellén',
    author_email='dnmellen@gmail.com',
    url='https://github.com/dnmellen/pycolorterm',
    packages=[
        'pycolorterm',
    ],
    package_dir={'pycolorterm': 'pycolorterm'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='pycolorterm',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)