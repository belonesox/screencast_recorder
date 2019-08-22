#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Setup for the package
"""

from setuptools import setup
setup(
    entry_points={
        'console_scripts': [
            'screencast_recorder=screencast_recorder:main',
        ],
    },
    name='screencast_recorder',
    version='0.01',
    packages=['screencast_recorder'],
    author_email = "stanislav.fomin@gmail.com",
    install_requires=[
        'python-xlib'
    ],
)

