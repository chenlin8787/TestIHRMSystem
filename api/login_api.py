# 导包
import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login(self, jsonData, headers):
        response = requests.post(url=self.login_url, json=jsonData, headers=headers)
        return response


if __name__ == '__main__':
    login_api = LoginApi()
    jsonData = {"mobile": "13800000002", "password": "123456"}
    headers = {"Content-type": "application/json"}
    response = login_api.login(jsonData, headers)
    print("登录的结果为：", response.json())
