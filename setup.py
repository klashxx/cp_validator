# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='cp_validator',
    author='Juan Diego Godoy Robles',
    url='https://klashxx.github.io/',
    author_email='klashxx@gmail.com',
    packages=['cp_validator'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    package_data={'cp_validator': ['static/*']}
)

