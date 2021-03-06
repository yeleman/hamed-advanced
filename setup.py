#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

""" Allow any django app to handle SMS-MO, SMS-MT using the Orange API. """

from codecs import open

from setuptools import setup, find_packages

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='hamed_advanced',
    version='1.2',
    description="Simple pair of cipher/decipher functions "
                "for hamed advanced mode",
    long_description=readme,
    author='renaud gaudin',
    author_email='rgaudin@gmail.com',
    url='http://github.com/yeleman/hamed-advanced',
    keywords="hamed",
    license="Public Domain",
    packages=find_packages('.'),
    zip_safe=False,
    platforms='any',
    include_package_data=True,
    package_data={'': ['README.rst', 'LICENSE']},
    package_dir={'hamed_advanced': 'hamed_advanced'},
    install_requires=[
    ],
    entry_points={
        'console_scripts': ['hamed-advanced=hamed_advanced:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-pep8'
    ],
)
