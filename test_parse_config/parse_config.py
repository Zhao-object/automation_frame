import configparser

class Config(object):
    def __init__(self,filename='../../test_config_data/config.ini'):
        # 创建ConfigParser的对象 config 进行实例化
        self.conf = configparser.ConfigParser()
        self.filename = filename
    def parse_config(self,title,value):
        #读取config文件
        self.conf.read(self.filename,encoding='utf-8')
        #通过section拿指定的值
        self.conf.sections()
        result = self.conf.get(title,value)
        if '(' and ')' in result:
            return eval(result)
        else:
            return result

if __name__ == '__main__':
    a = Config('../test_config_data/config_web.ini').parse_config('test','test')
    print(a)
    print(type(a))