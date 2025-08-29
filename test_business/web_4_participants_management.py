# 资源管理
# -*- coding: UTF-8 -*-
from selenium.common.exceptions import NoSuchElementException
from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
import time,re

class ParticipantsManagementPage(BasePage):
    def __init__(self):
        super(ParticipantsManagementPage, self).__init__()
        self.config = Config('../../test_config_data/config_web_4.ini')  # 实例化一个读取配置文件对象
#######################学员信息,日常考评,周考成绩######################
    def participants_management_button(self):#学员管理按钮
        locator = self.config.parse_config("ParticipantsManagement", 'participants_management_button')
        self.click(*locator)

    def student_info_button(self):#学员信息按钮
        locator = self.config.parse_config("ParticipantsManagement", 'student_info_button')
        self.click(*locator)

    def student_area_select(self,text):#区域下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'student_area_select')
        time.sleep(2)
        self.select_text_option(*locator,text=text)

    def student_orientation_select(self,text):#方向下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'student_orientation_select')
        time.sleep(2)
        self.select_text_option(*locator, text=text)

    def student_class_select(self,text):#班级下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'student_class_select')
        time.sleep(3)
        self.select_text_option(*locator, text=text)

    def student_status_select(self,text):#状态下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'student_status_select')
        time.sleep(3)
        self.select_text_option(*locator, text=text)

    def student_sweep_away(self,text='全部'):#清除区域、方向、班级、状态
        area = self.config.parse_config("ParticipantsManagement", 'student_area_select')
        self.select_text_option(*area, text=text)
        time.sleep(2)
        orientation = self.config.parse_config("ParticipantsManagement", 'student_orientation_select')
        self.select_text_option(*orientation, text=text)
        time.sleep(2)
        sclass = self.config.parse_config("ParticipantsManagement", 'student_class_select')
        self.select_text_option(*sclass, text=text)
        time.sleep(2)
        status = self.config.parse_config("ParticipantsManagement", 'student_status_select')
        self.select_text_option(*status, text=text)

    def input_search_name(self,value):#按姓名搜索
        locator = self.config.parse_config("ParticipantsManagement", 'search_name')
        time.sleep(2)
        self.ele_text_clear(*locator)
        self.input_text(*locator,value=value)

    def search_button(self):#搜索
        locator = self.config.parse_config("ParticipantsManagement", 'search_button')
        time.sleep(2)
        self.click(*locator)

    def modification_button(self):#修改按钮
        locator = self.config.parse_config("ParticipantsManagement", 'modification_button')
        time.sleep(2)
        self.click(*locator)

    def choose_button(self,path):#选择文件上传
        locator = self.config.parse_config("ParticipantsManagement", 'choose_button')
        time.sleep(1)
        self.input_text(*locator,value=path)

    def save_button(self):#保存
        locator = self.config.parse_config("ParticipantsManagement", 'save_button')
        time.sleep(2)
        self.click(*locator)

    def decode_button(self):#解密按钮
        locator = self.config.parse_config("ParticipantsManagement", 'decode_button')
        time.sleep(2)
        self.click(*locator)

    def input_decode(self,password):#输入二级密码
        locator = self.config.parse_config("ParticipantsManagement", 'input_decode')
        self.input_text(*locator, value=password)

    def decode_ok_button(self):#解密确定按钮
        locator = self.config.parse_config("ParticipantsManagement", 'decode_ok_button')
        self.click(*locator)

    def notarize_button(self):#保存弹窗确认按钮
        time.sleep(3)
        locator = self.config.parse_config("ParticipantsManagement", 'notarize_button')
        self.click(*locator)

    def look_studentinfo_button(self):#查看学生信息
        locator = self.config.parse_config("ParticipantsManagement", 'look_studentinfo_button')
        self.click(*locator)

    def close_lookinfo_button(self):#关闭查看信息
        locator = self.config.parse_config("ParticipantsManagement", 'close_lookinfo')
        self.click(*locator)

    def daily_review_button(self):#导航日常考评按钮
        time.sleep(2)
        locator = self.config.parse_config("ParticipantsManagement", 'daily_review_button')
        self.click(*locator)

    def week_exam_button(self):#导航周考成绩按钮
        time.sleep(2)
        locator = self.config.parse_config("ParticipantsManagement", 'week_exam_button')
        self.click(*locator)


    def logout_login_PL(self,name,passwd,checkcode):#注销并且切换账号
        # 注销
        locator = self.config.parse_config("ParticipantsManagement", 'logout_button')
        self.click(*locator)
        # 账号
        time.sleep(2)
        userName_locator = self.config.parse_config("login", 'userName_locator')
        self.ele_text_clear(*userName_locator)
        time.sleep(2)
        self.input_text(*userName_locator,value=name)
        # 密码
        userPass_locator = self.config.parse_config("login", 'userPass_locator')
        self.ele_text_clear(*userPass_locator)
        time.sleep(2)
        self.input_text(*userPass_locator, value=passwd)
        # 验证码
        checkcode_locator = self.config.parse_config("login", 'checkcode_locator')
        self.ele_text_clear(*checkcode_locator)
        time.sleep(2)
        self.input_text(*checkcode_locator, value=checkcode)
        # 登录按钮
        login_button_locator = self.config.parse_config("login", 'login_button_locator')
        self.click(*login_button_locator)

    def input_name_search(self,name):#学员考评姓名搜索
        inputlocator = self.config.parse_config("ParticipantsManagement", 'check_search_name_button')
        self.input_text(*inputlocator,value=name)
        time.sleep(3)
        searchlocator = self.config.parse_config("ParticipantsManagement", 'input_search_name_button')
        self.click(*searchlocator)
        self.ele_text_clear(*inputlocator)

    def serach_name_button_exam(self):#清空输入框，点击搜索
        inputlocator = self.config.parse_config("ParticipantsManagement", 'check_search_name_button')
        self.ele_text_clear(*inputlocator)
        searchlocator = self.config.parse_config("ParticipantsManagement", 'input_search_name_button')
        self.click(*searchlocator)

    def work_select(self,text):#作业考评下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'work_select')
        self.select_text_option(*locator, text=text)

    def work_button(self):#作业按钮
        locator = self.config.parse_config("ParticipantsManagement", 'work_button')
        time.sleep(2)
        self.click(*locator)

    def morning_exam_select(self,text):#晨考考评下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'morning_exam_select')
        self.select_text_option(*locator, text=text)

    def morning_exam_button(self):
        time.sleep(2)
        locator = self.config.parse_config("ParticipantsManagement", 'morning_exam_button')
        self.click(*locator)

    def admin_button(self, name, passwd, checkcode):# 注销并且切换账号
        # 注销
        locator = self.config.parse_config("ParticipantsManagement", 'logout_button')
        self.click(*locator)
        # 账号
        time.sleep(2)
        userName_locator = self.config.parse_config("login", 'userName_locator')
        self.ele_text_clear(*userName_locator)
        time.sleep(2)
        self.input_text(*userName_locator, value=name)
        # 密码
        userPass_locator = self.config.parse_config("login", 'userPass_locator')
        self.ele_text_clear(*userPass_locator)
        time.sleep(2)
        self.input_text(*userPass_locator, value=passwd)
        # 验证码
        checkcode_locator = self.config.parse_config("login", 'checkcode_locator')
        self.ele_text_clear(*checkcode_locator)
        time.sleep(2)
        self.input_text(*checkcode_locator, value=checkcode)
        # 登录按钮
        login_button_locator = self.config.parse_config("login", 'login_button_locator')
        self.click(*login_button_locator)

    def weekly_exam_button(self):#周考导入按钮
        locator = self.config.parse_config("ParticipantsManagement", 'weekly_exam_button')
        self.click(*locator)

    def class_select_button(self,text):#班级下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'class_select')
        self.select_text_option(*locator, text=text)

    def stage_select_button(self,text):#阶段下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'stage_select')
        self.select_text_option(*locator, text=text)

    def upload_file(self,path):#选择文件上传
        locator = self.config.parse_config("ParticipantsManagement", 'upload_file')
        time.sleep(1)
        self.input_text(*locator,value=path)

    def submit_button(self):#提交按钮
        time.sleep(2)
        locator = self.config.parse_config("ParticipantsManagement", 'submit_button')
        self.click(*locator)

    def uploadfile_assert(self):#上传文件格式断言
        time.sleep(3)
        locator = self.config.parse_config("ParticipantsManagement", 'affirm_button')
        self.get_ele_text(*locator)
        return self.get_ele_text(*locator)

    def affirm_button(self):#上传弹窗确认按钮
        time.sleep(1)
        locator = self.config.parse_config("ParticipantsManagement", 'affirm_button')
        self.click(*locator)

    # -------------断言------------------------------------------------------------------------------------------------
    def assert_go_studentinfo(self):#判断正确进入学员信息页面
        locator = self.config.parse_config("ParticipantsManagement", 'go_studentinfo')
        self.get_ele_text(*locator)
        return self.get_ele_text(*locator)

    def assert_areainfo(self):#区域下拉框断言
        locator = self.config.parse_config("ParticipantsManagement", 'student_area_select')
        self.try_return_ele_textORfaile(*locator)
        return self.try_return_ele_textORfaile(*locator)

    def assert_orientation(self):#方向下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'student_orientation_select')
        self.try_return_ele_textORfaile(*locator)
        return self.try_return_ele_textORfaile(*locator)

    def assert_class(self):#班级下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'student_class_select')
        self.try_return_ele_textORfaile(*locator)
        return self.try_return_ele_textORfaile(*locator)

    def assert_status(self):#状态下拉框
        locator = self.config.parse_config("ParticipantsManagement", 'student_status_select')
        self.try_return_ele_textORfaile(*locator)
        return self.try_return_ele_textORfaile(*locator)
