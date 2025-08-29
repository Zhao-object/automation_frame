# 后台管理
# -*- coding: UTF-8 -*-
from automation_frame.test_business.web_backstage_management_page import BackManaPage
import unittest,time

from parameterized import parameterized

class BackStageManagement(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("-" * 20 + "开始测试一条用例(API)" + "-" * 20)
        #先获得一个类属性
        self.backstageManagementpage = BackManaPage()#实例化生成get了 一次url 的 登录页面对象

    def test_01_backstage_button(self):
        self._testMethodDoc = '进入后台管理界面'
        time.sleep(5)
        self.backstageManagementpage.backstage_button()  # 点击人事管理按钮
        print('点击后台管理按钮')
        assert '菜单管理' in self.backstageManagementpage.menu_button_assert()

    def test_02_role_management_button(self):
        self._testMethodDoc = '进入角色管理界面'
        time.sleep(5)
        self.backstageManagementpage.role_management_button()

    def test_03_add_role_button(self):
        self._testMethodDoc = '点击新增按钮'
        self.backstageManagementpage.add_role()

    def test_04_add_role_name(self):
        self._testMethodDoc = '新增角色名'
        time.sleep(5)
        self.backstageManagementpage.add_role_name('系统管理（伪）')

    def test_05_add_role_describe(self):
        self._testMethodDoc = '新增角色描述'
        time.sleep(5)
        self.backstageManagementpage.add_role_describe('实验数据')

    def test_06_add_role_button(self):
        self._testMethodDoc = '新增角色保存按钮,确认保存按钮'
        time.sleep(3)
        self.backstageManagementpage.add_save_role()
        time.sleep(3)
        self.backstageManagementpage.add_confirm()


    # def test_07_user_management_button(self):
    #     self._testMethodDoc = '进入用户管理界面'
    #     time.sleep(5)
    #     self.backstageManagementpage.user_management_button()
    #
    # def test_08_dictionary_management_button(self):
    #     self._testMethodDoc = '进入字典管理界面'
    #     time.sleep(3)
    #     self.backstageManagementpage.dictionary_management_button()




    # info = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('员工管理区域')
    # @parameterized.parameterized.expand(info)
    # def test_02_area(self,arg1,arg2,arg3):
    #     time.sleep(3)
    #     self.personnelManagementpage.area_select(arg2[0])#区域下拉框选择
    #     self._testMethodDoc = arg1
    #     print(arg1)

    @classmethod
    def tearDown(self):
        print("-" * 20 + "结束测试一条用例(API)" + "-" * 20)
