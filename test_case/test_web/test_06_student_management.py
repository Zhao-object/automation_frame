from automation_frame.test_business.web_student_management_page import StudentPage
from automation_frame.test_parse_data.prase_data import DataParse
import unittest,time
from parameterized import parameterized


class Studen(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("-" * 20 + "开始测试一条用例(API)" + "-" * 20)
        self.student = StudentPage()#实例化生成get了 一次url 的 登录页面对象

    #点击学员管理
    def test_1_student(self):
        self.student.student_button()
        response = self.student.res_student()
        self.assertIn('今日',response,'失败')

    # #解密
    # data = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('decrypt')
    # @parameterized.parameterized.expand(data)
    # def test_2_decrypt(self,tittle,text,expected):
    #     self.student.decrypt()
    #     self.student.input_pws(text)
    #     self.student.confirm_button()
    #     print('标题:', tittle, '预期结果:', expected)

    #搜索查询学院基本信息
    data = DataParse('../../test_data/data_web.xlsx').parse_excel_datas('student')
    @parameterized.parameterized.expand(data)
    def test_3_student(self,tittle,text,expected):
        self._testMethodDoc = tittle
        self.student.choose_class(text[0])
        self.student.choose_direction(text[1])
        self.student.choose_stau(text[2])
        self.student.input_name(text[3])
        self.student.search_button()
        print('标题:',tittle,'预期结果:',expected)
        response = self.student.res_look()
        self.assertIn('查看', response, '失败')

    # 点击今日考勤
    def test_4_atten(self):
        self.student.atten_button()
        response = self.student.res_atten()
        self.assertIn('批量', response, '失败')


