#!/usr/bin/python3

from setuptools import setup

setup(
    name="mygroup",
    version='0.1.2',
    description='The Subham Test Framework',
    url='https://github.com/subhamproject/rcx-jenkins',
    author='Subham Mandal',
    author_email='subham.devops@gmail.com',
    py_modules=['mygroup'],
    install_requires=[
        'Click','click-shell',
    ],
    entry_points='''
        [console_scripts]
        mygroup=mygroup:main
    ''',
)
