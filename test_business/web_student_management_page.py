from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config
import time


class StudentPage(BasePage):

    def __init__(self):
        super(StudentPage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')

    # 点击学员管理管理
    def student_button(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'student_button')
        self.click(*locator)

    #返回断言要用的值
    def res_student(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'atten')
        response= self.get_ele_text(*locator)
        print(response)
        return response

    #点击解密按钮
    def decrypt(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'decrypt_button')
        self.click(*locator)

    #输入密码
    def input_pws(self, name):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'input_pws')
        self.ele_text_clear(*locator)
        self.input_text(*locator, value=name)

    #点击确定
    def confirm_button(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'confirm_button')
        self.click(*locator)

   # 点击班级下拉框
    def choose_class(self, text):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'choose_class')
        self.select_text_option(*locator, text=text)

    # 点击方向下拉框
    def choose_direction(self, text):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'choose_direction')
        self.select_text_option(*locator, text=text)

    # 点击最新状态
    def choose_stau(self, text):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'choose_stau')
        self.select_text_option(*locator, text=text)

    # 输入姓名
    def input_name(self, name):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'input_name')
        self.ele_text_clear(*locator)
        self.input_text(*locator, value=name)

    # 点击搜索
    def search_button(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'search_button')
        self.click(*locator)

    # 返回断言要用的值
    def res_look(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'look')
        response = self.get_ele_text(*locator)
        return response

    #点击今日考勤
    def atten_button(self,*locator):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'atten')
        self.click(*locator)

    # 返回断言要用的值
    def res_atten(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'atten_button')
        response = self.get_ele_text(*locator)
        return response

