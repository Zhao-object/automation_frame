from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
import time

class StrainingPage(BasePage):

    def __init__(self):
        super(StrainingPage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')  # 实例化一个读取配置文件对象

    def tarin_button(self):
        xpath = self.config.parse_config('training_resources', 'tarain_button')
        self.click(*xpath)

    def Resource_base_drop_down_box(self,text):
        xpath=self.config.parse_config('training_resources','Resource_base_drop_down_box')
        self.select_text_option(*xpath,text=text)

    def Consultant_base_drop_down_box(self,text):
        xpath=self.config.parse_config('training_resources','Consultant_base_drop_down_box')
        self.select_text_option(*xpath,text=text)

    def state_base_drop_down_box(self,text):
        xpath=self.config.parse_config('training_resources','state_base_drop_down_box')
        self.select_text_option(*xpath,text=text)

    def source_base_drop_down_box(self,text):
        xpath=self.config.parse_config('training_resources','source_base_drop_down_box')
        self.select_text_option(*xpath,text=text)

    def Assign_time_input_box(self,text):
        xpath=self.config.parse_config('training_resources','Assign_time_input_box')
        self.input_text(*xpath,value=text)
        self.ele_text_clear(*xpath)

    def Training_resource_search_input_box(self,text):
        xpath=self.config.parse_config('training_resources','Training_resource_search_input_box')
        self.input_text(*xpath,value=text)
        time.sleep(1)
        self.ele_text_clear(*xpath)

    def Training_resource_search_button(self):
        xpath=self.config.parse_config('training_resources','Training_resource_search_button')
        self.click(*xpath)

    def Training_resource_tracking(self):
        xpath=self.config.parse_config('training_resources','Training_resource_tracking')
        self.click(*xpath)

    def Tracking_resources(self):
        xpath=self.config.parse_config('training_resources','Tracking_resources')
        self.click(*xpath)
        time.sleep(1)

    def Tracking_resource_current_status_drop_down_box(self,text):
        xpath=self.config.parse_config('training_resources','Tracking_resource_current_status_drop_down_box')
        self.select_text_option(*xpath,text=text)
        time.sleep(1)

    def Tracking_resource_priority_drop_down_box(self,text):
        xpath=self.config.parse_config('training_resources','Tracking_resource_priority_drop_down_box')
        self.select_text_option(*xpath,text=text)
        time.sleep(1)

    def Tracking_resource_next_tracking_input_box(self,text):
        xpath=self.config.parse_config('training_resources','Tracking_resource_next_tracking_input_box')
        self.ele_text_clear(*xpath)
        self.input_text(*xpath,value=text)
        time.sleep(1)

    def  Tracking_resource_tracking_content_input_box(self,text):
        xpath=self.config.parse_config('training_resources','Tracking_resource_tracking_content_input_box')
        self.ele_text_clear(*xpath)
        self.input_text(*xpath,value=text)
        time.sleep(1)

    def Tracking_resource_saving(self):
        xpath=self.config.parse_config('training_resources','Tracking_resource_saving')
        self.click(*xpath)
        time.sleep(1)

    def Transfer_to_responsible_person(self):
        xpath=self.config.parse_config('training_resources','Transfer_to_responsible_person')
        self.click(*xpath)
        time.sleep(1)

    def Transfer_to_responsible_person_for_inquiry(self):
        xpath=self.config.parse_config('training_resources','Transfer_to_responsible_person_for_inquiry')
        self.click(*xpath)
        time.sleep(1)

    def Transfer_to_responsible_person_for_check(self):
        xpath=self.config.parse_config('training_resources','Transfer_to_responsible_person_for_check')
        s_xpath=self.config.parse_config('training_resources','Transfer_to_responsible_person_for_check_s')
        self.click(*xpath)
        time.sleep(1)
        self.click(*s_xpath)

    def To_be_submitted_by_the_responsible_person(self,text):
        o_xpath=self.config.parse_config('training_resources','To_be_submitted_by_the_responsible_person_o')
        self.click(*o_xpath)
        t_xpath=self.config.parse_config('training_resources','To_be_submitted_by_the_responsible_person_t')
        self.select_text_option(*t_xpath,text=text)
        time.sleep(1)
        th_xpath=self.config.parse_config('training_resources','To_be_submitted_by_the_responsible_person_th')
        self.click(*th_xpath)
        f_xpath=self.config.parse_config('training_resources','To_be_submitted_by_the_responsible_person_f')
        self.click(*f_xpath)
        s_xpath=self.config.parse_config('training_resources','To_be_submitted_by_the_responsible_person_s')
        time.sleep(1)
        self.click(*s_xpath)
        time.sleep(1)

    def Allocate_resources(self):
        xpath=self.config.parse_config('training_resources','Allocate_resources')
        time.sleep(3)
        self.click(*xpath)

    def Pro_rata_distribution(self,text1,text2,text3,text4,text5):
        o_xpath=self.config.parse_config('training_resources','Pro_rata_distribution_o')
        self.click(*o_xpath)
        t_xpath=self.config.parse_config('training_resources','Pro_rata_distribution_t')
        self.input_text(*t_xpath,value=text1)
        th_xpath=self.config.parse_config('training_resources','Pro_rata_distribution_th')
        self.input_text(*th_xpath,value=text2)
        f_xpath=self.config.parse_config('training_resources','Pro_rata_distribution_f')
        self.input_text(*f_xpath,value=text3)
        s_xpath=self.config.parse_config('training_resources','Pro_rata_distribution_s')
        self.input_text(*s_xpath,value=text4)
        se_xpath=self.config.parse_config('training_resources','Pro_rata_distribution_se')
        self.input_text(*se_xpath,value=text5)
        e_xpath=self.config.parse_config('training_resources','Pro_rata_distribution_e')
        self.click(*e_xpath)
        time.sleep(2)
        n_xpath=self.config.parse_config('training_resources','Pro_rata_distribution_n')
        self.click(*n_xpath)

    def Common_resource_pool(self):
        o_xpath=self.config.parse_config('training_resources','Common_resource_pool_o')
        t_xpath=self.config.parse_config('training_resources','Common_resource_pool_t')
        self.click(*o_xpath)
        time.sleep(1)
        self.click(*t_xpath)

    def Public_resource_claim(self):
        o_xpath=self.config.parse_config('training_resources','Public_resource_claim_o')
        t_xpath=self.config.parse_config('training_resources','Public_resource_claim_t')
        th_xpath=self.config.parse_config('training_resources','Public_resource_claim_th')
        self.click(*o_xpath)
        time.sleep(1)
        self.click(*t_xpath)
        time.sleep(1)
        self.click(*th_xpath)
        time.sleep(1)










#断言
    def assert_Pro_rata_distribution(self):
        xpath = self.config.parse_config('training_resources', 'assert_Pro_rata_distribution')
        time.sleep(2)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result

    def assert_Public_resource_claim(self):
        xpath = self.config.parse_config('training_resources', 'assert_Public_resource_claim')
        time.sleep(2)
        try:
            result = self.get_ele_text(*xpath)  # 返回元素内容text
        except:
            return " "
        else:
            return result