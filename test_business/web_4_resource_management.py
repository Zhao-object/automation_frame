# 资源管理
# -*- coding: UTF-8 -*-
from selenium.common.exceptions import NoSuchElementException
from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
import time
#资源管理页面
class ResourceManagementPage(BasePage):

    def __init__(self):
        super(ResourceManagementPage, self).__init__()
        self.config = Config('../../test_config_data/config_web_4.ini')  # 实例化一个读取配置文件对象

    #资源管理按钮
    def resource_button(self):
        locator = self.config.parse_config("navigaion","resource_manage")
        self.click(*locator)

    #咨询主管资源管理按钮
    def consult_resource_manage_button(self):
        locator = self.config.parse_config("navigaion", "consult_resource_manage")
        self.click(*locator)

    # 咨询主管分配资源按钮
    def consult_resource_manage_allocate_button(self):
        locator = self.config.parse_config("navigaion", "consult_resource_manage_allocate")
        self.click(*locator)

    #培训资源按钮
    def train_resource_button(self):
        locator = self.config.parse_config("train_resource", "train_resource_button")
        self.click(*locator)

    #分配资源按钮
    def allocate_resource_button(self):
        locator = self.config.parse_config("allocat_resource", "allocat_resource_button")
        self.click(*locator)



    #解密按钮
    def train_resource_decode(self):
        locator = self.config.parse_config("train_resource", "train_resource_decode_button")
        self.click(*locator)

    #解密输入密码输入框
    def train_resource_input(self,text):
        locator = self.config.parse_config("train_resource","train_resource_input")
        self.input_text(*locator,value=text)

    #解密确定按钮
    def train_resource_affirm(self):
        locator = self.config.parse_config("train_resource","train_resource_confirm")
        self.click(*locator)

###解密断言(培训资源)###
    def look_train_resource_decode(self):
        locator_faile = self.config.parse_config("train_resource","train_resource_decode_faile_look")
        locator_success = self.config.parse_config("train_resource","train_resource_decode_success_look")
        locator_faile_yes = self.config.parse_config("train_resource","train_resource_decode_faile_yes")
        locator_cancel_decode = self.config.parse_config("train_resource","train_resource_cancel")
        try:
            result = self.get_ele_text(*locator_faile)
        except NoSuchElementException:
            result = self.get_ele_text(*locator_success)
            if '*' not in result:
                return '解密成功'
            else:
                return '解密失败'
        else:
            time.sleep(0.5)
            self.click(*locator_faile_yes)
            time.sleep(0.5)
            self.click(*locator_cancel_decode)
            return result

    ###解密断言(分配资源)###
    def look_train_resource_decode_two(self):
        locator_faile = self.config.parse_config("train_resource", "train_resource_decode_faile_look")
        locator_success = self.config.parse_config("train_resource", "train_resource_decode_success_look_two")
        locator_faile_yes = self.config.parse_config("train_resource", "train_resource_decode_faile_yes")
        locator_cancel_decode = self.config.parse_config("train_resource", "train_resource_cancel")
        try:
            result = self.get_ele_text(*locator_faile)
        except NoSuchElementException:
            result = self.get_ele_text(*locator_success)
            if '*' not in result:
                return '解密成功'
            else:
                return '解密失败'
        else:
            time.sleep(0.5)
            self.click(*locator_faile_yes)
            time.sleep(0.5)
            self.click(*locator_cancel_decode)
            return result

    #培训资源资源库下拉框
    def train_lib_select(self,text):
        locator = self.config.parse_config("train_resource","resource_lib_select")
        self.select_text_option(*locator,text=text)

