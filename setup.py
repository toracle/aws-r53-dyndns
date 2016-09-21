#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='aws-r53-dyndns',
    version='0.1.0',
    description=u'',
    author='Jeongsoo Park',
    author_email='toracle@gmail.com',
    url='https://github.com/toracle/aws-r53-dyndns',
    packages=find_packages(),
    install_requires=[
        'boto',
    ],
    entry_points={
        'console_scripts': [
            'aws-r53-dyndns=aws_r53_dyndns.main:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
)
