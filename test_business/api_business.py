import requests

from automation_frame.test_business.api_login import Login
from automation_frame.test_parse_config.parse_config import Config

class Member():

    def __init__(self):
        # 调用配置层test_parse_config中的parse_config模块 拿到登录要用的参数
        loginfo = Config().parse_config('count','loginfo')
        # 将拿到的登录的参数转换成字典形式
        loginfo = eval(loginfo)
        # 调用业务层test_business中的api_login_page模块 拿到session
        url = Config().parse_config('url', 'login')
        self.result = Login().login_api(url,loginfo)
        # 将session赋值给变量s
        self.session = self.result[1]

    #post请求拿到响应文本的方法
    def post_text(self,url,data):
        response = self.session.post(url=url,data=data)
        print('接口响应：', response.text)
        return response.text

    #post请求拿到响应json数据的方法
    def post_json(self,url,data):
        response = self.session.post(url=url,data=data)
        print('接口响应：', response.json())
        return response.json()

    #post请求拿到响应码的方法
    def post_status_code(self, url, data):
        response = self.session.post(url=url, data=data)
        print('接口响应：', response.status_code)
        return response.status_code


    # post上传文件方法(传参）
    def post_upfile(self, url,file):
        response = self.session.post(url=url,files=file)
        print('接口响应：', response.text)
        return response

    #get请求获取资源的方法
    def get_resource(self,url):
        response = self.session.get(url=url)
        print('接口响应：',response.status_code)
        return response

    # get请求获取资源的方法(传参）
    def get_resource_data(self,url,data):
        response = self.session.get(url=url,params=data)
        print('接口响应：', response.status_code)
        return response

    #post请求获取资源的方法(url传参）
    def post_resource_data_params(self, url, data, params):
        response = self.session.post(url=url, params=params, data=data)
        print('接口响应：', response.status_code)
        return response


if __name__ == '__main__':
    pass
