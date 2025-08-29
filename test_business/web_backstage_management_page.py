# -*- coding: UTF-8 -*-
from selenium.common.exceptions import NoSuchElementException
from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
import time

class BackManaPage(BasePage):

    def __init__(self):
        super(BackManaPage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')  # 实例化一个读取配置文件对象

    def backstage_button(self):# 点击跳转后台管理
        locator = self.config.parse_config("BackStageManagement2.5", 'backstage_button')
        self.click(*locator)

    def role_management_button(self):# 点击跳转角色管理
        locator = self.config.parse_config("BackStageManagement2.5", 'role_management')
        self.click(*locator)

    def add_role(self):#角色管理新增角色按钮
        locator = self.config.parse_config("BackStageManagement2.5", 'add_role')
        self.click(*locator)

    def add_role_name(self,name):#新增角色名
        locator = self.config.parse_config("BackStageManagement2.5", 'add_role_name')
        self.input_text(*locator,value=name)

    def add_role_describe(self,describe):#新增角色描述
        locator = self.config.parse_config("BackStageManagement2.5", 'add_role_describe')
        self.input_text(*locator,value=describe)

    def add_save_role(self):#新增角色保存
        locator = self.config.parse_config("BackStageManagement2.5", 'add_save_role_button')
        self.click(*locator)

    def add_confirm(self):  # 新增保存确认
        locator = self.config.parse_config("BackStageManagement2.5", 'add_confirm')
        self.click(*locator)

    def user_management_button(self):#点击跳转用户管理
        locator = self.config.parse_config("BackStageManagement2.5", 'user_management')
        self.click(*locator)

    def dictionary_management_button(self):#点击跳转字典管理
        locator = self.config.parse_config("BackStageManagement2.5", 'The_dictionary_management')
        self.click(*locator)












# -----断言部分---------------------------------------------------------------------------------------------
    def menu_button_assert(self):  # 人事管理按钮页面跳转断言
        locator = self.config.parse_config('BackStageManagement2.5', 'menu_assert')  # 获得断言用的元素配置
        time.sleep(5)
        try:
            result = self.get_ele_text(*locator)  # 返回元素内容text
        except NoSuchElementException:
            return " "
        else:
            return result
# -----断言部分---------------------------------------------------------------------------------------------













