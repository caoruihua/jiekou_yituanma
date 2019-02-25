#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_19uaa.py
# @Author: Feng
# @Date  : 2018/11/2
# @Desc  :


import json
import sys
import unittest

import requests

from lib.util import Login

sys.path.append('../..')

from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info


class Eapp(unittest.TestCase):
    """应用ID相关"""

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "Eapp")  # 读取TestUserReg工作簿的所有数据
        cls.header7 = Login.head()

    def test_01_Eapp_chajian(self):
        u"""相关插件"""
        case_data = get_test_data(self.data_list, 'test_Eapp_chajian')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_uaa_invite_mobile', url, data, expect_res, json.dumps(res.json()))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_02_Eapp_applets_orders(self):
        u"""通知中心卡片顺序接口"""
        case_data = get_test_data(self.data_list, 'test_Eapp_applets_order')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_Eapp_applets_order', url, data, expect_res, json.dumps(res.json()))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_03_Eapp_applets_favorate(self):
        u"""应用中心"我常用的"接口"""
        case_data = get_test_data(self.data_list, 'test_Eapp_applets_favorrite')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_Eapp_applets_favorrite', url, data, expect_res, json.dumps(res.json()))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_04_Eapp_applets_all(self):
        u"""首页所有卡片接口"""
        case_data = get_test_data(self.data_list, 'test_Eapp_applets_ALL')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_Eapp_applets_ALL', url, data, expect_res, json.dumps(res.json()))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_05_Eapp_applets_catalog(self):
        u"""首页所有卡片数据接口"""
        case_data = get_test_data(self.data_list, 'test_Eapp_applets_catalog')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_Eapp_applets_catalog', url, data, expect_res, json.dumps(res.json()))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_06_Eapp_applets_edit(self):
        u"""编辑我常用的"""
        case_data = get_test_data(self.data_list, 'test_Eapp_applets_edit')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_Eapp_applets_edit', url, data, expect_res, json.dumps(res.json()))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
