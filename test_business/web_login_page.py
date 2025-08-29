from automation_frame.test_business.web_base_page import BasePage
from automation_frame.test_parse_config.parse_config import Config#读取配置
from selenium.common.exceptions import NoSuchElementException
import time

#登录页面(包含页面内各个元素!包含断言)
class LogInPage(BasePage):

    def __init__(self):
        super(LogInPage, self).__init__()#继承
        self.config = Config('../../test_config_data/config_web.ini')#实例化一个读取配置文件对象
        url = self.config.parse_config("url",'url')#获取url
        self.driver.get(url)#打开url
    #用户名输入框!
    def login_username(self,username):
        #获取元素配置
        locator = self.config.parse_config("login",'userName_locator')
        self.input_text(*locator,value=username)#输入账号
    #密码输入框!
    def login_password(self,password):
        #获取元素配置
        locator = self.config.parse_config("login", 'userPass_locator')
        self.input_text(*locator,value=password)#输入密码

    #验证码输入框!
    def login_verifycode(self,verifycode):
        # 获取元素配置
        locator = self.config.parse_config("login", 'checkcode_locator')
        self.ele_text_clear(*locator)#清空验证码
        self.input_text(*locator,value=verifycode)#输入验证码

    #登录按钮!
    def login_button(self):
        # 获取元素配置
        locator = self.config.parse_config("login", 'login_button_locator')
        self.click(*locator)#点击登录

###断言部分####
    def look_login(self):
        locator = self.config.parse_config('login', 'user_locator')  # 获得断言用的元素配置
        time.sleep(5)
        try:
            result = self.get_ele_text(*locator) #返回元素内容text
        except NoSuchElementException:
            return "失败"
        else:
            return result
if __name__ == '__main__':
    page = LogInPage()
    page.login_username("WNCD000")
    page.login_password('woniu')
    page.login_verifycode('0000')
    page.login_button()
    result = page.look_login()
    print('结果',result)