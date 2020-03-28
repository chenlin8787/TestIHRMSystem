import unittest
import logging

from parameterized import parameterized

from api.login_api import LoginApi
import app
import utils


# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义要加载的登录数据的路径
    filename = app.BASE_DIR + "/data/login.json"

    # 编写测试函数
    # 登录
    @parameterized.expand(utils.read_login_data(filename))
    def test01_login(self, case_name, jsonData, http_code, success, code, message):
        # 定义登陆成功的请求体
        jsonData = jsonData
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, http_code, success, code, message)