##资源库下拉框断言##
    def look_train_lib_select(self):
        locator = self.config.parse_config("train_resource", "resource_lib_select")
        result = self.try_return_ele_textORfaile(*locator)
        return result

    #培训资源状态下拉框
    def train_status_select(self,text):
        locator = self.config.parse_config("train_resource","status_select")
        self.select_text_option(*locator,text=text)

    #培训资源来源下拉框
    def train_source_select(self,text):
        locator = self.config.parse_config("train_resource","source_select")
        self.select_text_option(*locator,text=text)

    #培训资源分配时间开始时间输入框
    def train_stat_time_input(self,text):
        locator = self.config.parse_config("train_resource", "start_time_input")
        self.input_text(*locator,value=text)

    # 培训资源分配时间结束时间输入框
    def train_end_time_input(self, text):
        locator = self.config.parse_config("train_resource", "end_time_input")
        self.input_text(*locator, value=text)

    #搜索按钮
    def train_search(self):
        locator = self.config.parse_config("train_resource", "search_button")
        self.click(*locator)

###搜索断言###
    def look_train_search(self):
        locator = self.config.parse_config("train_resource","look_search")
        return self.try_return_ele_passORfaile(*locator)

    #培训资源区域下拉框
    def train_area_select(self,text):
        locator = self.config.parse_config("train_resource", "area_select")
        self.select_text_option(*locator, text=text)

##区域下拉框断言##
    def look_train_area_select(self):
        locator = self.config.parse_config("train_resource", "area_select")
        result = self.try_return_ele_textORfaile(*locator)
        return result

    #培训资源新增按钮
    def train_add_resource_buttob(self):
        locator = self.config.parse_config("train_resource", "add_button")
        self.click(*locator)


    #培训资源电话输入框
    def train_phone_input(self,text):
        locator = self.config.parse_config("train_resource", "add_phone_input")
        self.input_text(*locator,value=text)

    #姓名输入框
    def train_name_input(self,text):
        locator = self.config.parse_config("train_resource", "add_name_input")
        self.input_text(*locator,value=text)

    #最新状态下拉框
    def train_status_select(self,text):
        locator = self.config.parse_config("train_resource", "add_status_select")
        self.select_text_option(*locator,text=text)

    #渠道来源下拉框
    def train_source_select(self,text):
        locator = self.config.parse_config("train_resource", "add_source_select")
        self.select_text_option(*locator,text=text)

    #保存新增资源保存按钮
    def train_add_resource_save_button(self):
        locator = self.config.parse_config("train_resource", "add_save_button")
        self.click(*locator)

##新增资源保存断言###
    def look_add_resource_save(self):
        locator_phone = self.config.parse_config("train_resource","add_phone_input")#手机
        locator_add_success = self.config.parse_config("train_resource", "look_add_success")#新增成功
        update_locator = self.config.parse_config("train_resource","look_add_success_update")#已更新资源
        yes_locator = self.config.parse_config("train_resource", "add_success_yes")#提示信息确定
        try:
            self.find_element(*update_locator)
        except NoSuchElementException:
            try:
                self.find_element(*locator_add_success)
            except NoSuchElementException:
                locator = ('xpath',"//*[@id='form-add']/div/div/div/button")
                time.sleep(1)
                self.click(*locator)
                time.sleep(1)
                return "新增或更新失败"
            else:
                locator = ('xpath',"//button[@data-bb-handler='ok']")
                time.sleep(1)
                self.click(*locator)
                time.sleep(1)
                return "新增成功"
        else:
            locator = ('xpath',"//button[@data-bb-handler='ok']")
            time.sleep(1)
            self.click(*locator)
            time.sleep(1)
            return "更新该资源成功"


    #跟踪资源按钮
    def train_resource_tail_button(self):
        locator = self.config.parse_config("train_resource", "tail_button")
        self.click(*locator)

    #跟踪资源跟踪资源按钮
    def train_resource_tail_taile_button(self):
        locator = self.config.parse_config("train_resource", "tail_tail")
        self.click(*locator)

    #跟踪资源状态下拉框
    def train_resource_tail_status_select(self,text):
        locator = self.config.parse_config("train_resource", "tail_status_select")
        self.select_text_option(*locator,text=text)

    #跟踪资源优先级别下拉框
    def train_resource_tail_leval_select(self,text):
        locator = self.config.parse_config("train_resource", "leval_select")
        self.select_text_option(*locator,text=text)

    #跟踪优先级别下次跟踪时间输入框
    def train_resource_next_tail_time_input(self,text):
        locator = self.config.parse_config("train_resource", "next_tail_input")
        js = "document.getElementsByName('t.next_time')[0].value=" + text
        self.execute_js(js)


    #跟踪内容文本域
    def train_resource_text_content_input(self,text):
        locator = self.config.parse_config("train_resource", "tail_content_input")
        self.input_text(*locator,value=text)

    #报名信息a连接
    def train_resource_apply_info_a(self):
        locator = self.config.parse_config("train_resource", "tail_apply_a")
        self.click(*locator)

    #入读班级下拉框
    def train_resource_read_class_select(self,text):
        locator = self.config.parse_config("train_resource", "tail_read_class")
        self.select_text_option(*locator,text=text)

    # 应交学费下拉框
    def train_resource_pay_money_select(self, text):
        locator = self.config.parse_config("train_resource", "tail_pay_money_select")
        self.select_text_option(*locator, text=text)

    #支付方式下拉框
    def train_resource_pay_way_select(self, text):
        locator = self.config.parse_config("train_resource", "tail_pay_way_select")
        self.select_text_option(*locator, text=text)

    # 收入帐户下拉框
    def train_resource_pay_account_select(self, text):
        locator = self.config.parse_config("train_resource", "tail_pay_account_select")
        self.select_text_option(*locator, text=text)

    #保存按钮
    def train_resource_tail_save_button(self):
        locator = self.config.parse_config("train_resource", "tail_tail_save")
        self.click(*locator)

