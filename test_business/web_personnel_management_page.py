# -*- coding: UTF-8 -*-
from selenium.common.exceptions import NoSuchElementException
from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
import time

class PersonnelPage(BasePage):

    def __init__(self):
        super(PersonnelPage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')  # 实例化一个读取配置文件对象

    def personnel_button(self):#导航栏人事管理按钮
        #获取元素配置
        locator = self.config.parse_config("Navigation_personnel_management2.5",'personnel_management')
        self.click(*locator)#点击跳转人事管理

    def staff_button(self):#员工管理按钮
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'staff_management')
        self.click(*locator)

    def area_select(self,value):#区域下拉框
        locator = self.config.parse_config("Navigation_personnel_management2.5",'area_select')
        self.select_text_option(*locator,text=value)

    def status_select(self):#状态下拉框
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'status_select')
        self.select_text_option(*locator, text='在职')

    def username_input(self,name):#输入姓名
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'username_input')
        self.input_text(*locator,value=name)

    def inquire_button(self):#查询
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'inquire')
        self.click(*locator)

    def clear_input(self):#清空输入
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'username_input')
        self.ele_text_clear(*locator)

    def add_staff_button(self):#点击新增员工按钮
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_staff')
        self.click(*locator)

    def add_area_select(self,value):#新增员工区域下拉框
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_area_select')
        self.select_text_option(*locator,text=value)

    def add_department_selecct(self,value):#新增员工部门下拉框
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_department_selecct')
        self.select_text_option(*locator, text=value)

    def add_staff_name(self,name):#新增员工姓名
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_staff_name')
        self.input_text(*locator, value=name)

    def add_staff_work_id(self,id):#新增员工工号
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_work_id')
        self.input_text(*locator, value=id)

    def add_staff_position(self,position):#新增员工职位
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_position')
        self.input_text(*locator, value=position)

    def add_sex_selecct(self,value):#新增员工性别下拉框
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_sex')
        self.select_text_option(*locator, text=value)

    def add_staff_phone_number(self,phone):#新增员工电话号码
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_staff_phone_number')
        self.input_text(*locator, value=phone)

    def add_save(self):#新增员工保存
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'add_save')
        self.click(*locator)

    def modification_staff(self):#员工信息修改
        locator = self.config.parse_config("Navigation_personnel_management2.5", 'modification_staff')
        self.click(*locator)






# -----断言部分---------------------------------------------------------------------------------------------
    def personne_button_assert(self):#人事管理按钮页面跳转断言
        locator = self.config.parse_config('Navigation_personnel_management2.5', 'staff_management')  # 获得断言用的元素配置
        time.sleep(5)
        try:
            result = self.get_ele_text(*locator)  # 返回元素内容text
        except NoSuchElementException:
            return " "
        else:
            return result
# -----断言部分---------------------------------------------------------------------------------------------
    def inquire_username_assert(self):#员工姓名查询结果断言
        locator = self.config.parse_config('Navigation_personnel_management2.5', 'inquire_username_assert')  # 获得断言用的元素配置
        time.sleep(3)
        try:
            result = self.get_ele_text(*locator)  # 返回元素内容text
        except NoSuchElementException:
            return " "
        else:
            return result
# -----断言部分---------------------------------------------------------------------------------------------
    def area_select_assert(self):#区域下拉框断言
        locator = self.config.parse_config('Navigation_personnel_management2.5', 'area_select')  # 获得断言用的元素配置
        time.sleep(3)
        try:
            result = self.get_ele_text(*locator)  # 返回元素内容text
        except NoSuchElementException:
            return " "
        else:
            return result
# -----断言部分---------------------------------------------------------------------------------------------
    def area_select_assert(self):#区域下拉框断言
        locator = self.config.parse_config('Navigation_personnel_management2.5', 'add_staff_assert')  # 获得断言用的元素配置
        time.sleep(3)
        try:
            result = self.get_ele_text(*locator)  # 返回元素内容text
        except NoSuchElementException:
            return " "
        else:
            return result
# -----断言部分---------------------------------------------------------------------------------------------