from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
import time

class FinancialPage(BasePage):

    def __init__(self):
        super(FinancialPage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')  # 实例化一个读取配置文件对象

    def Enter_the_financial_flow_module(self):
        o_xpath=self.config.parse_config('financial_management','finanial_button')
        self.click(*o_xpath)
        t_xpath=self.config.parse_config('financial_management','finanial_water')
        self.click(*t_xpath)

    def New_flow(self,text):
        o_xpath=self.config.parse_config('financial_management','New_flow_o')
        self.click(*o_xpath)
        time.sleep(1)
        t_xpath=self.config.parse_config('financial_management','New_flow_t')
        self.input_text(*t_xpath,value=text)
        time.sleep(1)
        th_xpath=self.config.parse_config('financial_management','New_flow_th')
        self.click(*th_xpath)
        time.sleep(1)

    def Revision_of_flow_record(self,text):
        o_xpath=self.config.parse_config('financial_management','Revision_of_flow_record_o')
        self.click(*o_xpath)
        time.sleep(1)
        t_xpath=self.config.parse_config('financial_management','Revision_of_flow_record_t')
        self.ele_text_clear(*t_xpath)
        time.sleep(1)
        self.input_text(*t_xpath,value=text)
        th_xpath=self.config.parse_config('financial_management','Revision_of_flow_record_th')
        self.click(*th_xpath)
        time.sleep(1)
        result=self.get_alert_text()
        self.alert_confirm()
        time.sleep(1)
        f_xpath=self.config.parse_config('financial_management','Revision_of_flow_record_f')
        self.click(*f_xpath)
        return result