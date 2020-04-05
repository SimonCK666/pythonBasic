#!/usr/bin/env python
# -*- coding:utf-8 -*-

import openpyxl as xl

wb = xl.load_workbook('sheets.xlsx')
sheet = wb['Sheet1']

# find the special cell
cell = sheet['a1']
cell = sheet.cell(1, 1)
print(cell.value)

