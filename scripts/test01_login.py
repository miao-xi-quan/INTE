# 导包
import unittest

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
    # 获取AplLogin对象
        cls.apl_login = ApiLogin()
    # 登录测试方法
    def test01_login(self,mobile="13800000002",password="123456"):
    # 调用业务方法
        r = self.apl_login.api_login(mobile,password)
    # 提取token
        token = r.json().get("data")
        api.headers['Authorization'] = "Bearer " + token
        print("登录成功header值位:",api.headers)
    # 断言
        assert_common(self,r)