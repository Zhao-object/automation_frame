from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config  #读取配置
import time
class EnterprisePage(BasePage):

    def __init__(self):
        super(EnterprisePage, self).__init__()
        self.config = Config('../../test_config_data/config_web.ini')

    # 点击企业客户
    def enterprise_button(self):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'enterprise')
        self.click(*locator)

    #输入企业名称
    def input_name(self,name):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'input_name')
        self.input_text(*locator,value=name)

    #点击搜索
    def search_butoon(self):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'search_butoon')
        self.click(*locator)

    #断言
    pass

    #点击新增企业按钮
    def add__button(self):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'add_butoon')
        self.click(*locator)

    #输入企业名称
    def input_newentname(self,newentname):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'newentname')
        self.input_text(*locator,value=newentname)

    #输入企业所属行业
    def input_newentcate(self,newentcate):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'newentcate')
        self.input_text(*locator,value=newentcate)

    #输入企业地址
    def input_newentaddr(self,newentaddr):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'newentaddr')
        self.input_text(*locator, value=newentaddr)

    #输入企业联系人
    def input_newentheader(self,newentaddr):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'newentheader')
        self.input_text(*locator, value=newentaddr)

    #输入企业电话
    def input_newtel(self,newentaddr):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'newtel')
        self.input_text(*locator, value=newentaddr)

    # 点击添加按钮
    def save_butoon(self):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'save_butoon')
        self.click(*locator)

    #弹框确定
    def alert_butoon(self):
        time.sleep(2)
        self.alert_confirm()


    #断言
    pass

    #点击修改按钮
    def modify_butoon(self):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'modify_butoon1')
        self.click(*locator)

    def name_clear(self):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'entName')
        self.ele_text_clear(*locator)

    #输入企业名称
    def input_entName(self,entName):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'entName')
        self.input_text(*locator, value=entName)

    #点击保存
    def repeat_save_butoon(self):
        time.sleep(2)
        locator = self.config.parse_config('customer', 'repeat_save')
        self.click(*locator)

    #断言
    pass
