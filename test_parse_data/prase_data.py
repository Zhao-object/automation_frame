# -*- coding: utf-8 -*-
import xlrd

class DataParse(object):

    def __init__(self,filename='../../test_data/data_web.xls'):
        #传入文件名
        self.filename = filename
    def parse_excel_datas(self, sheetname):  # 传入表名
        try:
            # 打开excel文件
            workbook = xlrd.open_workbook(filename=self.filename)
            # 根据表名获取表
            sheet1 = workbook.sheet_by_name(sheet_name=sheetname)
        except Exception as ex:
            print("打开测试数据文件错误:", ex)
        # 读取表中的行数
        try:
            row = sheet1.nrows
        except Exception as ex:
            print("错误:",ex)
        # 读取表中的列数
        col = sheet1.ncols
        if col == 3:
            ori_list = []  # 定义一个空列表
            for row in range(1, row):  # 循环取值
                value = sheet1.row_values(row)  # 将取出的值赋值给value
                ori_list.append(value)  # 追加到列表
            for i in ori_list:  # 循环把每个元素的第二个值变成字典格式的
                dic = eval(i[1])
                i[1] = dic  # 改变列表的元素
            print("9")
        elif col == 4:
            ori_list = []  # 定义一个空列表
            for row in range(1, row):  # 循环取值
                value = sheet1.row_values(row)  # 将取出的值赋值给value
                ori_list.append(value)  # 追加到列表
            for i in ori_list:  # 循环把每个元素的第二个值变成字典格式的
                dic = eval(i[1])
                i[1] = dic  # 改变列表的元素
                dic1 = eval(i[2])
                i[2] = dic1
        else:
            ori_list = []  # 定义一个空列表
            for row in range(1, row):  # 循环取值
                value = sheet1.row_values(row)  # 将取出的值赋值给value
                ori_list.append(value)  # 追加到列表
            # print("内容:",ori_list)
            for i in ori_list:  # 循环把每个元素的第二个值变成字典格式的
                dic = eval(i[1])
                i[1] = dic  # 改变列表的元素wwwwwww
                dic1 = eval(i[2])
                i[2] = dic1
                dic2 = eval(i[3])
                i[3] = dic2
        return ori_list
if __name__ == '__main__':
    a = DataParse(r"D:\automation_frame\test_data\data_web.xls").parse_excel_datas('weblogin')
    print(a)


