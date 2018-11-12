#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_16yunpan.py
# @Author: Feng
# @Date  : 2018/11/5
# @Desc  :

import unittest
import requests
import json
import sys
import os
sys.path.append('../..')

from config.config import *
from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info



class wxapp(unittest.TestCase):
    u'''小程序'''

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "WXAPP")  # 读取TestUserReg工作簿的所有数据

    def test_01wxapp_sns(self):
        u'''查看吐槽-个人中心'''
        case_data = get_test_data(self.data_list, 'test_wxapp_sns')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.get(url=url,headers=hearder2)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_wxapp_sns', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)



    def test_02wxapp_TucaoList(self):
        u'''查看吐槽列表'''
        case_data = get_test_data(self.data_list, 'test_wxapp_tucaolist')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.post(url=url,data=data.encode(),headers=hearder2)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_wxapp_sns', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_03wxapp_subscribe(self):
        u'''查看基本描述'''
        case_data = get_test_data(self.data_list, 'test_wxapp_subscribe')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.post(url=url,data=data.encode(),headers=hearder2)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_wxapp_subscribe', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_04wxapp_badges(self):
        u'''吐槽筛选'''
        case_data = get_test_data(self.data_list, 'test_wxapp_shaixuan')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.get(url=url,headers=hearder2)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_wxapp_shaixuan', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)


    def test_05wxapp_find_problem(self):
        u'''吐槽详情查看'''
        case_data = get_test_data(self.data_list, 'test_wxapp_findproblem')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.post(url=url,data=data.encode(),headers=hearder3)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_wxapp_find_problem', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_06wxapp_find_problem_jindu(self):
        u'''吐槽进度'''
        case_data = get_test_data(self.data_list, 'test_wxapp_findproblem_jindu')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.post(url=url,data=data.encode(),headers=hearder3)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_wxapp_find_problem_jindu', url, data, expect_res,
                      json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)


    def test_07wxapp_find_problem_remind(self):
        u'''吐槽进度'''
        case_data = get_test_data(self.data_list, 'test_wxapp_findproblem_remind')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.post(url=url,data=data.encode(),headers=hearder3)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_wxapp_find_problem_remind', url, data, expect_res,
                      json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)








if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例