import unittest,time,os,requests,sys

from HTMLTestRunner import HTMLTestRunner
class TestSuite():

    def do_test(self,filename):
        """
        discover()方法有3个参数
        start_dir表示测试的模块名称或者测试用例的目录
        pattern='test*.py'表示测试用例文件名的匹配规则，请注意文件名以test开头
        top_level_dir=NONE表示测试模块的顶层目录
        """
        # 定义测试用例的目录为当前目录
        test_dir = '../../test_case/' + filename
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
        now = time.strftime("%Y-%m-%d %H-%M-%S") # #按照一定的格式获取当前的时间
        # 定义报告存放路径'..\\report\\report.html'
        dir_path = './report'
        report_filename =  now + 'report.html'
        filename = os.path.join(dir_path, report_filename)
        with open(filename, "w",encoding='utf-8')as f:
            # 定义测试报告
            runner = HTMLTestRunner(stream=f, title='woniuboss2.5 automation report', description="oniuboss2.5 unittest framework")
            # 运行测试
            runner.run(discover)

if __name__ == '__main__':
   # TestSuite().do_test('test_api')
   # TestSuite().do_test("test_web")
   TestSuite().do_test("test_web")


