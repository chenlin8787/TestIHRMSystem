# 封装通用断言函数
import os
import json


def assert_common_utils(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get('success'))
    self.assertEqual(code, response.json().get('code'))
    self.assertIn(message, response.json().get('message'))


# 封装读取登录数据的函数
def read_login_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))
    return result_list


def read_emp_data(filename, interface_name):
    with open(filename, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
     # 定义一个存放数据的空列表
        result_list = list()
        # 存放员工的某个接口的数据到空列表
        result_list.append(tuple(jsonData.get(interface_name).values()))

    return result_list


if __name__ == '__main__':
    # filename = os.path.dirname(os.path.abspath(__file__)) + "/data/login.json"
    # print("路径为：", filename)
    # result = read_login_data(filename)
    # print(result)

    # 调试读取员工数据的代码
    filename = os.path.dirname(os.path.abspath(__file__)) + "/data/emp.json"
    result = read_emp_data(filename, "modify_emp")
    print(result)
