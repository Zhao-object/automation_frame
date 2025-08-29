from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_data.prase_data import DataParse
import unittest,warnings
from parameterized import parameterized
from automation_frame.test_parse_config.parse_config import Config

class Market(unittest.TestCase):

    @classmethod
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始".center(40, "*"))

    def test_market(self):  # 点击市场营销
        url = Config('../../test_config_data/config.ini').parse_config('url','market')
        response = Member().get_resource(url)
        self.assertEqual(response.status_code, 200,'失败')

    password = DataParse('../../test_data/data.xlsx').parse_excel_datas('decrypt')
    @parameterized.parameterized.expand(password) #解密接口
    def test_decrypt(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url', 'decrypt')
        response = Member().post_text(url,arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response, arg3, '失败')

    queryinfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('query')
    @parameterized.parameterized.expand(queryinfo)
    def test_query(self,arg1,arg2,arg3):#查询接口
        self._testMethodDoc = arg1 #unitest内置方法在报告里加标题
        url = Config('../../test_config_data/config.ini').parse_config('url', 'query')
        response = Member().post_json(url, arg2)
        print('用例标题:', arg1 ,'响应结果:', len(response))
        self.assertEqual(len(response), arg3, '失败')

    def test_Region(self):#新增网络
        url = url = Config('../../test_config_data/config.ini').parse_config('url', 'getRegion')
        response = Member().get_resource(url)
        self.assertNotEqual(response, 0, '失败')

    area = DataParse('../../test_data/data.xlsx').parse_excel_datas('area')
    @parameterized.parameterized.expand(area)
    def test_dept(self,arg1,arg2,arg3):#新增网络选择区域
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url', 'area')
        response = Member().post_json(url, arg2)
        print('用例标题:', arg1 ,'响应结果:', len(response))
        self.assertEqual(len(response), arg3, '失败')

    phone = DataParse('../../test_data/data.xlsx').parse_excel_datas('phone')
    @parameterized.parameterized.expand(phone)
    def test_area(self, arg1, arg2, arg3):  # 新增网络输入电话
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url', 'phone')
        response = Member().post_text(url, arg2)
        print('用例标题:', arg1, '响应结果:',response)
        self.assertEqual(response, 'null', '失败')

    data = DataParse('../../test_data/data.xlsx').parse_excel_datas('add')
    @parameterized.parameterized.expand(data)
    def test_add(self, arg1, arg2, arg3):  # 新增网络资源
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url', 'add_resource')
        response = Member().post_text(url, arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response, arg3, '失败')

    upfileinfo = DataParse('../../test_data/data.xlsx').parse_excel_datas('upfile')
    @parameterized.parameterized.expand(upfileinfo) #上传文件
    def test_upfile(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url', 'upfile')
        response = Member().post_upfile(url,arg2)
        self.assertEqual(response.text, arg3,'失败')

    @classmethod
    def tearDown(self):
        print("结束".center(40, "*"))


if __name__ == '__main__':
    unittest.main()
