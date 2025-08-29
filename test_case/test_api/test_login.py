from automation_frame.test_business.api_login import Login
from automation_frame.test_parse_data.prase_data import DataParse
import requests
import unittest
import warnings
from parameterized import parameterized
from automation_frame.test_parse_config.parse_config import Config

class LogIn(unittest.TestCase):

    @classmethod
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始".center(40, "*"))

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('login')
    @parameterized.parameterized.expand(loginfo)
    def test_login_api(self,arg1,arg2,arg3):  # 登录接口
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url','login')
        print("url",url)
        login_text = Login().login_api(url,arg2)
        print('用例标题:', arg1, '参数：', arg2, '响应结果:', login_text[0])
        self.assertEqual(login_text[0],arg3 ,'失败')

    @classmethod
    def tearDown(self):
        print("结束".center(40, "*"))


if __name__ == '__main__':
    unittest.main()
