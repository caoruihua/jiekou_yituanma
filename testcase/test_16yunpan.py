#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_16yunpan.py
# @Author: Feng
# @Date  : 2018/11/5
# @Desc  :

import json
import sys
import unittest

import requests

sys.path.append('../..')

from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info


class Yunpan(unittest.TestCase):
    u"""查看云盘"""

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "yunpan")  # 读取TestUserReg工作簿的所有数据

    def test_01yupan_list(self):
        u"""查看云盘文件"""
        case_data = get_test_data(self.data_list, 'test_yudisk_list')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.post(url=url, data=data.encode(), headers=hearder2)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_common_shuoming', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