###跟踪资源成功断言###
    def look_train_resource_tail(self):
        locator = self.config.parse_config("train_resource", "tail_success")
        result = self.try_return_ele_textORfaile(*locator)
        return result

    #保存成功确定按钮
    def train_resource_tail_affirm_button(self):
        locator = self.config.parse_config("train_resource", "tail_success_affirm")
        self.click(*locator)

    #修改资源按钮
    def train_resource_update_button(self):
        locator = self.config.parse_config("train_resource", "update_button")
        self.click(*locator)

    #最后跟踪输入框
    def train_resource_update_end_tail_textarea(self,text):
        locator = self.config.parse_config("train_resource", "update_end_tail")
        self.ele_text_clear(*locator)
        self.input_text(*locator,value=text)

    #修改资源保存按钮
    def train_resource_update_save_button(self):
        locator = self.config.parse_config("train_resource","update_resource_save")
        self.click(*locator)

###修改资源断言###
    def look_update_resource(self):
        locator = self.config.parse_config("train_resource","look_update_resource")
        result = self.try_return_ele_textORfaile(*locator)
        return result

    #废弃资源学生
    def train_resource_waste_student(self):
        locator = self.config.parse_config("train_resource", "train_resource_waste_student")
        locator_student_name = self.config.parse_config("train_resource", "waste_student_name")
        waste_student_name = self.get_ele_text(*locator_student_name)
        self.click(*locator)
        return waste_student_name #返回被废弃的学生

    #废弃按钮
    def train_resource_waste_buttn(self):
        locator = self.config.parse_config("train_resource", "train_resource_waste_button")
        self.click(*locator)


    #废弃确认按钮
    def train_resource_waste_yes(self):
        locator = self.config.parse_config("train_resource", "train_resource_yes")
        self.click(*locator)

##废弃功能断言###
    def look_train_resource_waste(self,waste_student_name):
        locator_common = self.config.parse_config("train_resource","common_resource_button")
        locator_train = self.config.parse_config("train_resource","train_resource_button")
        self.click(*locator_common)
        time.sleep(2)
        locator_name = self.config.parse_config("train_resource","train_resource_common_waste_student")
        result = self.try_return_ele_textORfaile(*locator_name)
        self.click(*locator_train)
        if waste_student_name == result:
            return '废弃成功'
        else:
            return '废弃失败'

