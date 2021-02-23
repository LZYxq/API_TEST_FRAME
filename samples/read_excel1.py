#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: read_excel.py
# @time: 2020/7/1 9:13 下午

import os
import xlrd
from common.excel_utils import ExcelUtils

# excel_path = os.path.join( os.path.dirname(__file__) , 'data/test_data.xlsx' )
excel_path = os.path.join( os.path.dirname(__file__) , 'data/datashell.xls' )
excelUtils = ExcelUtils(excel_path,"Sheet1")
print(excelUtils.get_merged_cell_value(4,0) )
print(excelUtils.get_row_count())
sheet_list = []
for row in range(1,excelUtils.get_row_count()): #s
    row_dict = {}
    row_dict["事件"] = excelUtils.get_merged_cell_value(row,0)
    row_dict["步骤序号"] = excelUtils.get_merged_cell_value(row, 1)
    row_dict["步骤操作"] = excelUtils.get_merged_cell_value(row, 2)
    row_dict["完成情况"] = excelUtils.get_merged_cell_value(row, 3)
    # row_dict["事件"] = excelUtils.get_merged_cell_value(row, 0)
    # row_dict["自欧典二"] = excelUtils.get_merged_cell_value(row, 1)
    # row_dict["字段三"] = excelUtils.get_merged_cell_value(row, 2)
    # row_dict["四"] = excelUtils.get_merged_cell_value(row, 3)
    # row_dict["五"] = excelUtils.get_merged_cell_value(row, 4)
    sheet_list.append( row_dict )
#
# for row in sheet_list:
#     print( row )

all_data_list = []
first_row = excelUtils.sheet.row(0)
# print( first_row )
for row in range(1,excelUtils.get_row_count()):
    row_dict = {}
    for col in range(0,excelUtils.get_col_count()):
        row_dict[first_row[col].value] = excelUtils.get_merged_cell_value(row,col)
    all_data_list.append( row_dict )

for row in all_data_list:
    print( row )

