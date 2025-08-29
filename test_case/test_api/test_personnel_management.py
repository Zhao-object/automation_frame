from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_config.parse_config import Config
from automation_frame.test_parse_data.prase_data import DataParse
from parameterized import parameterized
import requests,unittest,warnings

class API_personnel(unittest.TestCase):
    @classmethod
    def setUp(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始".center(40, "*"))

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('员工管理搜索')
    @parameterized.parameterized.expand(loginfo)
    def test_Employee_search(self,arg1,arg2,arg3):
        url=Config('../../test_config_data/config.ini').parse_config('url','Employee_search')
        self._testMethodDoc = arg1
        response = Member().post_text(url, arg2)
        self.assertIn(arg3,response,'失败')


    loginfo =DataParse('../../test_data/data.xlsx').parse_excel_datas('员工管理新增')
    @parameterized.parameterized.expand(loginfo)
    def test_Employee_add(self,arg1,arg2,arg3):
        url=Config('../../test_config_data/config.ini').parse_config('url','Employee_add')
        self._testMethodDoc = arg1
        print('标题',arg1)
        response=Member().post_text(url,arg2)
        self.assertEqual(response,arg3,'失败')

    loginfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('员工管理修改')
    @parameterized.parameterized.expand(loginfo)
    def test_Employee_modify(self, arg1, arg2, arg3):
        url=Config('../../test_config_data/config.ini').parse_config('url','Employee_modify')
        self._testMethodDoc = arg1
        response=Member().post_text(url,arg2)
        self.assertEqual(response,arg3,'失败')




    @classmethod
    def tearDown(cls):
        print("结束".center(40, "*"))

if __name__ == '__main__':
    unittest.main()