######分配资源#######
    #注销按钮
    def logout(self):
        locator = self.config.parse_config("allocat_resource", "logout_button")
        self.click(*locator)

    #分配资源渠道下拉框
    def allot_resource_ditch_select(self,text):
        locator = self.config.parse_config("allocat_resource", "ditch_select")
        self.select_text_option(*locator,text=text)

###分配资源渠道下拉框断言###
    def look_allot_resource_ditch_select(self):
        locator = self.config.parse_config("allocat_resource", "ditch_select")
        result = self.try_return_ele_textORfaile(*locator)
        return result

    #分配资源第一个资源勾选框
    def allot_resource_first_check(self):
        locator = self.config.parse_config("allocat_resource", "allocat_first_check")
        self.click(*locator)


    # 分配资源分配简历选择框
    def allot_resource_resume_select(self,text):
        locator = self.config.parse_config("allocat_resource", "allocat_resume_select")
        self.select_text_option(*locator,text=text)

    #分配资源提交按钮
    def allot_resource_submit_button(self):
        locator = self.config.parse_config("allocat_resource", "submit_button")
        self.click(*locator)

    # 分配资源提交再次确定按钮
    def allot_resource_submit_again_button(self):
        locator = self.config.parse_config("allocat_resource", "again_submit_button")
        self.click(*locator)


###分配资源提交断言###
    def look_allot_resource_submit(self):
        locator = self.config.parse_config("allocat_resource", "look_allocat_resource_submit")
        result = self.try_return_ele_passORfaile(*locator)
        return result

    #消息提示确定
    def allot_resource_submit_third_button(self):
        locator = self.config.parse_config("allocat_resource", "third_submit_button")
        self.click(*locator)


    #分配资源输入框
    def allot_resource_ditch_input(self, text):
        locator = self.config.parse_config("allocat_resource", "alloca_resource_input")
        self.input_text(*locator,value=text)

###分配资源输入框断言###
    def look_allot_resource_input(self):
        locator = self.config.parse_config("allocat_resource", "alloca_resource_input")
        result = self.return_execute_js("document.getElementsByName('cusInfo')[0].value")
        return result



    #分配资源提交消息提示确定按钮
    def allot_resource_submit_affirm_button(self):
        locator = self.config.parse_config("allocat_resource", "submit_affirm_button")
        self.click(*locator)


###分配资源提交按钮断言###
    def look_allot_resource_submit_button(self):
        locator = self.config.parse_config("allocat_resource","look_submit_div")
        result = self.try_return_ele_textORfaile(*locator)
        return result

    #按比例分配按钮
    def allot_resource_ratio_allot(self):
        locator = self.config.parse_config("allocat_resource", "ratio_allot")
        self.click(*locator)


###按比例分配按钮断言###
    def look_allot_resource_ratio_allot(self):
        locator = self.config.parse_config("allocat_resource", "ratio_allot_submit")
        result = self.try_return_ele_passORfaile(*locator)
        return result

    #按比例分配输入框
    def allot_resource_ratio_input(self,text):
        locator = self.config.parse_config("allocat_resource", "ratio_allot_input")
        self.ele_text_clear(*locator)
        self.input_text(*locator,value=text)

    #按比例分配提交按钮
    def allot_resource_ratio_submit(self):
        locator = self.config.parse_config("allocat_resource", "ratio_allot_submit")
        self.click(*locator)

    # 按比例分配确定按钮
    def allot_resource_ratio_submit_affirm(self):
        locator = self.config.parse_config("allocat_resource", "ratio_allot_affirm")
        self.click(*locator)

###按比例分配断言###
    def look_ratio_allot(self):
        locator = self.config.parse_config("allocat_resource","look_ratio_allot")
        result = self.try_return_ele_textORfaile(*locator)
        return result

    # 按比例分配成功提示二次确定按钮
    def allot_resource_ratio_submit_two_affirm(self):
        locator = self.config.parse_config("allocat_resource", "again_ratio_allot_affirm")
        self.click(*locator)

