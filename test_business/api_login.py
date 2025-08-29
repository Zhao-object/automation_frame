import requests

class Login():

    def __init__(self):

        self.session = requests.session()

    def login_api(self,url,data):
        log = self.session.post(url=url,data=data)
        login_text = log.text
        return login_text,self.session
