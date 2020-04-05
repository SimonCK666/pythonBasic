#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin

# Relative path

path = Path("ecommerce")
print(path.exists())

print('------------------')

path1 = Path()
# Pack everything in the directory
for file in path1.glob('*.py'):
    print(file)
print('------------------')
for file in path1.glob('*'):
    print(file)