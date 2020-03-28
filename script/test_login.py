import unittest
import logging
from api.login_api import LoginApi
import app
# from utils import assert_common_utils
import utils


# class LoginConfig():
#     HEADERS = {"Content-type": "application/json"}


# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 编写测试函数
    # 登录成功
    def test01_login_success(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, True, 10000, "操作成功")

    # 密码错误
    def test02_password_is_error(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "13800000002", "password": "1234567"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 账号不存在
    def test03_mobile_is_not_exist(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "13900000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 输入的手机号码有英文字符
    def test04_mobile_has_eng(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "138000A0C02", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码有特殊字符
    def test05_mobile_has_special(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "138000*0#02", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码为空
    def test06_mobile_is_None(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test07_password_is_None(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "13800000002", "password": ""}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参
    def test08_more_params(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "13800000002", "password": "123456", "sign": "123"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, True, 10000, "操作成功")

    # 少手机号码
    def test09_less_mobile(self):
        # 定义登陆成功的请求体
        jsonData = {"password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 少密码
    def test10_less_password(self):
        # 定义登陆成功的请求体
        jsonData = {"mobile": "13900000002"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参
    def test11_params_is_empty(self):
        # 定义登陆成功的请求体
        jsonData = None
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 参数错误
    def test12_params_is_error(self):
        # 定义登陆成功的请求体
        jsonData = {"mboile": "13900000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        # logging.info("HEADERS里面的内容为：{}".format(app.HEADERS))
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登陆结果：响应状态码，success，code，message
        utils.assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
