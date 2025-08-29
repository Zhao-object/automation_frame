# 人事管理
# -*- coding: UTF-8 -*-
from automation_frame.test_business.web_personnel_management_page import PersonnelPage
from automation_frame.test_parse_data.prase_data import DataParse
import unittest,time
from parameterized import parameterized

class PersonnelManagement(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("-" * 20 + "开始测试一条用例(API)" + "-" * 20)
        #先获得一个类属性
        self.personnelManagementpage = PersonnelPage()#实例化生成get了 一次url 的 登录页面对象

    def test_01_button(self):
        #这个类所有的实例都有那个类属性
        self._testMethodDoc = '进入人事管理界面'
        self.personnelManagementpage.personnel_button()#点击人事管理按钮
        print('点击人事管理按钮')
        assert '员工管理' in self.personnelManagementpage.personne_button_assert()

    info = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('员工管理区域')
    @parameterized.parameterized.expand(info)
    def test_02_area(self,arg1,arg2,arg3):
        time.sleep(3)
        self.personnelManagementpage.area_select(arg2[0])#区域下拉框选择
        self._testMethodDoc = arg1
        print(arg1)
        # assert arg3 in self.personnelManagementpage.area_select_assert()

    def test_03_status(self):
        self.personnelManagementpage.status_select()#状态下拉框选择
        print('状态下拉框选择')
        self._testMethodDoc = '状态下拉框选择-在职'

    info = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('员工管理查询')
    @parameterized.parameterized.expand(info)
    def test_04_username_input(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        print(arg1,arg2[0])
        self.personnelManagementpage.username_input(arg2[0])#输入员工名
        time.sleep(3)
        self.personnelManagementpage.inquire_button()#点击查询
        assert arg3 in self.personnelManagementpage.inquire_username_assert()
        time.sleep(3)
        self.personnelManagementpage.clear_input()#清除输入框

    def test_05_add_staff(self):
        self._testMethodDoc='新增员工按钮'
        self.personnelManagementpage.add_staff_button()
        assert '新增员工' in self.personnelManagementpage.area_select_assert()

    info = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('新增员工区域选择')
    @parameterized.parameterized.expand(info)
    def test_06_add_area_select(self,arg1,arg2,arg3):#新增员工区域选择下拉框
        self._testMethodDoc=arg1
        print(arg1,arg2[0])
        time.sleep(3)
        self.personnelManagementpage.add_area_select(arg2[0])

    info = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('新增员工部门选择')
    @parameterized.parameterized.expand(info)
    def test_07_add_department(self,arg1,arg2,arg3):#新增员工部分选择下拉框
        self._testMethodDoc=arg1
        print(arg1, arg2[0])
        time.sleep(3)
        self.personnelManagementpage.add_department_selecct(arg2[0])

    def test_08_add_staff_name(self):#新增员工姓名
        self._testMethodDoc='新增员工姓名'
        time.sleep(2)
        self.personnelManagementpage.add_staff_name('椿')

    def test_09_add_staff_work_id(self):#新增员工工号
        self._testMethodDoc='新增员工工号'
        time.sleep(2)
        self.personnelManagementpage.add_staff_work_id('WNCQ928')

    def test_10_add_staff_position(self):#新增员工职位,性别,电话号码
        self._testMethodDoc = '新增员工职位,性别,电话号码'
        time.sleep(2)
        self.personnelManagementpage.add_staff_position('讲师')
        self.personnelManagementpage.add_sex_selecct('女')
        self.personnelManagementpage.add_staff_phone_number('16676766655')

    def test_11_add_save(self):#新增员工保存
        self._testMethodDoc = '新增员工信息保存'
        self.personnelManagementpage.add_save()

    # def test_12_modification_staff(self):#员工信息修改
    #     self._testMethodDoc='员工信息修改'
    #     self.personnelManagementpage.modification_staff()



    @classmethod
    def tearDown(self):
        print("-" * 20 + "结束测试一条用例(API)" + "-" * 20)
















    @classmethod
    def tearDown(self):
        print("-" * 20 + "结束测试一条用例(API)" + "-" * 20)


if __name__ == '__main__':
    unittest.main()