# 导包
import unittest
import logging
import app

from api.emp_api import EmpApi
from utils import assert_common_utils

from api.login_api import LoginApi


class TestEmp(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = LoginApi()
        self.emp_api = EmpApi()
        # 定义员工模块的url
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    def tearDown(self):
        pass

    # 编写测试员工增删改查的案例
    def test01_test_emp_operation(self):
        # 1 实现登录接口
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        headers=app.HEADERS)
        #   获取登录接口返回的json数据
        result = response.json()
        # 输出登录的结果
        logging.info("员工登录接口的结果为：{}".format(result))
        #   把令牌提取出来，并保存到请求头当中
        token = result.get('data')
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        # 2 实现添加员工接口
        response = self.emp_api.add_emp("卡子666", "13676789883", headers)
        # 打印添加的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        #   获取添加员工返回的json数据
        add_result = response.json()
        #   把员工id提取出来，并保存到变量当中
        emp_id = add_result.get('data').get('id')
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
        # 3 实现查询员工接口
        # 发生查询员工的接口请求
        response = self.emp_api.query_emp(emp_id, headers)
        # 打印查询员工的结果
        logging.info("查询员工的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
        # 4 实现修改员工接口
        # 发生修改员工的接口请求
        response = self.emp_api.modify_emp(emp_id, "卡卡卡卡子666", headers)
        # 打印修改员工的结果
        logging.info("修改员工的结果为：{}".format(response.json()))
        # 导包
        import pymysql
        # 链接数据库
        conn = pymysql.connect(host='182.92.81.159', user='readuser', password='iHRM_user_2019', database='ihrm')
        # 获取游标
        cursor = conn.cursor()
        # 执行SQL语句
        sql = "select username from bs_user where id={}".format(emp_id)
        logging.info("打印SQL语句：{}".format(sql))
        cursor.execute(sql)
        result = cursor.fetchone()
        logging.info("执行SQL语句查询的结果为：{}".format(result))
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        self.assertEqual("卡卡卡卡子666", result[0])
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
        # 5 实现删除员工接口
        # 发生删除员工的接口请求
        response = self.emp_api.delete_emp(emp_id, headers)
        # 打印删除员工的结果
        logging.info("删除员工的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
