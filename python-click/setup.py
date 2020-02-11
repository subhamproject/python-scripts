#!/usr/bin/python3
#https://kushaldas.in/posts/building-command-line-tools-in-python-with-click.html
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