#############################阶段,综合#########################################################
# 点击学员管理
    def student_button(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'student_button')
        self.click(*locator)

    # 返回学员管理断言要用的值
    def res_student(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'evaluation')
        response = self.get_ele_text(*locator)
        return response

    # 点击阶段考评
    def evaluation_button(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'evaluation')
        self.click(*locator)

    # 返回阶段考评断言要用的值
    def res_evaluation(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'res_evaluation')
        response = self.get_ele_text(*locator)
        return response

    # 点击解密按钮
    def decrypt(self):
        time.sleep(2)
        locator = self.config.parse_config('decrypt', 'decrypt_button')
        self.click(*locator)

    # 输入密码
    def input_pws(self, name):
        time.sleep(2)
        locator = self.config.parse_config('decrypt', 'input_pws')
        self.ele_text_clear(*locator)
        self.input_text(*locator, value=name)

    #密码错误点击确定
    def mistake_button(self):
        time.sleep(2)
        locator = self.config.parse_config('decrypt', 'res_decrypt')
        self.click(*locator)

    # 点击确定
    def confirm_button(self):
        time.sleep(2)
        locator = self.config.parse_config('decrypt', 'confirm_button')
        self.click(*locator)

    #返回解密断言要用的值
    def res_decrypt(self):
        time.sleep(2)
        locator = self.config.parse_config('decrypt', 'res_decrypt')
        response = self.get_ele_text(*locator)
        return response

    # 点击区域下拉框选择方向
    def choose_area(self, text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'area')
        self.select_text_option(*locator, text=text)

    # 点击班级下拉框选择班级
    def choose_class(self, text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'class')
        self.select_text_option(*locator, text=text)

    # 输入姓名
    def input_name(self, name):
        time.sleep(2)
        locator = self.config.parse_config('student', 'name')
        self.ele_text_clear(*locator)
        self.input_text(*locator, value=name)

    # 点击查询
    def search_button(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'search')
        self.click(*locator)

    # 返回查询断言要用的值
    def res_search(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'res_search')
        response = self.get_ele_text(*locator)
        return response

    #点击查看模板
    def template_button(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'template')
        self.click(*locator)

    #切换窗口
    def swich_window(self):
        self.switch_window()

    def current_window(self):
        self.switch_current_window()

    #获取元素值断言
    def res_template(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'res_template')
        response = self.get_attribute_outer(*locator)
        response1=re.findall(r'src="(.*?)" alt=',response)
        print('获取元素值',response1)
        return response1

    #关闭窗口
    def close_windown(self):
        self.close_handle()

    #点击录入
    def enter(self):
        time.sleep(3)
        locator = self.config.parse_config('student', 'enter_button')
        self.click(*locator)

    # 返回点击录入断言要用的值
    def res_record(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'res_record')
        response = self.get_ele_text(*locator)
        return response

    #选择班级
    def choose_class1(self, text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'choose_class')
        self.select_text_option(*locator, text=text)

    #输入成绩
    def input_record(self, name):
        time.sleep(2)
        locator = self.config.parse_config('student', 'input_record')
        self.ele_text_clear(*locator)
        self.input_text(*locator, value=name)

    #选择阶段
    def choose_stage(self, text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'choose_stage')
        self.select_text_option(*locator, text=text)

    #输入评语
    def input_comment(self, conment):
        time.sleep(2)
        locator = self.config.parse_config('student', 'input_comment')
        self.ele_text_clear(*locator)
        self.input_text(*locator, value=conment)

    #点击保存
    def save(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'save_button')
        self.click(*locator)

    #输入不对点击保存弹出的弹框
    def ok(self):
        try:
            time.sleep(2)
            locator = self.config.parse_config('student', 'ok_button')
            self.click(*locator)
        except NoSuchElementException as e:
            print('此处没有这个元素')
        else:
            print('元素已出现')

    # 返回录入成绩断言要用的值
    def res_comment(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'res_comment')
        response = self.get_ele_text(*locator)
        return response

    #点击数据导出
    def data_export(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'data_export')
        self.click(*locator)
        time.sleep(2)

    #点击确定导出
    def confirm(self):
        self.window_radiobutton("正在打开 阶段考试记录.xls","保存文件")
        self.window_button("正在打开 阶段考试记录.xls","确定")

    #点击阶段导入
    def import_data(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'import')
        self.click(*locator)

    #选择班级
    def import_cl(self,text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'import_cl')
        self.select_text_option(*locator, text=text)

    #选择阶段
    def import_ph(self,text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'import_ph')
        self.select_text_option(*locator, text=text)

    #上传文件
    def files(self,filepath):
        time.sleep(2)
        locator = self.config.parse_config('student', 'files')
        self.input_text(*locator, value=filepath)

    #点击提交
    def uploadfile(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'uploadfile')
        self.click(*locator)

    #文件内容不正确点击确定
    def handler_ok(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'handler_ok')
        self.click(*locator)

    #上传文件断言
    def up_sucsess(self):
        try:
            time.sleep(2)
            locator = self.config.parse_config('student', 'up_sucsess')
            response = self.get_ele_text(*locator)
        except NoSuchElementException as e:
            print('此处没有这个元素')
        else:
            return response
            print('元素已出现')

    #点击综合成绩
    def achievement1(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'achievement1')
        self.click(*locator)

    #综合成绩点击数据导出
    def data_download(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'data_download')
        self.click(*locator)

    #保存文件
    def save_file(self):
        self.window_radiobutton("正在打开 综合评估.xls" , "保存文件")
        self.window_button("正在打开 综合评估.xls", "确定")

    #综合成绩查询选择区域
    def region_id(self,text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'region_id')
        self.select_text_option(*locator, text=text)

    # 综合成绩查询选择方向
    def peOrientation(self,text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'peOrientation')
        self.select_text_option(*locator, text=text)

    # 综合成绩查询选择班级
    def peClas(self, text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'peClas')
        self.select_text_option(*locator, text=text)

    # 综合成绩查询选择阶段
    def pePhase(self, text):
        time.sleep(2)
        locator = self.config.parse_config('student', 'pePhase')
        self.select_text_option(*locator, text=text)

    #综合成绩查询输入姓名
    def input_peStuName(self, name):
        time.sleep(2)
        locator = self.config.parse_config('student', 'peStuName')
        self.ele_text_clear(*locator)
        self.input_text(*locator, value=name)

    #点击查询
    def search1(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'search1')
        self.click(*locator)

    #查询断言要用的值
    # 返回录入成绩断言要用的值
    def res_search1(self):
        time.sleep(2)
        locator = self.config.parse_config('student', 'res_search1')
        response = self.get_ele_text(*locator)
        return response