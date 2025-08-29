from automation_frame.test_business.api_business import Member
from automation_frame.test_parse_data.prase_data import DataParse
import unittest,warnings
from parameterized import parameterized
from automation_frame.test_parse_config.parse_config import Config

class BackStage(unittest.TestCase):

    @classmethod
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始".center(40, "*"))

    bk_query = DataParse('../../test_data/data.xlsx').parse_excel_datas('bk_query')
    @parameterized.parameterized.expand(bk_query) #后台管理用户管理查询接口
    def test_query(self,arg1,arg2,arg3):
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url','bk_query')
        response = Member().post_json(url,arg2)
        print('用例标题:', arg1, '响应结果:', len(response))
        self.assertEqual(len(response),arg3, '失败')

    add_tree = DataParse('../../test_data/data.xlsx').parse_excel_datas('add_tree')
    @parameterized.parameterized.expand(add_tree)  # 后台管理资源树接口
    def test_addtree(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url', 'add_tree')
        response = Member().post_text(url, arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response, arg3, '失败')

    dic_add = DataParse('../../test_data/data.xlsx').parse_excel_datas('dic_add')
    @parameterized.parameterized.expand(dic_add)  # 后台管理字典管理新增接口
    def test_dicadd(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url','bk_dicadd')
        response = Member().post_text(url, arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response, arg3, '失败')

    dic_start = DataParse('../../test_data/data.xlsx').parse_excel_datas('dic_start')
    @parameterized.parameterized.expand(dic_start)  # 后台管理字典管理启用接口
    def test_dicstart(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url','bk_dicstart')
        response = Member().post_text(url, arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response, arg3, '失败')

    dic_stop = DataParse('../../test_data/data.xlsx').parse_excel_datas('dic_stop')
    @parameterized.parameterized.expand(dic_stop)  # 后台管理字典管理停用接口
    def test_dicstop(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url','bk_dicstop')
        response = Member().post_text(url, arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response, arg3, '失败')

    dic_edit = DataParse('../../test_data/data.xlsx').parse_excel_datas('dic_edit')
    @parameterized.parameterized.expand(dic_edit)  # 后台管理字典管理停用接口
    def test_dicstop(self, arg1, arg2, arg3):
        self._testMethodDoc = arg1
        url = Config('../../test_config_data/config.ini').parse_config('url','bk_dicedit')
        response = Member().post_text(url, arg2)
        print('用例标题:', arg1, '响应结果:', response)
        self.assertEqual(response, arg3, '失败')

    @classmethod
    def tearDown(self):
        print("结束".center(40, "*"))


if __name__ == '__main__':
    unittest.main()