# 资源管理
# -*- coding: UTF-8 -*-
from automation_frame.test_business.web_4_resource_management import ResourceManagementPage
from automation_frame.test_parse_data.prase_data import DataParse
import unittest,time
from parameterized import parameterized
from automation_frame.test_business.web_4_login_page import LogInPage


class ResourceManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ResourceManagementPage().resource_button()#资源管理
    def setUp(self):
        #先获得一个类属性
        self.resourcepage = ResourceManagementPage()#实例化生成了资源管理页面对象

    #培训资源解密
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("train_resource_decode")
    @parameterized.parameterized.expand(mydata)
    def test_a1_train_decode(self,tittle, mylist, expected):
        self._testMethodDoc = tittle
        self.resourcepage.train_resource_button()  # 培训资源
        time.sleep(2)
        self.resourcepage.train_resource_decode()#解密
        time.sleep(0.5)
        self.resourcepage.train_resource_input(mylist[0])#输入密码
        self.resourcepage.train_resource_affirm()#确定
        time.sleep(0.5)
        result = self.resourcepage.look_train_resource_decode()#断言
        assert expected in result


    #区域下拉框功能
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("train_resource_area")
    @parameterized.parameterized.expand(mydata)
    def test_a2_train_resource_lib(self, tittle, mylist, expected):
        self._testMethodDoc = tittle
        self.resourcepage.train_area_select(mylist[0])
        result = self.resourcepage.look_train_area_select()
        assert expected in result


    #检查资源管理的培训资源的资源库下拉框
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("train_resource_resource_lib")
    @parameterized.parameterized.expand(mydata)
    def test_a3_train_resource_lib(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.resourcepage.train_lib_select(mylist[0])
        result = self.resourcepage.look_train_lib_select()
        assert expected in result

    #跟踪资源成功
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("train_resource_tail_resource")
    @parameterized.parameterized.expand(mydata)
    def test_a4_train_resource_tail_save(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        time.sleep(1)
        self.resourcepage.train_resource_tail_button()#跟踪资源
        time.sleep(1)
        self.resourcepage.train_resource_tail_taile_button()#跟踪资源跟踪资源
        time.sleep(0.5)
        self.resourcepage.train_resource_tail_status_select(mylist[0])#状态
        self.resourcepage.train_resource_tail_leval_select(mylist[1])#优先级别
        self.resourcepage.train_resource_next_tail_time_input(mylist[2])#下次跟踪输入框
        self.resourcepage.train_resource_text_content_input(mylist[3])#跟踪内容
        time.sleep(0.5)
        self.resourcepage.train_resource_read_class_select(mylist[4])#入读班级
        self.resourcepage.train_resource_pay_money_select(mylist[5])#应交学费
        self.resourcepage.train_resource_pay_way_select(mylist[6])#支付方式
        self.resourcepage.train_resource_pay_account_select(mylist[7])#收入账户
        self.resourcepage.train_resource_tail_save_button()#保存
        time.sleep(1)
        result = self.resourcepage.look_train_resource_tail()#断言
        self.resourcepage.train_resource_tail_affirm_button()#确定
        assert expected in result

    #修改资源成功
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("train_resource_update")
    @parameterized.parameterized.expand(mydata)
    def test_a5_train_resource_update(self,tittle,text,expected):
        self._testMethodDoc = tittle
        self.resourcepage.train_resource_update_button()#修改操作
        time.sleep(1)
        self.resourcepage.train_resource_update_end_tail_textarea(text=text)#最后跟踪文本域
        time.sleep(1)
        self.resourcepage.train_resource_update_save_button()#保存
        time.sleep(0.5)
        result = self.resourcepage.look_update_resource()#断言
        assert expected in result


    # # 输入分配时间,搜索成功
    # mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("train_resource_time_search")
    # @parameterized.parameterized.expand(mydata)
    # def test_a6_train_resource_search(self, tittle, mylist, expected):
    #     self._testMethodDoc = tittle
    #     self.resourcepage.train_stat_time_input(mylist[0])  # 开始时间
    #     self.resourcepage.train_end_time_input(mylist[1])  # 结束时间
    #     self.resourcepage.train_search()  # 搜索
    #     time.sleep(2)
    #     result = self.resourcepage.look_train_search()  # 断言
    #     self.resourcepage.train_resource_button()#培训资源
    #     time.sleep(1)
    #     assert expected in result


    #废弃资源成功
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("train_resource_waste")
    @parameterized.parameterized.expand(mydata)
    def test_a7_train_resource_waste(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.resourcepage.train_resource_button()#培训资源
        time.sleep(1)
        stu_name = self.resourcepage.train_resource_waste_student()#选中学生
        self.resourcepage.train_resource_waste_buttn()#废弃
        time.sleep(0.5)
        self.resourcepage.train_resource_waste_yes()#废弃确认
        time.sleep(0.5)
        result = self.resourcepage.look_train_resource_waste(stu_name)#断言
        assert expected in result

    #新增培训资源
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("train_resource_add")
    @parameterized.parameterized.expand(mydata)
    def test_a8_train_resource_add(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.resourcepage.train_add_resource_buttob()#新增
        time.sleep(1)
        self.resourcepage.train_phone_input(mylist[0])#电话
        self.resourcepage.train_name_input(mylist[1])#姓名
        self.resourcepage.train_status_select(mylist[2])#状态下拉框
        self.resourcepage.train_source_select(mylist[3])#渠道下拉框
        time.sleep(0.5)
        self.resourcepage.train_add_resource_save_button()#保存
        result = self.resourcepage.look_add_resource_save()#断言
        assert expected in result



###分配资源###
    #注销登录(切换账号)成功
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("allot_resource_consult_login")
    @parameterized.parameterized.expand(mydata)
    def test_b1_allot_resource_consult_login(self,tittle, mylist, expected):
        self._testMethodDoc = tittle
        self.resourcepage.logout()#注销
        time.sleep(2)
        loginpage = LogInPage()#登录页面
        loginpage.login_username(mylist[0])
        loginpage.login_password(mylist[1])
        loginpage.login_verifycode(mylist[2])
        loginpage.login_button()
        result = loginpage.look_login()  # 断言
        assert expected in result

    #咨询主管分配资源解密
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("allot_resource_consult_decode")
    @parameterized.parameterized.expand(mydata)
    def test_b2_allot_decode(self, tittle, mylist, expected):
        self._testMethodDoc = tittle
        self.resourcepage.consult_resource_manage_button()#咨询主管资源管理
        time.sleep(0.5)
        self.resourcepage.consult_resource_manage_allocate_button()  # 咨询主管分配资源
        time.sleep(2)
        self.resourcepage.train_resource_decode()  # 解密
        time.sleep(0.5)
        self.resourcepage.train_resource_input(mylist[0])  # 输入密码
        self.resourcepage.train_resource_affirm()  # 确定
        time.sleep(0.5)
        result = self.resourcepage.look_train_resource_decode_two()  # 断言
        assert expected in result

    # 咨询主管分配简历
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("allot_resource_ratio_allot")
    @parameterized.parameterized.expand(mydata)
    def test_b3_allot_resume_submit(self,tittle, mylist, expected):
        self._testMethodDoc = tittle
        self.resourcepage.allot_resource_first_check()#勾选
        self.resourcepage.allot_resource_resume_select(mylist[0])#分配简历
        self.resourcepage.allot_resource_submit_button()#提交
        time.sleep(0.5)
        self.resourcepage.allot_resource_submit_again_button()#二次确定
        time.sleep(0.5)
        result = self.resourcepage.look_allot_resource_submit()#断言
        time.sleep(0.5)
        self.resourcepage.allot_resource_submit_third_button()#三次确定
        time.sleep(0.5)
        assert expected in result

    #按比例分配(输入比例,提交)
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("allot_resource_ratio_input")
    @parameterized.parameterized.expand(mydata)
    def test_b4_allot_resource_ratio_alert(self,tittle,mylist,expected):
        self._testMethodDoc = tittle
        self.resourcepage.allot_resource_ratio_allot()  # 按比例分配
        time.sleep(1)
        self.resourcepage.allot_resource_ratio_input(mylist[0])#修改比例
        self.resourcepage.allot_resource_ratio_submit()#按比例分配提交
        time.sleep(1)
        self.resourcepage.allot_resource_ratio_submit_affirm()#按比例分配确定按钮
        time.sleep(1)
        result = self.resourcepage.look_ratio_allot()#断言
        self.resourcepage.allot_resource_ratio_submit_two_affirm()#二次确定
        assert expected in result

#登录(切换回账号)成功
    mydata = DataParse("../../test_data/data_web_4.xlsx").parse_excel_datas("cut_login")
    @parameterized.parameterized.expand(mydata)
    def test_b5_allot_resource_admin_login(self,tittle, mylist, expected):
        self._testMethodDoc = tittle
        self.resourcepage.logout()#注销
        time.sleep(2)
        loginpage = LogInPage()#登录页面
        loginpage.login_username(mylist[0])
        loginpage.login_password(mylist[1])
        loginpage.login_verifycode(mylist[2])
        loginpage.login_button()
        result = loginpage.look_login()  # 断言
        assert expected in result

    
    def test_b6_Access_to_public_resources (self):
        self._testMethodDoc='进入公共资源模块'
        self.resourcepage.Access_to_public_resources()

    loginfo=DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('公共资源区域下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_b7_Common_resources_area_drop_down_box(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.resourcepage.Common_resources_area_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('公共资源部门下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_b8_Public_resources_department_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Public_resources_department_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('公共资源最后废弃人下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_b9_Drop_down_box_of_the_last_abandoned_public_resources(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Drop_down_box_of_the_last_abandoned_public_resources(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('公共资源状态下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_c1_Public_resource_status_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Public_resource_status_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('公共资源来源下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_c2_Public_resource_source_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Public_resource_source_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('公共资源学历下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_c3_Public_resources_education_dropdown_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Public_resources_education_dropdown_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('公共资源查询输入框')
    @parameterized.parameterized.expand(loginfo)
    def test_c4_Public_resource_query_input_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Public_resource_query_input_box(arg2[0])

    def test_c5_Query_button(self):
        self._testMethodDoc = '公共资源查询按钮'
        self.resourcepage.Query_button()
        assert '成都' in self.resourcepage.assert_Query_button()

    def test_c6_Public_resource_claim(self):
        self._testMethodDoc='公共资源认领'
        time.sleep(2)
        self.resourcepage.Public_resource_claim()
        assert '已成功认领' in self.resourcepage.assert_Public_resource_claim()

    def test_c7_Transfer_of_resources(self):
        self._testMethodDoc='进入转交资源模块'
        self.resourcepage.Transfer_of_resources()
        assert '转交资源' in self.resourcepage.assert_Transfer_of_resources()

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源查询区域下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_c8_Query_area_drop_down_box(self,arg1,arg2,arg3):
        self._testMethodDoc=arg1
        self.resourcepage.Query_area_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源查询部门下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_c9_Query_Department_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Query_Department_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源查询咨询师下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_d1_Query_consultant_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Query_consultant_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源查询状态下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_d2_Query_status_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Query_status_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源查询来源下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_d3_Query_source_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Query_source_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源查询输入框')
    @parameterized.parameterized.expand(loginfo)
    def test_d4_Transfer_resource_query_input_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Transfer_resource_query_input_box(arg2[0])

    def test_d5_Transfer_resource_inquiry(self):
        self._testMethodDoc='转交资源查询'
        self.resourcepage.Transfer_resource_inquiry()

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源转交区域下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_d6_Transfer_area_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Transfer_area_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源转交部门下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_d7_Transfer_department_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Transfer_department_drop_down_box(arg2[0])

    loginfo = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('转交资源转交咨询师下拉框')
    @parameterized.parameterized.expand(loginfo)
    def test_d8_Transfer_to_consultant_drop_down_box(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        self.resourcepage.Transfer_to_consultant_drop_down_box(arg2[0])

    def test_d9_see(self):
        self._testMethodDoc = '查看资源'
        self.resourcepage.see()
        assert '查看简历' in self.resourcepage.assert_see()

    def test_e1_Forward_resource_submission(self):
        self._testMethodDoc='转交资源'
        self.resourcepage.Forward_resource_submission()
        assert '转交资源完成' in self.resourcepage.assert_Forward_resource_submission()





