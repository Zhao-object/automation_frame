# 学员管理
# -*- coding: UTF-8 -*-
from automation_frame.test_business.web_4_participants_management import ParticipantsManagementPage
from automation_frame.test_parse_data.prase_data import DataParse
import unittest,time
from parameterized import parameterized

class ParticipantsManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ParticipantsManagementPage().participants_management_button()  #学员管理

    def setUp(self):
        print("-" * 20 + "开始测试一条用例(API)" + "-" * 20)
        #先获得一个类属性
        self.Participant = ParticipantsManagementPage()#实例化生成教学管理页面对象

    # # ------------------------------------------------------------------------------------------------------------------
    def test_a1_participants_management_button(self):
        self._testMethodDoc = '打开学员管理导航菜单'
        self.Participant.participants_management_button()
    #
    # # --------进入学员信息界面--------------------------------------------------------------------------------------------
    def test_a2_student_info_button(self):
        self._testMethodDoc = '进入学员信息界面'
        self.Participant.student_info_button()
        assert '学员信息' in self.Participant.assert_go_studentinfo()

    info = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('学员信息区域')
    @parameterized.parameterized.expand(info)
    def test_a3_student_area_select(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        self.Participant.student_area_select(arg2[0])
        print(self.Participant.assert_areainfo())
        assert arg3 in self.Participant.assert_areainfo()

    info = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('学员信息方向')
    @parameterized.parameterized.expand(info)
    def test_a4_student_orientation_select(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        self.Participant.student_orientation_select(arg2[0])
        print(self.Participant.assert_orientation())
        assert arg3 in self.Participant.assert_orientation()

    info = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('学员信息班级')
    @parameterized.parameterized.expand(info)
    def test_a5_student_class_select(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        self.Participant.student_class_select(arg2[0])
        print(self.Participant.assert_class())
        assert arg3 in self.Participant.assert_class()

    info = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('学员信息状态')
    @parameterized.parameterized.expand(info)
    def test_a6_student_status_select(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        self.Participant.student_status_select(arg2[0])
        print(self.Participant.assert_status())
        assert arg3 in self.Participant.assert_status()

    info = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('学员信息姓名搜索')
    @parameterized.parameterized.expand(info)
    def test_a7_student_name_select(self,arg1,arg2,arg3):#输入姓名搜索
        self._testMethodDoc = arg1
        self.Participant.input_search_name(arg2[0])
        self.Participant.search_button()


    info = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('学员信息姓名搜索')
    @parameterized.parameterized.expand(info)
    def test_a8_student_name_select(self,arg1,arg2,arg3):#无前置条件-直接点击搜索
        self._testMethodDoc = arg1
        self.Participant.student_sweep_away()
        self.Participant.input_search_name(arg2[0])
        time.sleep(3)
        self.Participant.search_button()

    def test_a9_decode_button(self):
        self._testMethodDoc = '点击解密按钮'
        self.Participant.decode_button()

    def test_b1_input_decode(self):
        self._testMethodDoc = '输入二级密码'
        self.Participant.input_decode('woniu123')

    def test_b2_decode_ok_button(self):
        self._testMethodDoc = '确定解密'
        self.Participant.decode_ok_button()


    def test_b3_modification_button(self):
        self._testMethodDoc = '点击修改按钮'
        self.Participant.modification_button()

    def test_b4_choose_button(self):
        self._testMethodDoc = '点击选择文件'
        self.Participant.choose_button('D:\\logo.png')

    def test_b5_save_button(self):
        self._testMethodDoc = '点击保存按钮'
        self.Participant.save_button()

    def test_b6_ok_button(self):
        self._testMethodDoc = '解密弹窗确认按钮'
        self.Participant.notarize_button()

    def test_b7_lookinfo_button(self):
        self._testMethodDoc = '查看/关闭指定学员信息'
        self.Participant.look_studentinfo_button()
        time.sleep(4)
        self.Participant.close_lookinfo_button()
    # # --------进入学员日常考评--------------------------------------------------------------------------------------------
    def test_b8_logout_and_login(self,name='WNCD160',passwd='WNcd1234',checkcode='0000'):
        self._testMethodDoc = '注销并切换账号,点击学员管理'
        self.Participant.logout_login_PL(name,passwd,checkcode)
        self.Participant.participants_management_button()

    def test_b9_daily_review_button(self):
        self._testMethodDoc = '点击日常考评按钮'
        self.Participant.daily_review_button()

    info = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('学员考评姓名搜索')
    @parameterized.parameterized.expand(info)
    def test_c1_input_name_search(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        self.Participant.input_name_search(arg2[0])

    def test_c2_search_exam_name_button(self):
        self._testMethodDoc = '无前置条件，点击查询'
        self.Participant.serach_name_button_exam()


    def test_c3_operation_for_examination_and_assessment_of(self,text='良'):
        self._testMethodDoc = '考评操作：作业[良]'
        self.Participant.work_select(text)
        self.Participant.work_button()

    def test_c4_morning_exam(self,text='优'):
        self._testMethodDoc = '考评操作：晨考[优]'
        self.Participant.morning_exam_select(text)
        self.Participant.morning_exam_button()

    def test_c5_login(self,name='WNCD000',passwd='woniu123',checkcode='0000'):
        self._testMethodDoc = '注销并切换管理员账号,点击学员管理'
        self.Participant.logout_login_PL(name,passwd,checkcode)
        self.Participant.participants_management_button()
    #
    # # --------进入学员周考成绩--------------------------------------------------------------------------------------------
    def test_c6_week_exam_button(self):
        self._testMethodDoc = '点击周考成绩按钮'
        self.Participant.week_exam_button()

    def test_c7_weekly_exam_button_upload_file(self,value='WNCDC10'):
        self._testMethodDoc = '点击周考导入按钮'
        time.sleep(3)
        self.Participant.weekly_exam_button()#点击周考导入按钮
        self.Participant.class_select_button(text=value)#点击班级下拉框

    def test_c8_stage_select(self,value='第一阶段'):
        self._testMethodDoc = '点击阶段下拉框'
        self.Participant.stage_select_button(text=value)

    def test_c9_upload_file(self):
        self._testMethodDoc = '点击上传文件'
        self.Participant.upload_file('D:\\logo.png')
        self.Participant.submit_button()
        a = self.Participant.uploadfile_assert()
        print(a)
        assert '确定' in a
        time.sleep(3)
        self.Participant.affirm_button()



    # 点击学员管理
    def test_d1_student(self):
        self._testMethodDoc = '点击学员管理'
        self.Participant.student_button()
        response = self.Participant.res_student()
        self.assertIn('阶段考评', response, '失败')

    #点击阶段考评
    def test_d2_evaluation(self):
        self._testMethodDoc = '点击阶段考评'
        self.Participant.evaluation_button()
        response = self.Participant.res_evaluation()
        self.assertIn('阶段考评', response, '失败')

    # 点击解密
    data = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('decrypt')
    @parameterized.parameterized.expand(data)
    def test_d3_decrypt(self, tittle, text, expected):
        self._testMethodDoc = expected
        self.Participant.decrypt()
        self.Participant.input_pws(text)
        self.Participant.confirm_button()
        print('标题:', tittle, '预期结果:', expected)

    #选择区域班级输入姓名查询
    data = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('choose')
    @parameterized.parameterized.expand(data)
    def test_d4_select(self,tittle, text, expected):
        self._testMethodDoc = expected
        self.Participant.choose_area(text[0])
        self.Participant.choose_class(text[1])
        self.Participant.input_name(text[2])
        time.sleep(1)
        self.Participant.search_button()
        time.sleep(3)
        response = self.Participant.res_search()
        self.assertIn('录入', response, '失败')
        print('标题:', tittle, '预期结果:', expected)

    #点击弹出模板进行断言
    def test_d5_template(self):
        self.Participant.template_button()
        time.sleep(3)
        self.Participant.switch_window()
        time.sleep(2)
        response = self.Participant.res_template()
        self.Participant.close_windown()
        self.Participant.current_window()
        self.assertIn('jpg', response[0], '失败')
        # 选择区域班级输入姓名查询

    #点击录入
    def test_d6_record(self):
        self._testMethodDoc = "点击录入"
        self.Participant.enter()
        time.sleep(2)
        response = self.Participant.res_record()
        self.assertIn('阶', response[0], '失败')

    #学院管理阶段考评录入
    data = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('record')
    @parameterized.parameterized.expand(data)
    def test_d7_record(self,tittle, text, expected):
        self._testMethodDoc = expected
        time.sleep(2)
        self.Participant.choose_class1(text[0])
        self.Participant.input_record(text[1])
        self.Participant.choose_stage(text[2])
        self.Participant.input_comment(text[3])
        self.Participant.save()
        self.Participant.ok()
        response = self.Participant.res_comment()
        self.assertIn('97', response, '失败')
        print('标题:', tittle, '预期结果:', expected)

    #阶段考评上传文件
    data = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('file')
    @parameterized.parameterized.expand(data)
    def test_d8_upfile(self,tittle, text, expected):
        self._testMethodDoc = expected
        time.sleep(2)
        self.Participant.import_data()
        self.Participant.import_cl(text[0])
        self.Participant.import_ph(text[1])
        self.Participant.files(text[2])
        self.Participant.uploadfile()
        self.Participant.handler_ok()
        print('标题:', tittle, '预期结果:', expected)
        # response = self.Participant.up_sucsess()
        # self.assertIn('上传', response, '失败')

    #点击综合查询k_
    def test_d9_click_comprehensive(self):
        self.Participant.achievement1()

    #综合成绩查询
    data = DataParse('../../test_data/data_web_4.xlsx').parse_excel_datas('comprehensive')
    @parameterized.parameterized.expand(data)
    def test_e1_comprehensive(self,tittle, text, expected):
        self._testMethodDoc = expected
        time.sleep(2)
        self.Participant.region_id(text[0])
        self.Participant.peOrientation(text[1])
        self.Participant.peClas(text[2])
        self.Participant.pePhase(text[3])
        self.Participant.input_peStuName(text[4])
        self.Participant.search1()
        response = self.Participant.res_search1()
        self.assertIn('柏', response, '失败')
        print('标题:', tittle, '预期结果:', expected)

    # 阶段考评点击数据导出
    # def test_8_datadown(self):
    # self.Participant.data_export()
    # self.Participant.confirm()

    # #综合成绩数据导出
    # def test_9_datadown(self):
    #     self.Participant.achievement1()
    #     self.Participant.data_download()
    #     self.Participant.save_file()


    @classmethod
    def tearDown(self):
        print("-" * 20 + "结束测试一条用例(API)" + "-" * 20)



