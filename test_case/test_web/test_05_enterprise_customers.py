from automation_frame.test_business.web_enterprise_customers_page import EnterprisePage
from automation_frame.test_parse_data.prase_data import DataParse
import unittest
from parameterized import parameterized

#用例层
class Enterprise(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("-" * 20 + "开始测试一条用例(API)" + "-" * 20)
        self.enterprise = EnterprisePage()#实例化生成get了 一次url 的 登录页面对象

    enterprise = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('enterprise')
    @parameterized.parameterized.expand(enterprise)
    def test_1_name(self,tittle,name,expected):
        self._testMethodDoc = tittle
        self.enterprise.enterprise_button()
        self.enterprise.input_name(name)
        self.enterprise.search_butoon()
        print('标题:',tittle,'预期结果:',expected)

    input_text = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('add_enterprise')
    @parameterized.parameterized.expand(input_text)
    def test_2_name(self, tittle, text, expected):
        self._testMethodDoc = tittle
        self.enterprise.add__button()
        self.enterprise.input_newentname(text[0])
        self.enterprise.input_newentcate(text[1])
        self.enterprise.input_newentaddr(text[2])
        self.enterprise.input_newentheader(text[3])
        self.enterprise.input_newtel(text[4])
        self.enterprise.save_butoon()
        self.enterprise.alert_butoon()
        print('标题:', tittle, '预期结果:', expected)

    input_text = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('modify_name')
    @parameterized.parameterized.expand(input_text)
    def test_3_modify(self, tittle, text, expected):
        self._testMethodDoc = tittle
        self.enterprise.modify_butoon()
        self.enterprise.name_clear()
        self.enterprise.input_entName(text)
        self.enterprise.repeat_save_butoon()
        self.enterprise.alert_butoon()



if __name__ == '__main__':
    unittest.main()