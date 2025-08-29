from automation_frame.test_business.web_employment_management_page import EmployManaPage
from automation_frame.test_parse_data.prase_data import DataParse
import unittest,time
from parameterized import parameterized


class Employ(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("-" * 20 + "开始测试一条用例(API)" + "-" * 20)
        self.employ = EmployManaPage()#实例化生成get了 一次url 的 登录页面对象

    def test_1_choose(self):
        self.employ.employ_button()
        response = self.employ.res_employ()
        self.assertIn('就业', response, '失败')

    data = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('choose')
    @parameterized.parameterized.expand(data)
    def test_2_choose(self,tittle,text,expected):
        self._testMethodDoc = tittle
        time.sleep(3)
        self.employ.choose(text[0])
        print('标题:',tittle,'预期结果:',expected)
        response = self.employ.res_choose()
        self.assertIn('操作', response, '失败')

    # 解密
    data = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('decrypt')
    @parameterized.parameterized.expand(data)
    def test_2_decrypt(self, tittle, text, expected):
        self.employ.decrypt()
        self.employ.input_pws(text)
        self.employ.confirm_button()
        print('标题:', tittle, '预期结果:', expected)

    def test_3_interview(self):
        self.employ.interview_button()
        response = self.employ.res_interview()
        self.assertIn('付文攀', response, '失败')
        self.employ.close_button()

    data = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('employ_choose')
    @parameterized.parameterized.expand(data)
    def test_4_choose(self,tittle,text,expected):
        self.employ.employ_button1()
        self.employ.choose_class(text[0])
        self.employ.choose_direction(text[1])
        self.employ.input_name(text[2])
        response = self.employ.res_search()
        self.assertIn('面试', response, '失败')
        print('标题:', tittle, '预期结果:', expected)

    def test_5_interview(self):
        self.employ.records_button()

    data = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('employ_interview')
    @parameterized.parameterized.expand(data)
    def test_6_interview(self, tittle, text, expected):
        self.employ.input_salary(text[0])
        self.employ.choose_mcomm(text[1])
        self.employ.input_mark(text[2])
        self.employ.save_button()
        self.employ.alert_butoon()
        print('标题:', tittle, '预期结果:', expected)




if __name__ == '__main__':
    unittest.main()