###########公共,转交##############################################################
    def Access_to_public_resources(self):
        o_xpath=self.config.parse_config('resource_management','Enter_resource_management')
        xpath = self.config.parse_config('resource_management', 'Access_to_public_resources')
        self.click(*o_xpath)
        time.sleep(0.5)
        self.click(*xpath)

    def Common_resources_area_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Common_resources_area_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Public_resources_department_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Public_resources_department_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Drop_down_box_of_the_last_abandoned_public_resources(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management',
                                         'Drop_down_box_of_the_last_abandoned_public_resources')
        self.select_text_option(*xpath, text=text)

    def Public_resource_status_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Public_resource_status_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Public_resource_source_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Public_resource_source_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Public_resources_education_dropdown_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Public_resources_education_dropdown_box')
        self.select_text_option(*xpath, text=text)

    def Public_resource_query_input_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Public_resource_query_input_box')
        self.input_text(*xpath, value=text)
        self.ele_text_clear(*xpath)

    def Query_button(self):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Query_button')
        self.click(*xpath)

    def Public_resource_claim(self):
        one_xpath = self.config.parse_config('resource_management', 'one_Public_resource_claim')
        two_xpath = self.config.parse_config('resource_management', 'two_Public_resource_claim')
        three_xpath = self.config.parse_config('resource_management', 'three_Public_resource_claim')
        four_xpath = self.config.parse_config('resource_management', 'four_Public_resource_claim')
        time.sleep(1)
        self.click(*one_xpath)
        time.sleep(2)
        self.click(*two_xpath)
        time.sleep(2)
        self.click(*three_xpath)
        time.sleep(2)
        self.click(*four_xpath)

    def Transfer_of_resources(self):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Transfer_of_resources')
        self.click(*xpath)

    def Query_area_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Query_area_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Query_Department_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Query_Department_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Query_consultant_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Query_consultant_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Query_status_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Query_status_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Query_source_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Query_source_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Transfer_resource_query_input_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Transfer_resource_query_input_box')
        self.ele_text_clear(*xpath)
        time.sleep(1)
        self.input_text(*xpath, value=text)

    def Transfer_resource_inquiry(self):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Transfer_resource_inquiry')
        self.click(*xpath)

    def Transfer_area_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Transfer_area_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Transfer_department_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Transfer_department_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def Transfer_to_consultant_drop_down_box(self, text):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'Transfer_to_consultant_drop_down_box')
        self.select_text_option(*xpath, text=text)

    def see(self):
        time.sleep(1)
        xpath = self.config.parse_config('resource_management', 'see')
        self.click(*xpath)
        time.sleep(2)

    def Forward_resource_submission(self):
        time.sleep(1)
        o_xpath = self.config.parse_config('resource_management', 'Forward_resource_submission_o')
        self.click(*o_xpath)
        time.sleep(1)
        t_xpath = self.config.parse_config('resource_management', 'Forward_resource_submission_t')
        self.click(*t_xpath)
        time.sleep(1)
        th_xpath = self.config.parse_config('resource_management', 'Forward_resource_submission_th')
        self.click(*th_xpath)
        time.sleep(1)
        f_xpath = self.config.parse_config('resource_management', 'Forward_resource_submission_f')
        self.click(*f_xpath)

    # 断言
    def assert_Query_button(self):
        xpath = self.config.parse_config('resource_management', 'assert_Query_button')
        time.sleep(2)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result

    def assert_Public_resource_claim(self):
        xpath = self.config.parse_config('resource_management', 'assert_Public_resource_claim')
        time.sleep(2)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result

    def assert_Transfer_of_resources(self):
        xpath = self.config.parse_config('resource_management', 'assert_Transfer_of_resources')
        time.sleep(1)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result

    def assert_see(self):
        xpath = self.config.parse_config('resource_management', 'assert_see')
        time.sleep(1)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result

    def assert_Forward_resource_submission(self):
        xpath = self.config.parse_config('resource_management', 'assert_resource_management')
        time.sleep(1)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result






























    #分配资源按钮
    def allocat_resource_button(self):
        locator = self.config.parse_config("allocat_resource", "allocat_resource_button")
        self.click(*locator)

    #



        