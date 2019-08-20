#!/usr/bin/python

import filecmp
import click
import os
import shutil


dc = filecmp.dircmp('test1', 'test2')
common_files = ','.join(dc.common)
left_only_files = ','.join(dc.left_only)
right_only_files = ','.join(dc.right_only)
with open('diff.txt','w') as report:
      report.write('Common files: ' +common_files+'\n')
      report.write('\n'+'Only in test1 folder: '+left_only_files)
      report.write('\n'+'Only in test2 folder: '+right_only_files)
      report.write('\n')
