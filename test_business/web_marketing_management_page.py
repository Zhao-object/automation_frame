from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
import time
class MarketPage(BasePage):

    def __init__(self):
        super(MarketPage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')  # 实例化一个读取配置文件对象


    def marketing(self):
        locator=self.config.parse_config('marketing_management','marketing_management')
        self.click(*locator)

    def region_Dropdownbox (self,text):
        xpath=self.config.parse_config('marketing_management','region_Dropdownbox')
        # self.Drop_down_box(xpath,text)
        self.select_text_option(*xpath,text=text)

    def state_Dropdownbox(self,text):
        xpath= self.config.parse_config('marketing_management','state_Dropdownbox')
        self.select_text_option(*xpath,text=text)

    def search(self):
        xpath=self.config.parse_config('marketing_management','search')
        self.click(*xpath)

    def Upload_exclusive(self):
        xpath=self.config.parse_config('marketing_management','Upload_exclusive')
        self.click(*xpath)
        self.click()

    def Upload_resume(self,text1,text2):
        region_xpath=self.config.parse_config('marketing_management','Upload_resume_area_drop_down_box')
        self.select_text_option(*region_xpath,text=text1)
        department_xpath=self.config.parse_config('marketing_management','Upload_resume_Department_drop_down_box')
        self.select_text_option(*department_xpath,text=text2)
        Resume_document=self.config.parse_config('marketing_management','Resume_document')
        self.click(*Resume_document)
        time.sleep(2)
        self.window_inout('打开','1148','C:\\Users\\Administrator\\Desktop\\WNBOSS\\专属A简历.xls')
        self.window_button('打开(O)')

    def new_network(self):
        xpath=self.config.parse_config('marketing_management','new_network')
        self.click(*xpath)

    def new_network_resources(self,text1,text2,text3):
        region_xpath=self.config.parse_config('marketing_management','new_network_region')
        department_xpath=self.config.parse_config('marketing_management','new_network_department')
        phone_input=self.config.parse_config('marketing_management','new_network_phone_input')
        preservation_xpath=self.config.parse_config('marketing_management','new_network_preservation')
        self.select_text_option(*region_xpath,text=text1)
        self.select_text_option(*department_xpath,text=text2)
        self.ele_text_clear(*phone_input)
        self.input_text(*phone_input,value=text3)
        self.click(*preservation_xpath)
        time.sleep(2)
        self.refresh()


    #断言
    def assert_click_marketing(self):
        locator = self.config.parse_config('marketing_management', 'assert_market')  # 获得断言用的元素配置
        time.sleep(3)
        try:
            result = self.get_ele_text(*locator)  # 返回元素内容text
        except:
            return " "
        else:
            return result

    def assert_search(self):
        xpath=self.config.parse_config('marketing_management','assert_search')
        time.sleep(2)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result

    def assert_Upload_exclusive(self):
        xpath = self.config.parse_config('marketing_management', 'assert_Upload_exclusive')
        time.sleep(2)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result

    def assert_new_network(self):
        xpath=self.config.parse_config('marketing_management','assert_new_network')
        time.sleep(2)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result

if __name__ == '__main__':
    a=MarketPage()
    a.region_Dropdownbox('成都')