# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name="Code Katas",
    description="Solutions to various code challenges",
    version=0.1,
    author="Mike Harrison",
    license='MIT',
    py_modules=[
        'airports',
    ],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest']}
)
