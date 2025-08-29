from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config
import time

class EmployManaPage(BasePage):

    def __init__(self):
        super(EmployManaPage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')

    # 点击就业管理
    def employ_button(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'employ_button')
        self.click(*locator)

    # 返回断言要用的值
    def res_employ(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'assert_emloy')
        response = self.get_ele_text(*locator)
        print(response)
        return response

    #点击技术面试下拉框选择
    def choose(self,text):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'select_button')
        self.select_text_option(*locator,text=text)

    # 返回断言要用的值
    def res_choose(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'assert_choose')
        response = self.get_ele_text(*locator)
        print(response)
        return response

    #点击面试按钮
    def interview_button(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'interview_button')
        self.click(*locator)

    #关闭弹窗
    def close_button(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'close_button')
        self.click(*locator)

    # 返回断言要用的值
    def res_interview(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'aseert_interview')
        response = self.get_ele_text(*locator)
        print(response)
        return response

    #点击就业管理
    def employ_button1(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'employ_button1')
        self.click(*locator)

    #点击班级下拉框选择班级
    def choose_class(self,text):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'choose_class')
        self.select_text_option(*locator,text=text)

    #点击方向下拉框选择方向
    def choose_direction(self,text):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'choose_direction')
        self.select_text_option(*locator,text=text)

    #输入姓名
    def input_name(self,name):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'input_name')
        self.ele_text_clear(*locator)
        self.input_text(*locator,value=name)

    #输入学号
    def input_number(self,number):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'input_number')
        self.input_text(*locator,value=number)

    # 返回断言要用的值
    def res_search(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'aseert_search')
        response = self.get_ele_text(*locator)
        print(response)
        return response

    # 点击解密按钮
    def decrypt(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'decrypt_button')
        self.click(*locator)

    # 输入密码
    def input_pws(self, name):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'input_pws')
        self.ele_text_clear(*locator)
        self.input_text(*locator, value=name)

    # 点击确定
    def confirm_button(self):
        time.sleep(2)
        locator = self.config.parse_config('sudent', 'confirm_button')
        self.click(*locator)

    #点击面试
    def records_button(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'records_button')
        self.click(*locator)

    #输入期望薪资
    def input_salary(self,name):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'input_salary')
        self.ele_text_clear(*locator)
        self.input_text(*locator,value=name)

    #选择沟通能力
    def choose_mcomm(self,text):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'choose_mcomm')
        self.select_text_option(*locator,text=text)

    #输入备注
    def input_mark(self,name):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'input_mark')
        self.ele_text_clear(*locator)
        self.input_text(*locator,value=name)

    # 弹框确定
    def alert_butoon(self):
        time.sleep(2)
        try:
            self.diss_alert()
        except:
            print("此处没有弹框！不用点击弹框中的确认按钮")
        else:
            print("处理弹框完成！点击了取消按钮")
            return True

    #点击保存
    def save_button(self):
        time.sleep(2)
        locator = self.config.parse_config('employ', 'save_button')
        self.click(*locator)
