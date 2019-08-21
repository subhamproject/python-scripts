#!/usr/bin/python

import os

script_path = os.path.dirname(os.path.abspath( __file__ ))
script = os.path.dirname(os.path.realpath( __file__ ))
print(script_path)
print(script)
print(__file__)

__file__ is a script name ..similar to $0 in shell
