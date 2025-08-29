from automation_frame.test_business.web_login_page import LogInPage
from automation_frame.test_parse_data.prase_data import DataParse
import unittest
from parameterized import parameterized
import requests

#用例层
class TestLogin(unittest.TestCase):

    #@classmethod
    def setUp(self):
        print("-" * 20 + "开始测试一条用例(API)" + "-" * 20)
        #先获得一个类属性
        self.loginpage = LogInPage()#实例化生成get了 一次url 的 登录页面对象

    mydata = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('weblogin')
    @parameterized.parameterized.expand(mydata)
    def test_login(self,tittle,mylist,expected):
        #这个类所有的实例都有那个类属性
        self._testMethodDoc = tittle
        self.loginpage.login_username(mylist[0])#输入账号
        self.loginpage.login_password(mylist[1])#输入密码
        self.loginpage.login_verifycode(mylist[2])#输入验证码
        self.loginpage.login_button()#点击登录
        assert expected in self.loginpage.look_login()#断言

if __name__ == '__main__':
    # mylist = ['WNCD000','woniu','0000']
    # TestLogin().test_login('登录成功',mylist,"测试账号")
    unittest.main()
